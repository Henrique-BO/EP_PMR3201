# Bibliotecas Python
import sys
from statistics import *
import matplotlib.pyplot as plt
import numpy as np

# Classes desenvolvidas para o Simulador de Filas
from AleatorioAlunos import *
from FilasAlunos import *
            
# definir aqui a funcao simulacao
def simulacao():
  # Cria todos os clientes e coloca na fila de eventos
  Dtev1 = fexp(lambdacliente_hour/3600, duracaoexpediente_hour*3600)
  clienteid, time1 = 0, 0
  fe = FilaEventos()
  for i in range(len(Dtev1)):
    time1 += Dtev1[i]
    cliente = Cliente(clienteid, 1, time1)
    fe.insereFilaEventos((time1, cliente))
    clienteid += 1
  
  # Processa os eventos enquanto existir algum
  while not fe.FilvaEventosVazia():
    cliente = fe.retiraFilaEventos() # objeto do tipo Cliente
    clock = cliente.get_timeEvento(cliente.get_tipoEvento()) # Tempo de ocorrencia do evento
    
    # Evento 1: Cliente chegou
    if cliente.get_tipoEvento() == 1:
      # Ha algum caixa livre: cliente comeca o atendimento imediatamente
      caixa_livre = verificaCaixaLivre(sinalCaixaLivre)
      if caixa_livre[0]:
        cliente.set_tipoEvento(2)
        cliente.set_timeEvento(clock, 2)
        cliente.set_caixaid(caixa_livre[1])
        fe.insereFilaEventos((clock, cliente))
        sinalCaixaLivre[caixa_livre[1]] = False
      # Nao ha caixa livre: cliente entra na menor fila para esperar seu atendimento
      else:
        menor_fila = achaMenorFila(vetorFilaCaixa)
        cliente.set_caixaid(menor_fila)
        vetorFilaCaixa[menor_fila].insereFilaCaixa(cliente)
        # Tamanhos da fila foram modificados
        preenche_log(clock)

    # Evento 2: Cliente inicia atendimento
    # Cria um novo Evento 3 para o instante em que o cliente vai terminar de ser atendido
    elif cliente.get_tipoEvento() == 2:
      caixa = cliente.get_caixaid()
      Dt_atend = TempoDeAtendimentoCaixa(vetorTaxaDeAtendimentoCaixa[caixa]/3600, tempominimodeatendimento)
      cliente.set_tipoEvento(3)
      cliente.set_timeEvento(clock + Dt_atend, 3)
      fe.insereFilaEventos((clock + Dt_atend, cliente))

    # Evento 3: Cliente encerra atendimento
    elif cliente.get_tipoEvento() == 3:
      saida.insereListaSaida(cliente)
      caixa = cliente.get_caixaid()
      # Nao ha mais ninguem na fila: caixa passa a estar livre
      if vetorFilaCaixa[caixa].FilaCaixaEstaVazia():
        sinalCaixaLivre[caixa] = True
      # Tem alguem na fila: esse cliente comeca o atendimento (caixa continua nao-livre)
      else:
        proximo_cliente = vetorFilaCaixa[caixa].retiraFilaCaixa()
        proximo_cliente.set_tipoEvento(2)
        proximo_cliente.set_timeEvento(clock, 2)
        fe.insereFilaEventos((clock, proximo_cliente))
        # Tamanhos da fila foram modificados
        preenche_log(clock)

  return saida, logfilas
      
  
def preenche_log(clock):
  log = [clock] + TamanhoDasFilas(vetorFilaCaixa)
  logfilas.append(log)


# Programa main
if __name__ == "__main__":

  # taxa de chegada de clientes por hora
  # A simulacao usa segundos mas a taxa por hora e' de
  # mais facil compreeensao para o usuario
  lambdacliente_hour = 70
  
  # Duracao total do expediente em horas
  duracaoexpediente_hour = 6

  # Numero de repeticoes da simulacao
  numeroderepeticoes = 50

  # Definicao dos caixas 
  nCaixas = int(input("Digite o número de caixas: "))
  vetorFilaCaixa = nCaixas*[None]
  for k in range(0,nCaixas):
      vetorFilaCaixa[k]=FilaCaixa()

    
  # Taxa de atendimento de cada caixa por hora
  # Definida como 15 clientes/hora para todos os caixas em todos os projetos
  vetorTaxaDeAtendimentoCaixa = nCaixas*[15]

  # Minimo tempo de atendimento em qualquer caixa
  tempominimodeatendimento = 120

  # Lista que indica que so i-esimo caixa esta disponivel para o atendimento
  # Um caixa so estara livre se nenhum cliente estiver sendo atendido e a sua fila estiver vazia
  sinalCaixaLivre = nCaixas*[True]

  print("\n===============================================================\n")

  print("Executando %d simulações com os seguintes parâmetros:" % numeroderepeticoes)
  print("\tTaxa de chegada de clientes:", lambdacliente_hour, "clientes/hora")
  print("\tDuração do expediente:", duracaoexpediente_hour, "h")
  print("\tNúmero de caixas:", nCaixas)
  print("\tTaxa de atendimento de clientes:")
  for i in range(nCaixas):
    print("\t\tCaixa %d: %d clientes/hora" % (i, vetorTaxaDeAtendimentoCaixa[i]))
  print("\tTempo mínimo de atendimento:", tempominimodeatendimento, "s")

  print("\n===============================================================\n")


  # lista de clientes onde sao colocados os objetos da classe
  # Cliente quando e' terminado o atendimento 
  saida = ListaClientesSaida()
  
  # Listas que guardam o logfilas e o conjunto de estatisticas de 
  # todas as repeticoes da simulacao, para serem usados posteriormente
  logfilas_iteracoes = []
  estatisticas_iteracoes = []

  # Executa as simulacoes e calcula as medias globais (considerando todas as iteracoes)
  media_tempo_espera = 0
  media_tempo_atendimento = 0
  media_tempo_total = 0
  num_medio_fila = [0]*nCaixas # Numero medio de clientes de cada fila
  for i in range(numeroderepeticoes):
    # logfilas: lista para monitoracao das filas
    # No inicio [[0,0,0,0]] tempo=0 e tamanho das filas = 0
    # A cada operacao de insercao de cliente na fila ou remocao
    # o estado de todas as filas e' checado 
    # formando uma sub-lista [clock, tam fila1, tam fila 2, tam fila 3]
    # sub-lista e' acrescentada na lista 
    logfilas = [[0]+nCaixas*[0]]

    # Executa a simulação
    saida, logfilas = simulacao()

    # Calculo das estatisticas de cada iteracao:
    # Media, variancia, tempo na fila, tempo no atendimento e tempo total
    estatisticas = calculaEstatisticas(saida, logfilas)

    # Calculo das medias globais (considerando todas as repeticoes)
    media_tempo_espera += estatisticas[0][0]/numeroderepeticoes
    media_tempo_atendimento += estatisticas[0][1]/numeroderepeticoes
    media_tempo_total += estatisticas[0][2]/numeroderepeticoes
    for i in range(nCaixas):
      num_medio_fila[i] += estatisticas[2][i]/numeroderepeticoes

    logfilas_iteracoes.append(logfilas)
    estatisticas_iteracoes.append(estatisticas)

  # Calcula as variancias globais (considerando todas as repeticoes)
  variancia_tempo_espera = 0
  variancia_tempo_atendimento = 0
  variancia_tempo_total = 0
  variancia_num_medio_fila = [0]*nCaixas
  for i in range(numeroderepeticoes):
    variancia_tempo_espera += (estatisticas_iteracoes[i][0][0] - media_tempo_espera)**2/numeroderepeticoes
    variancia_tempo_atendimento += (estatisticas_iteracoes[i][0][1] - media_tempo_atendimento)**2/numeroderepeticoes
    variancia_tempo_total += (estatisticas_iteracoes[i][0][2] - media_tempo_total)**2/numeroderepeticoes
    for j in range(nCaixas):
      variancia_num_medio_fila[j] += (estatisticas_iteracoes[i][2][j] - num_medio_fila[j])**2/numeroderepeticoes

  # Numero medio de clientes na fila (considerando todas as filas) e sua variancia
  num_medio_fila_geral = 0
  for i in range(nCaixas):
    num_medio_fila_geral += num_medio_fila[i]/nCaixas
  variancia_num_medio_fila_geral = 0
  for i in range(nCaixas):
    variancia_num_medio_fila_geral += (num_medio_fila[i] - num_medio_fila_geral)**2 / nCaixas

  print("Tempo médio de espera (s):", media_tempo_espera, "+/-", np.sqrt(variancia_tempo_espera))
  print("Tempo médio de atendimento (s):", media_tempo_atendimento, "+/-", np.sqrt(variancia_tempo_atendimento))
  print("Tempo total médio (s):", media_tempo_total, "+/-", np.sqrt(variancia_tempo_total))
  print("Número médio de pessoas em filas:", num_medio_fila_geral)
  for i in range(nCaixas):
    print("\tFila " + str(i) + ":", num_medio_fila[i], "+/-", np.sqrt(variancia_num_medio_fila[i]))
  print("\nObs.: Valores mostrados como 'média +/- desvio_padrão'")

  print("\n===============================================================\n")

  # Plot do estado das filas ao longo do tempo
  # numero de subplots e' dependente de nCaixas
  # cada subplot e'incorporado sequencialmente
  # x = tempo da simulacao em segundos
  # y = tamanho de uma das filas
  mostrar = input("Iteracao a ser mostrada ('q' para sair): ")
  while mostrar != "q":
    mostrar = int(mostrar)
    logfilas = logfilas_iteracoes[mostrar]
    fig, ax = plt.subplots(nCaixas)
    fig.suptitle('Evolucao do Tamanho da Fila (iteração %d)'%mostrar)
    nlines = len(logfilas)
    # x recebe a coluna 0 da lista
    x = [row[0] for row in logfilas]
    for k in range(1,nCaixas+1):
      # y recebe a coluna k da lista
      y = [row[k] for row in logfilas]
      ax[k-1].step(x, y)
      ax[k-1].set_xlabel('tempo (s)')
      ax[k-1].set_ylabel('Fila'+str(k-1))
      ax[k-1].grid()
    plt.show()
    mostrar = input("Iteracao a ser mostrada ('q' para sair): ")


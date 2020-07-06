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



# Programa main
if __name__ == "__main__":

   # taxa de chegada de clientes por hora
   # A simulacao usa segundos mas a taxa por hora é demais
   # facil compreeensao para o usuario
   lambdacliente_hour = 50
   
   # Duracao total do expediente em horas
   duracaoexpediente_hour = 2

   # Definicao dos caixas 
   nCaixas=3
   vetorFilaCaixa=3*[None]
   for k in range(0,nCaixas):
       vetorFilaCaixa[k]=FilaCaixa()
     
   caixaid = None   # Identifica um determinado caixa e sua fila

   # taxa de atendimento de cada caixa por hora
   vetorTaxaDeAtendimentoCaixa=nCaixas*[None]
   vetorTaxaDeAtendimentoCaixa[0] = 15
   vetorTaxaDeAtendimentoCaixa[1] = 15
   vetorTaxaDeAtendimentoCaixa[2] = 15
   
   # caixaid = 0,1,2
   tempominimodeatendimento = 120
   sinalCaixaLivre = nCaixas*[True]

   # lista de clientes aonde sao colocados os objetos da classe
   # Cliente quando e' terminado o atendimento 
   saida = ListaClientesSaida()
   
    




   # lista para monitoracao das filas
   # No inicio [[0,0,0,0]] tempo=0 e tamanho das filas = 0
   # A cada operacao de inercao de cliente na fila ou remocao
   # o estado de todas as filas e' checado 
   # formando uma sub-lista [clock, tam fila1, tam fila 2, tam fila 3]
   # sub-lista e' acrescentada na lista 
   logfilas = [[0]+nCaixas*[0]]

                 
   # Calculo das estatisticas, Medias, Desvios Padroes
   # Media, variancia, tempo na fila, tempo no atendimento e tempo total
   
   
   # Plot do estado das filas ao longo do tempo
   # numero de subplots e' dependente de nCaixas
   # cada subplot e'incorporado sequencialmente
   # x = tempo da simulacao em segundos
   # y = tamanho de uma das filas
   # 
   fig, ax = plt.subplots(nCaixas)
   fig.suptitle('Evolucao do Tamanho da Fila')
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
   fig.canvas.draw()


from statistics import *
import random as rand
import numpy as np

#from Filas import *

#
# Gera amostras de intervalos de tempo entre chegada de clientes Dtev1
# Numero de amostras é compativel com a duracao do expediente
# - lambdacliente: taxa de chegada de clientes por segundo
# - duracaoexpediente: duracao de tempo do expediente da agencia bancaria
#   especificada em segundos 
def fexp(lambdacliente,duracaoexpediente):   
    x = 1000*[None]         # x e' alocado com 1000 posicoes
    somatoriadotempo = 0    # Somatoria dos intervalos de tempo Dtev1
    k=0
    # Amostras sao geradas ate' que a somatoria dos intervalos de tempo
    # ultrapasse a duracao do expediente
    while somatoriadotempo <= duracaoexpediente:    
        x[k] = rand.expovariate(lambdacliente)
        x[k] = int(x[k])
        somatoriadotempo = somatoriadotempo + x[k]
        k = k+1
    # retira-se o ultimo elemento que esta'alem do horario
    # do expediente                                                                                                                    
    return x[0:k-1]

#
# mucaixa: taxa de atendimento em segundos
# tempominimoatendimento: tempo minimo de atendimento em
# segundos
def TempoDeAtendimentoCaixa(mucaixa,tempominimoatendimento):
        x = int(rand.expovariate(mucaixa))
        if x >= tempominimoatendimento:
           return(x)
        else:
           return(tempominimoatendimento)

#
# Codigo que voce deve desenvolver

def calculaEstatisticas(listasaida,logfilas):
    """
    Recebe a lista de saida e o logfilas de uma simulacao especifica, 
    e retorna estatisticas correspondentes a essa iteracao.

    Essas estatisticas deverao ser tratadas novamente depois, considerando todas as iteracoes,
    para que se tenha um valor significativo, devido a natureza estocastica da simulacao.
    """
    n_clientes = listasaida.tamListaSaida()
    
    # Calculo das medias dos tempos
    media_tempo_espera = 0
    media_tempo_atendimento = 0
    media_tempo_total = 0
    while listasaida.tamListaSaida() != 0:
        cliente = listasaida.retiraListaSaida()
        media_tempo_espera += (cliente.get_timeEvento(2) - cliente.get_timeEvento(1)) / n_clientes
        media_tempo_atendimento += (cliente.get_timeEvento(3) - cliente.get_timeEvento(2)) / n_clientes
        media_tempo_total += (cliente.get_timeEvento(3) - cliente.get_timeEvento(1)) / n_clientes
    medias = [media_tempo_espera, media_tempo_atendimento, media_tempo_total]

    # Calculo das variancias dos tempos
    variancia_tempo_espera = 0
    variancia_tempo_atendimento = 0
    variancia_tempo_total = 0
    while listasaida.tamListaSaida() != 0:
        cliente = listasaida.retiraListaSaida()
        variancia_tempo_espera += ((cliente.get_timeEvento(2)-cliente.get_timeEvento(1)) - media_tempo_espera)**2 / n_clientes
        variancia_tempo_atendimento += ((cliente.get_timeEvento(3)-cliente.get_timeEvento(2)) - media_tempo_atendimento)**2 / n_clientes
        variancia_tempo_total += ((cliente.get_timeEvento(3)-cliente.get_timeEvento(1)) - media_tempo_total)**2 / n_clientes
    variancias = [variancia_tempo_espera, variancia_tempo_atendimento, variancia_tempo_total]

    # Numero medio de clientes por fila
    num_medio_fila = [0]*(len(logfilas[0]) - 1)
    T_final = logfilas[-1][0]
    for i in range(1, len(logfilas)):
        dt = logfilas[i][0] - logfilas[i-1][0]
        for j in range(len(num_medio_fila)):
            num_medio_fila[j] += logfilas[i][j+1]*dt/T_final
    
    return [medias, variancias, num_medio_fila]






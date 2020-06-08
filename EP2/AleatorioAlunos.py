from statistics import *
import random as rand

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
#
#def calculaEstatisticas(listasaida,logfilas):
#
#    < insira aqui o seu codigo >
#            
#         
#
#
#


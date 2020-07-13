50import numpy as np
from matplotlib import pyplot as plt
import random as rand

from AleatorioAlunos import fexp

if __name__ == "__main__":
    lambdacliente = 40/3600  # Taxa de chegadas por seg
    duracaoexpediente = 6*3600;    # Duracao do expediente em seg
    Dtev1 = fexp(lambdacliente,duracaoexpediente)
    print("Somatoria Dtev1 = ",sum(Dtev1)," Expediente 6h = ",\
          duracaoexpediente)
    # Histograma com 10 setores
    plt.hist(Dtev1,20)
    plt.show()   

class Cliente():
    def __init__(self,clienteid, tipoEvento,timeEvento1):
        self.__clienteid = clienteid
        self.__tipoEvento = tipoEvento   # tipo do evento que sera' o
                                         # proximo a ocorrer
        self.__timeEvento1 = timeEvento1 # instante de tempo de ocorrencia
                                         # do Evento 1
        self.__timeEvento2 = 0        # idem Evento 2
        self.__timeEvento3 = 0        # idem Evento 3
        self.__caixaid = 0            # identificacao do caixa
        
    def set_clienteid(self,clienteid):
        self.__clienteid = clienteid
    def get_clienteid(self):
        return(self.__clienteid)

    def set_tipoEvento(self,tipo):
        if tipo in range(1,4):        
           self.__tipoEvento = tipo
        else:
            print('Tipo de evento não existente')
            
    def get_tipoEvento(self):
        return(self.__tipoEvento)
        
    def set_timeEvento(self,time,tipoevento):
        if tipoevento == 1:
            self.__timeEvento1 = time
        else:
            if tipoevento == 2:
                self.__timeEvento2 = time
            else:
                if tipoevento == 3:
                    self.__timeEvento3 = time
#                else:
#                    print("Evento nao identificado!!!")
                    
    def get_timeEvento(self,tipoevento):
        if tipoevento == 1:
            return(self.__timeEvento1)
        else:
            if tipoevento == 2:
                return(self.__timeEvento2)
            else:
                if tipoevento == 3:
                    return(self.__timeEvento3)
#                else:
#                    print("Evento nao identificado!!!")
                    
    def set_caixaid(self,caixaid):
        self.__caixaid = caixaid
    def get_caixaid(self):
        x=self.__caixaid
        return(x)
        
    def __lt__(self, other):
        return self.__clienteid < other.__clienteid

    def __str__(self):
        x = "clienteid = " + str(self.__clienteid) + "\n" + \
             "tipoEvento  = " + str(self.__tipoEvento)  + "\n" + \
            "timeEvento1 = " + str(self.__timeEvento1) + "\n" + \
            "timeEvento2 = " + str(self.__timeEvento2) + "\n" + \
            "timeEvento3 = " + str(self.__timeEvento3) + "\n" + \
            "Caixa ID = " + str(self.__caixaid) + "\n\n"
        return(x)

# FIFO
class FilaCaixa:

    def __init__(self):
        # TODO: talvez implementar com uma permutacao circular
        self._fila = []

    def insereFilaCaixa(self, cliente):
        self._fila.append(cliente)

    def retiraFilaCaixa(self):
        return self._fila.pop(0)

    def FilaCaixaEstaVazia(self):
        return len(self._fila) == 0

    def tamFila(self):
        return len(self._fila)
        
class NoFilaEventos:
    """
    No de Lista Ligada utilizado para a implementacao
    da classe FilaEventos, ordenada por meio da chave 
    de ordenacao 'key'.
    """

    def __init__(self, x): # x == (key, cliente)
        self._key = x[0]
        self._cliente = x[1]
        self._prox = None

    def get_key(self):
        return self._key

    def get_cliente(self):
        return self._cliente

    def set_prox(self, novo):
        self._prox = novo
    def get_prox(self):
        return self._prox

class FilaEventos:

    def __init__(self):
        self._primeiro = None
    
    def insereFilaEventos(self, x):
        novo_no = NoFilaEventos(x)
        # Fila vazia: so adiciona
        if self._primeiro == None:
            self._primeiro = novo_no
        # Novo elemento a ser adicionado no inicio
        elif novo_no.get_key() <= self._primeiro.get_key():
            novo_no.set_prox(self._primeiro)
            self._primeiro = novo_no
        else:
            no = self._primeiro
            # Procura onde adicionar o elemento na lista
            while no.get_prox() and novo_no.get_key() > no.get_prox().get_key():
                no = no.get_prox()
            if no.get_prox():
                novo_no.set_prox(no.get_prox())
            no.set_prox(novo_no)
    
    def retiraFilaEventos(self):
        p = self._primeiro
        self._primeiro = self._primeiro.get_prox()
    
    def FilvaEventosVazia(self):
        return self._primeiro == None

            
class ListaClientesSaida():
    def __init__(self):
        self.__filasaida=[]
        
    def insereListaSaida(self,cliente):
        self.__filasaida.append(cliente)
        
    def retiraListaSaida(self):
        return(self.__filasaida.pop(0))
        
    def ListaSaidaVazia(self):
        if len(self.__filasaida) == 0:
            return(True)
        else:
            return(False)
    def tamListaSaida(self):
        x=len(self.__filasaida)
        return(x)

def verificaCaixaLivre(sinalCaixaLivre):
    for i in range(len(sinalCaixaLivre)):
        if sinalCaixaLivre[i]:
            return (True, i)
    return (False, None)
 
def achaMenorFila(vetorFilaCaixa):
    menor_fila = 0 # indice da menor fila
    for i in range(1, len(vetorFilaCaixa)):
        if vetorFilaCaixa[i].tamFila() < vetorFilaCaixa[menor_fila].tamFila():
            menor_fila = i
    return menor_fila

def TamanhoDasFilas(vetorFilaCaixa):
    vetorTamanhos = [None]*len(vetorFilaCaixa)
    for i in range(len(vetorFilaCaixa)):
        vetorTamanhos[i] = vetorFilaCaixa[i].tamFila()



    

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
class FilaCaixa():
        
class FilaEventos():
            
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
 
def achaMenorFila(vetorFilaCaixa):
   
def TamanhoDasFilas(vetorFilaCaixa):
 


    

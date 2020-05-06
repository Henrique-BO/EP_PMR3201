import nltk as nk
import pandas as pd
import matplotlib.pyplot as plt

# Funcao que recebe o endereco de um arquivo *.txt e a transforma em uma lista de non-stop words minusculas tokenizadas
def preProcessaTexto(filepath): #FUNCIONA
    assert filepath[-4:] == ".txt" # Checa se e um arquivo *.txt

    # Abre o arquivo e le seu conteudo
    f = open(filepath, 'r', encoding='utf8')
    raw = f.read()

    # Cria um tokenizer que mantem somente as palavras
    tokenizer = nk.tokenize.RegexpTokenizer("[\w]+")
    tokens = tokenizer.tokenize(raw)

    # Transforma todas as palvras em minusculas
    lwords = []
    for palavra in tokens:
        lwords.append(palavra.lower())

    # Carrega as stopwords da lingua inglesa e gera uma lista sem nenhuma stopword
    sw = nk.corpus.stopwords.words('english')
    words_ns = []
    for word in lwords:
        if word not in sw:
            words_ns.append(word)

    # A lista words_ns contem as non-stop words minusculas e e' retornada
    return words_ns

# Gera o dicionario de frequencias para um dado texto
def geraFrequencias(filepath): #FUNCIONA
    words_ns = preProcessaTexto(filepath)
    # Inicializa o dicionario de frequencias
    # Esse e' um dicionario de dicionarios, em que cada palavra e' representada dentro do subdicionario correspondente
    # `a sua inicial por uma entrada palavra: n_ocorrencias
    dicfreq = {'a':{}, 'b':{}, 'c':{}, 'd':{}, 'e':{}, 'f':{}, 'g':{}, 'h':{}, 'i':{}, 'j':{}, 'k':{}, 'l':{}, 'm':{}, 'n':{}, 'o':{}, 'p':{}, 'q':{}, 'r':{}, 's':{}, 't':{}, 'u':{}, 'v':{}, 'w':{}, 'x':{}, 'y':{}, 'z':{}}

    for x in words_ns:

        #TODO consertar esses erros
        if '_' in x: # Existem algumas ocorrencias da palavra _I_, contando como inicial _, logo retiramos isso para ficar so com o I
            x = x.replace('_', "")
        skip = False
        for char in x: # Evita que pegue numeros como palavras separadas
            skip = skip or char.isdigit()
        if 'à' in x:
            x = x.replace('à', 'a')
        if 'é' in x:
            x = x.replace('é', 'e')
        if 'ç' in x:
            x = x.replace('ç', 'c')
        if 'á' in x:
            x = x.replace('á', 'a')
        if 'ê' in x:
            x = x.replace('ê', 'e')
        if 'â' in x:
            x = x.replace('â', 'a')

        if skip or x == '':
            continue

        inicial = x[0]
        try:
            assert inicial in dicfreq # TESTE
        except:
            print(inicial, x)

        if x in dicfreq[inicial]:
            dicfreq[inicial][x] += 1 # Aumenta o numero de ocorrencias da palavra em 1
        else:
            dicfreq[inicial][x] = 1 # Se a palavra ainda nao apareceu ainda, colocar no dicionario

    return dicfreq

# Recebe um dicionario de dicionarios com a frequencia das palavras no texto
# e retorna uma lista com as 20 palavras mais frequentes na forma (palavra, n_ocorrencias)
def ordenaFrequencias(dicfreq):

    # Cria uma lista com todas as palavras
    l_freq = []
    for inicial in dicfreq:
        while dicfreq[inicial] != {}:
            l_freq.append(dicfreq[inicial].popitem())
    # Ordena a lista em ordem decrescente
    mergesort(l_freq)
    # Pega so as 20 palavras com a maior frequencia e retorna
    lwocorrencias = l_freq[:20]
    return lwocorrencias

# Ordena uma lista em ordem decrescente
def mergesort(L):
    tmp = [None]*len(L)
    def mergesort_rec(esquerda, direita):
        if (esquerda + 1) < direita:
            meio = (esquerda + direita)//2
            mergesort_rec(esquerda, meio)   # Ordena a parte da esquerda
            mergesort_rec(meio, direita)    # Ordena a parte da direita
            merge(esquerda, meio, direita)  # Mescla as duas metades

    # Mescla duas partes ordenadas de uma lista para formar uma unica ordenada
    def merge(esquerda, meio, direita):
        i_esquerda = esquerda   # Iterador da metade da esquerda
        i_direita = meio        # Iterador da metade da direita
        i_out = esquerda        # Iterador da lsita de saida (tmp)
        while i_esquerda < meio and i_direita < direita:
            if L[i_esquerda][1] > L[i_direita][1]:
                tmp[i_out] = L[i_esquerda]
                i_esquerda += 1
            else:
                tmp[i_out] = L[i_direita]
                i_direita += 1
            i_out += 1
        while i_esquerda < meio:
            tmp[i_out] = L[i_esquerda]
            i_esquerda += 1
            i_out += 1
        while i_direita < direita:
            tmp [i_out] = L[i_direita]
            i_direita += 1
            i_out += 1
        # Coloca a lista temporaria de volta na lista original
        for i in range(esquerda, direita):
            L[i] = tmp[i]

    mergesort_rec(0, len(L))

# Faz os graficos necessarios
def graficos(lwocorrencias, title):
    freqword = pd.DataFrame.from_records(lwocorrencias, columns=['word', 'count'])
    freqword.plot(kind='bar', x='word')
    plt.title(title)
    plt.show()


if __name__ == "__main__":

    #TODO organize into a presentable jupyter notebook
    dicfreq = geraFrequencias("AliceInWonderland.txt")
    print(dicfreq['w']['went'])
    print(dicfreq['w']['would'])
    lwocorrencias = ordenaFrequencias(dicfreq)
    graficos(lwocorrencias, "Alice in Wonderland")

    dicfreq = geraFrequencias("ThroughTheLookingGlass.txt")
    lwocorrencias = ordenaFrequencias(dicfreq)
    graficos(lwocorrencias, "Through the Looking Glass")

    dicfreq = geraFrequencias("WarAndPeace.txt")
    lwocorrencias = ordenaFrequencias(dicfreq)
    graficos(lwocorrencias, "War and Peace")
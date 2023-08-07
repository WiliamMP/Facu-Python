# --------------------------------------
#           ESTRUTURA DE DADOS
# --------------------------------------

# Lista

lista1 = []

lista2 = ['a','b','c']

# usando contrutor de tipo

lista3 = list()

linguagens = ["Python", "Java", "JavaScript", "Switft"]

print("Antes da listcomp = ", linguagens)

linguagens = [item.lower() for item in linguagens]
# cada indice ou item vai pra pequeno dentro da linguagens

print("\n Depois da lista comp = ", linguagens)


# map() e filter()

linguagens = 'Python Java Javascript C C#'.split()

nova_lista = map(lambda x: x.lower(), linguagens)
print(f"A nova lista é = {nova_lista}\n")
nova_lista = list(nova_lista)
print(f"Agora sim, a nova lista é = {nova_lista}")

# Range() & Filter()

numeros = list(range(0,21))

numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))
print(numeros_pares)

# Tuplas
# tupla é constante

tupla = ()

tupla2 = ('a','b','c')

# construtor de tipo
tupla3 = tuple()

# objetos do tipo set

set1 = set()
set1 = 1,2,3,5 # da pra usar comparação


# diferenças
# () tupla
# {} mapping
# [] list

# objetos do tipo mapping

dicionario = {}

dicionario2 = {'one':1, 'two':2, 'three':3} # tipo json

dicionario3 = dict()

# array NumPy
# usado para inteligência artificial

# import numpy

# matriz_1_1 = numpy.array([1,2,3]) # cria matriz 1 linha por 1 coluna
# matriz_2_2 = numpy.array([1,2], [3,4])

# print(type(matriz_1_1))
# print('\n matriz_1_1 = ', matriz_1_1)
# print('\n matriz_2_2 = ', matriz_2_2)

# ----------------------------------------
#           ALGORITMOS DE BUSCA
# ----------------------------------------

# busca linear ( ou busca sequencial)

def executar_busca_linear(lista, valor):
    for elemento in lista:
        if valor == elemento:
            return True
        return False

vogais = 'aeiou'
resultado = vogais.index('e')
print(resultado)

# ENTENDA complexdidade
# quando com a mesma entrada usa menos recursos computacionais pra uma mesma saida

# Busca binária, acha um valor dividindo em dois e procurando na outra metade
# Busca menos complexa, ou com menos gastos computacionais

def executar_busca_binaria(lista, valor):
    minimo = 0
    maximo = len(lista) - 1

    while minimo <= maximo:
        # Encontra o elemento que divide a lista ao meio
        meio = (minimo + maximo) // 2

        # Verifica se o valor procurado está a esquerda ou direita do valo central
        if valor < lista[meio]:
            maximo = meio -1
        elif valor > lista[meio]:
            minimo = meio + 1
        else:
            return True # se o valor for encontrado para aq 
    
    return False # se chegar ate aqui o valor n existe

# Algoritmos de ordenação
# estudar alguns algoritmos de ordenação, existe um site para estudar esse tipo de ordenação
# Existem algoritmos mais rápidos que outros
# existem algoritmos build-in feitos pelo próprio python e já em sintaxe

# Funções build-in Python
# Sorted() & Sort()

lista = [10, 4, 1 , 15, -3]

lista_ordenada1 = sorted(lista)
lista_ordenada2 = lista.sort()

print('Lista = ', lista, '\n')

print('lista_ordenada1 = ', lista_ordenada1)
print('lista_ordenada2 = ', lista_ordenada2)

print('lista = ', lista)

# Ficar de olho porque isso aqui geralmente cai em provas ou trabalhos

lista = [7,4]

if lista[0] > lista[1]:
    aux = lista[1]
    lista[1] = lista[0]
    lista[0] = aux # auxiliar para armazenar valores 

print(lista)

lista = [5, -1]

# Selection Sort (Ordenação por seleção)

lista = [10, 9, 5 ,8 ,11 ,3]

def executar_selection_sort(lista):
    tamanhoLista = len(lista)

    for i in range(0, tamanhoLista):
        indexMenor = i

        for j in range(i+1, tamanhoLista):
            if lista[j] < lista[indexMenor]:
                indexMenor = j
            lista[i], lista[indexMenor] = lista[indexMenor], lista[i]
    return lista
    
print(executar_selection_sort(lista))

# Feito com VS Code








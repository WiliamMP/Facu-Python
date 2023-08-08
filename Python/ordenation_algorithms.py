'''
    Algoritmos de ordenação (Resumo)
    
    Algoritmos de ordenação são algoritmos feitos para poderem ser utilizados na hora de se fazer
    a organização de uma lista ou qualquer outra fonte que tenha uma sequência que pode ser decrescente
    ou acrescente. Estes algoritmos variam desde extremamente compelxos, com demandas altas de recursos computacionais
    até rotinas simples capazes de, com uma mesma entrada de dados, fazerem de maneira mais eficiente e com menos recursos.

'''
# Selection Sort (Ordenação por comparação)
'''
    Selection Sort é o metodo mais comum dentre todos os algoritmos de ordenação, se você pegar uma pessoa que não possui conhecimento em ordenação
    muito possívelmente esta pessoa irá fazer um selection sort, pois é um metodo simples de organização. É consistido em pegar toda a lista e buscar
    pelo menor númerp possível e coloca-lo em primeiro, incrementar um no indice e repetir a rotina sucessivamente até organizar a mesma.
'''

def executar_selection_sort(lista): # !
    ListaTamanho = len(lista)

    for i in range(0, ListaTamanho):
        mIndice = i

        for j in range(i+1, ListaTamanho):

            if lista[j] < lista[mIndice]:
                mIndice = j
            lista[i], lista[mIndice] = lista[mIndice], lista[i]
    return lista

# Bubble Sort

# Insertion Sort

# Merge Sort

# Quick Sort

# Heap Sort

# Couting Sort

# Radix Sort

# Bucket Sort

# ============================================================================================================================================
# Chamada das funções

lista_geral = [1, 6, 9, 0, -5, 20, 99, 10, 44, 33, 22, 18, 15, 17, 2]

print(executar_selection_sort(lista_geral))
        


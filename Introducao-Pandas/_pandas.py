import pandas as pd

pd.Series(data=5)

lista_nomes = 'Howard Ian Peter Jonah Kellie'.split()

pd.Series(lista_nomes)

dados = {
    "nome1": "Howard",
    "nome2": "Ian",
    "nome3": "Peter",
    "nome4": "Jonah",
    "nome5": "Kellie",
}

print(pd.Series(dados))


serie_dados = pd.Series([10.2, -1, None, 15, 23.4])

print('Quantidade de linhas = ', serie_dados.shape) # retorna uma tupla com o número de linhas
print('Tipo de dados = ', serie_dados.dtypes) # Retona os tipos de dados, se for misto erá object
print('Os valore são únicos? ', serie_dados.is_unique) # Verifica se os valores unicos(sem duplicações)
print('Existem valores nulos? ', serie_dados.hasnans) # Retorna se possui valores nulos
print('Quanto valores existem? ', serie_dados.count()) # Retorna quantos valores exitem(exclui os nulos)
print('Qual o menor valor?', serie_dados.min()) # Extrai o menor valor da series( nesse caso precia ser do mesmo tipo)
print('Qual o maior valor?', serie_dados.max()) # Extrai o valor máximo, com a mesma condição do minimo 
print('Qual a média aritmética?', serie_dados.mean()) # Extrai a média aritmética de uma series numérica
print('Qual o desvio padrão?', serie_dados.std()) # Extrai o desvio padrão de uma das series númericas
print('Qual a mediana?', serie_dados.median()) # Extrai a mediana de uma das series numérica
print('\n Resumo: \n', serie_dados.describe()) # Exibe um resumo sobre o dados da series


teste = ["Wiliam","Teste","WWASSD"] # lista

pd.DataFrame(lista_nomes, columns=['nome'])

print(pd.DataFrame(lista_nomes, columns=['nome']))

dados_alunos = {
                'Nome': ['Wiliam', 'Carlos', 'Antonio'],
                'Idade': [19, 27, 22], 
                'Disciplina': ['Engenheiro', 'Matemática', 'Inglês']
               } # dicionario

df = pd.DataFrame.from_dict(dados_alunos)
print(df)
print('Somente o nome dos alunos')
print(df.Nome)


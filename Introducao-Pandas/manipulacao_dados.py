import pandas as pd
from datetime import date
from datetime import datetime as dt


lista_nomes = 'Howard Ian Peter Jonah Kellie'.split()

dfs = pd.DataFrame(lista_nomes, columns=['nome'])

print(pd.DataFrame(lista_nomes, columns=['nome']))

data_extracao = date.today()
dfs['data_extracao'] = data_extracao
dfs['data_extracao'] = dfs['data_extracao'].astype('datetime64[ns]')


dfs.sort_values(by='data_extracao', ascending=False, inplace=True)
print(dfs.info())
dfs.head()


##################################

dfs = pd.DataFrame(lista_nomes, columns=['nome'])
dfs['idade'] = 30
# tenho que ver o substituo para o dfs.append por conta que removeram essa feature ¯\_(ツ)_/¯

print(dfs.loc[(dfs['idade'] < 30)])
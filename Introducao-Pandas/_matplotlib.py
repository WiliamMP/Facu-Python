#%%
# import matplotlib.pyplot as plt
from matplotlib import pyplot as plt
import random
import numpy as np
import seaborn as sns

# usando random e matlibplot
dados1 = random.sample(range(100), k=20)
dados2 = random.sample(range(100), k=20)

plt.plot(dados1, dados2) # gerando com valores númericos

# usando numpy e matlibplot
x = np.linspace(0, 20, 100)
plt.plot(x, np.sin(x))
plt.show()

df = sns.load_dataset('titanic')
sns.countplot(x=df['class'])

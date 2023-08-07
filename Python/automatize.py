from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
# Configurações do chromedriver para poder manipular o chrome em ambiente de experimental 
service = Service(executable_path='./chromedriver.exe')

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=service,options=options)

# abrindo o site tendo em vista o protocolo https
driver.get('https://www.jotform.com/build/232174382825660#preview')

# Pegando os campos do HTML
Nome        = driver.find_element(By.XPATH, '/html/body/form/div/ul[1]/li[2]/div/div/span[1]/input')
Sobrenome   = driver.find_element(By.XPATH, '/html/body/form/div/ul[1]/li[2]/div/div/span[2]/input')
Data_Nasc   = driver.find_element(By.XPATH, '/html/body/form/div/ul[1]/li[3]/div/div/span/input')
Email       = driver.find_element(By.XPATH, '/html/body/form/div/ul[1]/li[4]/div/span/input')
Idade       = driver.find_element(By.XPATH, '/html/body/form/div/ul[1]/li[6]/div/input')
Altura      = driver.find_element(By.XPATH, '/html/body/form/div/ul[1]/li[7]/div/input')
Profissao   = driver.find_element(By.XPATH, '/html/body/form/div/ul[1]/li[8]/div/input')

# entrada de valores pelo usuário
Entrada_Nome = input("Insira seu nome: \n")
Entrada_Sobrenome = input("Insira seu sobrenome: \n")
Entrada_Data_Nasc = input("Insira sua data de nascimento(08082008): \n")
Entrada_Email = input("Insira seu email pessoal: \n")
Entrada_Sexo = input("Insira seu sexo(f or m): \n")
Entrada_Idade = input("Insira sua idade: \n")
Entrada_Altura = input("Insira sua altura: \n")
Entrada_Profissao = input("Insira sua profissao: \n")

# atribuindo infos para os devidos campos informados anteriormente
Nome.send_keys(Entrada_Nome)
Sobrenome.send_keys(Entrada_Sobrenome)
Data_Nasc.send_keys(Entrada_Data_Nasc)
Email.send_keys(Entrada_Email)

if Entrada_Sexo == 'f':
    Sexo = driver.find_element(By.XPATH, '/html/body/form/div/ul[1]/li[5]/div/div/span[1]/label')
else:
    Sexo = driver.find_element(By.XPATH, '/html/body/form/div/ul[1]/li[5]/div/div/span[2]/label') 

Sexo.click()

Idade.send_keys(Entrada_Idade)
Altura.send_keys(Entrada_Altura)
Profissao.send_keys(Entrada_Profissao)


time.sleep(5)
# conclusão do form
Nome.submit()
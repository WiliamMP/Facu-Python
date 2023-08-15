# OO - Orientação a objeto

class PrimeiraClasse:
    
    def imprimir_mensagem(self, nome): # Criando o método
        print(f"Olá {nome}, seja bem vindo!")
        objeto1 = PrimeiraClasse() # instanciando objeto do tipo primeira classe
        objeto1.imprimir_mensagem('Wiliam') # Invocando o método

# construtor de classe __init__()

class Televisao:
    def __init__(self):
        self.volume = 10
    def aumentar_volume(self):
        self.volume += 1
    def diminuir_volume(self):
        self.volume -= 1

tv = Televisao()
print("Volume ao ligar a tv = ", tv.volume)
tv.aumentar_volume()
print("Volume atual = ", tv.volume)


# Modificadores de acesso
# - public, 
# - private, 
# - protected
# Python n tem, por isso usa-se '_' antes do nome

class contaCorrente:
    def __init__(self):
        self._saldo = None
    def depositar(self, valor):
        self._saldo += valor
    def consultar_valor(self):
        return self._saldo

class Pessoa:
    def __init__(self):
        self.cpf = None
        self.nome = None
        self.endereco = None

class Funcionario(Pessoa):
    def __init__(self):
        self.matricula = None
        self_salario = None
    def bater_ponto(self):
        # Código aqui
        pass
    def fazer_login(self):
        # Código aqui
        pass

f1 = Funcionario()
f1.nome = "Funcionário A"
print(f1.nome)

# Métodos mágicos

print(dir(Pessoa()))

# Observe na saída desse trecho de código os Métodos mágicos

#################################################

import sqlite3

ddl_create = """
CREATE TABLE fornecedor (
    id_fornecedor INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nome_fornecedor TEXT NOT NULL,
    cnpj VARCHAR(18) NOT NULL,
    cidade TEXT,
    estado VARCHAR(2) NOT NULL,
    cep VARCHAR(9) NOT NULL,
    data_cadastro DATE NOT NULL

);
 """

conn = sqlite3.connect('aulaDB.db')
cursor = conn.cursor()
cursor.execute(ddl_create)
print(type(cursor))
print("tabela criada com sucesso!")

# IH ENTREI NO CRUD
# SQLITE USA READ NO LUGAR DO SELECT









                
        
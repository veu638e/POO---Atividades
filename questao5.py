#Conferindo se a senha está correta ou não

class usuario: 
    def __init__(self, nome, senha):
        self.nome = nome
        self.senha = senha


    def check_password (self, senha_digitada):
        if self.senha == senha_digitada:
            print("Bem Vindo(a)!")
        else:
            print("Senha incorreta")

Bianca = usuario("Bianca", "12345") #Criando um objeto cadastrado
senha_digitada = input("Digite a sua senha:")
Bianca.check_password(senha_digitada)


        
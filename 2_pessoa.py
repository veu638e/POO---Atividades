"""Criando a classe pessoa"""

class pessoa:
    #nome, idade, peso, altura
    def __init__(self, nome,idade, peso, altura): #dentro dos parenteses ficam os parametros, que são os valores que o uuario ira me fornecer;
        self.nome = nome #self.nome é o atributo que vai armazenar o parametro que o usuario forneceu;
        self.idade = idade
        self.peso = peso
        self.altura = altura

"""Criando os objetos da classe pessoa"""

pessoa1 = pessoa("Maria Luiza", 17, 70, 1.71)
pessoa2 = pessoa("Vitor", 17, 65, 1.80)
pessoa3 = pessoa("Fernanda", 23, 80, 1.65)

"""Imprimindo atributos dos meus objetos"""

#print(f" O nome da primeira pessoa cadastrada é: {pessoa1.nome}.")
#print(f" O nome da segunda pessoa cadastrada é: {pessoa2.nome}.")
#print(f" O nome da terceira pessoa cadastrada é: {pessoa3.nome}.")

"""Imprimindo todos os atributos do meu objeto"""

#1º forma de imprimir 
#print(vars(pessoa1))

# Forma de identificar  os atributos de um objeto 
#print(dir(pessoa2))

#2º Forma de de imprimir
print(pessoa3.__dict__)
#3º Forma de imprimir
#for atributo, valor in vars (pessoa2).items():
    #print(atributo+":", valor)




class pessoa:
    #nome, idade, peso, altura
    def __init__(self, nome,idade, peso, altura): #dentro dos parenteses ficam os parametros, que são os valores que o usuario ira me fornecer;
        self.nome = nome #self.nome é o atributo que vai armazenar o parametro que o usuario forneceu;
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def apresentacao(self):
        print(f"O nome da pessoa consultada é {self.nome};\nA idade dele(a) é: {self.idade}")

    def fazer_niver(self): 
        self.idade += 1
        print(f"Feliz aniversário {self.nome}!!! Agora você tem {self.idade} anos!")

pessoa1 = pessoa("Maria Luiza", 17, 70, 1.71)
pessoa2 = pessoa("Vitor", 17, 65, 1.80)
pessoa3 = pessoa("Fernanda", 23, 80, 1.65)

"""Chamando o método apresentação"""

pessoa1.apresentacao()
pessoa1.fazer_niver()
#pessoa3.apresentacao()


#Método construtor - def e __init__
#Criação de um método que altere a titulação do professor

class professor:
    def __init__(self, nome, titulacao, disciplina, salario):
        self.nome = nome
        self.titulacao = titulacao
        self.disciplina = disciplina
        self.salario = salario 

    def editar_titulacao (self, nova_titulacao):
        self.titulacao = nova_titulacao

    def mostrar_tudo(self):
        print(f"Os dados do usúario são: {self.nome}, {self.titulacao}, {self.disciplina}, {self.salario}.")

professor1 = professor("Nome: Jamerson", "Titulação: Mestre", "Disciplina: Programação Orientada a Objetos", "Salário: R$10.000")

professor1.mostrar_tudo()
professor1.editar_titulacao("Doutor")
print("Titulação a+lterada para:")
professor1.mostrar_tudo()

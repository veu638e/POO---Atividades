'''class animal:
    def comer (self):
        print("O animal está comendo")
        
class cachorro(animal):
    pass 

pet = cachorro()
pet.comer()'''

class pessoa:
    def __init__(self, nome):
        self.nome = nome
    def apresentar(self):
        print("Meu nome é", self.nome)
        
class aluno(pessoa):
    def apresentar(self):
        super().apresentar()
        print("Sou uma aluna desta instituição.")

aluno1 = aluno("Maria")
aluno1.apresentar()

class pessoa:
    def __init__(self, nome):
        self.nome = nome
    
class aluno(pessoa):
    def __init__(self, nome, matricula):
        super().__init__(nome)
        self.matricula = matricula
        
aluno1 = aluno("João", "12345")
        
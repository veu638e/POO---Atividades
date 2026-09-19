class aluno:
    def _init_(self, nome, matricula, nota1, nota2, nota3, nota4, nota5):
        self.nome = nome
        self.matricula = matricula
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
        self.nota4 = nota4
        self.nota5 = nota5

aluno1 = aluno("Marcelo", 1, 8, 7.5, 9, 8, 9)
aluno2 = aluno("Mariana", 2, 5, 6.5, 6, 7, 7.5)
aluno3 = aluno("Carla", 3, 10, 10, 9.8, 8.9, 8)

print(aluno1.__dict__)




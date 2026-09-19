class livro:
    def _init_(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

    def editar_titulo (self, novo_titulo):
        self.titulo = novo_titulo

    def mostrar_tudo(self):
        print("O nome do título do livro é: {self.titulo}; \n O nome do autor é: {self.autor}; \n O ano é:{self.ano}.")
        print("--------------------------------------------------------")

livro1 = livro("Casmurro", "Machado de Assis", 1899)
#Criando o objeto

livro1.mostrar_tudo() #pedido para o método ser executado
livro1.editar_titulo("Dom Casmurro")
livro1.mostrar_tudo()

    


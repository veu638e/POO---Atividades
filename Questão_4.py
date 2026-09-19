usuario = input("Digite o nome de usuário: ")
senha = input("Digite uma senha: ")

while senha==usuario:
    print("Erro! A senha não pode ser igual ao número de usuário!")
    print("----------------------")
    usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")

print("Cadastro realizado com sucesso!")
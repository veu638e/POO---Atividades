estudante = input("Digite o nome do estudante: ")
soma = 0
notas = []

for i in range(4):
    n = float(input(f"Digite a {i+1}º nota: "))
    notas.append(n)
    soma = soma+n
media = soma/4

print("\nBoletin de ", estudante)
print("------------------------")

for i in notas:
    print(i)

print("------------------------")
print(f"A soma das notas de {estudante} é: {soma:.1f}")
print(f"A média das notas de {estudante} é {media:.1f}")
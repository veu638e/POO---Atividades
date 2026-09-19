# usando listas, faça um programa que leia um vetor de 5 número inteiros e mostre-os.
#roda 5 vezes para o usuario digitar os 5 números
lista = []
for i in range(5):
    n = int(input(f"Digite o {i+1}º número: "))
    lista.append(n)

# exige cada item da lista
for i in lista:
    print(i)


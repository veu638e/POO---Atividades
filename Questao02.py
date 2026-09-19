lista = []

for i in range(5):
    n = int(input(f"Digite o {i+1}º número:"))

print("Lista atual:", lista)
lista.reverse()
print("Nova Lista:", lista)
"""Questão sobre substituição de item na lista"""

escala = ["João", "Mesquita", "Vitor", "Bruno", "Layla"]

print("Escala atual:", escala)

indice = int(input("Digite o número do funcionário que será substituído: "))

novo_func = input("Digite o nome do funcioário: ")

escala [indice-1] = novo_func

print("Nova escala", escala)


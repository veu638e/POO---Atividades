'''compras = ["arroz", "feijão", "leite", "pão", "ovos"] #lista é uma estrutura de dados. Sempre começa pelo indice 0.
#print(compras)

#as ações nas listas são realizadas através de métodos.
list = ["Maçã", "banana", "Mamão"]
#print(list)

#print(list[0]) serve para determinar qual item eu quero que apareça na tela.

#print(len(list)) # serve para ver quantos elementos tem na lista.

list.append('Laranja') #adiciona mais um elemento ao final da lista.
#print(list)

list.insert(0, 'Caqui') #insere um novo item na lista em qualquer posição desejada, o 0 indica que o elemnto foi inserido na posição 0.
print("Lista após o uso do insert: ", list)

list.insert(3, 'Uva')
print("Lista após a adição da uva: ", list)

list.remove("Caqui") #remove um item da lista através do nome.
print(list)

print(list.pop(2)) #remove um item através da posição.
print(list)'''

numeros = [1, 2, 3, 4, 5, 6]
print(numeros)

#1º forma de inserir uma valor:
numeros.insert(1,0) #apenas insere um valor sem substituir ninguém.
print(numeros)

#2º forma de inserir um valor:

numeros[1] = 50 #insere um valor no lugar do outro o substituindo.
print(numeros)

usuario1 = ["João", "000.000.000-00", "14/03/2008"]
print(usuario1)

usuario1[0] = "João Pereira" 
print(usuario1)

usuario1[0] = "Lucas Pereira"
print(usuario1)

usuario1[2] = "15/04/2007"
print(usuario1)

usuario1.append("19 anos")
print(usuario1)

print(len(usuario1))

'''if "Lucas Pereira" in usuario1:   # verifica se um item existe na lista
    usuario1.remove("Lucas Pereira") # caso o item citado acima exista o remove removerá o item da lista
    print(usuario1)'''

usuario1.clear() # Apaga a lista.
print(usuario1)






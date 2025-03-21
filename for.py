print("for utilizando lista")
lista = [1, 2, 3, 4, 5]
for elemento in lista:
    print (elemento)
print("for utilizando tupla")
tupla = (1, 2, 3, 4, 5)
for elemento in tupla:
    print(elemento)

pessoa = {"nome": "Anderson", "idade": "21", "cidade": "Recife"}
print("for utilizando dicionario - chaves")
for  chave in pessoa.keys():
    print(chave)

for valor in pessoa.values():
    print(valor) 

for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")

# range(): intervalo numerico 
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("utilizando a funcao range()")
for numero in range(5):
    print("numero:",  numero)

print("utilizando a funcao range() com len()")
lista = [1, 2, 3, 4, 5]
print(lista)
for indice in range(0, len(lista)):
   
    if indice == 3:
        lista[indice] = 5
    else:
        lista[indice] = 0
print(lista)

# enumerate()
lista_enumerate = ["a", "b", "c"]
for indice, valor in enumerate(lista_enumerate):
    print(f"{indice}: {valor}")
    if indice == 1:
        print("indice 1")

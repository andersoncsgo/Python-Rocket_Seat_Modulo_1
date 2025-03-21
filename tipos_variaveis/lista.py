# Declaracao

minha_lista = [1, 2, 3, 4, 5, 6, 7, 8, 112]

# Exibindo a lista
print("minha lista de exemplo:", minha_lista)

# Exibindo a lista
#minha_lista[0] = "python"
print("minha lista de exemplo:", minha_lista)

print("minha_lista[0]:", minha_lista[0])
print("minha_lista[5]:", minha_lista[5])
print("minha_lista[1:7]:", minha_lista[1:7]) #minha_lista[1:7], . minha_lista[1:2], .... minha_lista[6]
print("minha_lista[:6]:", minha_lista[:6])
print("minha_lista[2:]:", minha_lista[2:])


# Metodos de Lista

# Metodo append(): Adiciona um elemento ao final da lista

minha_lista.append(6)
print("apos append(6):", minha_lista)


# Metodo index
indice = minha_lista.index(6)
print("indice do elemento 6:", indice)

# Metodo insert: insere um elemento ao final da lista

minha_lista.insert(2, 10)
print("apos o insert(2, 10):", minha_lista)

# Metodo pop
elemento_devido = minha_lista.pop(3)
print("elemento removido:", elemento_devido)
print("apos pop(3):", minha_lista)

# Metodo remove
minha_lista.remove(True)
print("apos remove(True):", minha_lista)

# Metodo sort

minha_lista.sort()
print("apos o sort()", minha_lista)


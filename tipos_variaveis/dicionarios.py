# Criando um dicionario de exemplo
pessoa = {"nome": "Joao", "idade": 30, "cidade": "Sao Paulo"}

# Exibindo o dicionario
print("Meu dicionario de exemplo: ", pessoa)

# Acessando valores por chave
print("Nome:", pessoa["nome"])
print("Idade:", pessoa["idade"])
print("Cidade:", pessoa["cidade"])
pessoa["sobrenome"] = "Silva"
print("Sobrenome:", pessoa["sobrenome"])

pessoa["idade"] = 31
print("Idade atualizada:", pessoa["idade"])

# Removendo um par chave-valor
del pessoa["sobrenome"]
print("Meu dicionario de exemplo: ", pessoa)

# Metodos: keys(), values(), items()
chaves = list(pessoa.keys())
print("chaves do dicionario", chaves)
print("Primeira chave:", chaves[0])

# Metodos Values
valores = list(pessoa.values())
print("Valores dos dicionariso:", valores)
print("Primeiro valor:", valores[0])

# Metodos items
itens = list(pessoa.items())
print("Pares chave-valor do dicionarios:", itens)
print("Primeira chave-valor %s = %s " % (itens[0][0],itens[0][1]))
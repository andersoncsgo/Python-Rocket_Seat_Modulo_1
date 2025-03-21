# If,, elif e else

# Exemplo de if
idade = int(input("Quantos anos voce tem?"))
print("exemplo de comando if")

if idade >= 18:
    print("voce e maior de idade")
elif idade >= 12:
    print("voce e um adolescente")
else:
    print("voce e menor de idade")

mensgaem = "Pode tirar a carteira de habilitacao" if idade >= 18 else "voce nao pode tirar a carteira de habilitacao"
print(mensgaem)
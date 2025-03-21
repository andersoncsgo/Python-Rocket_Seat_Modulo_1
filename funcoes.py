# exemplo

def saudacao(nome):
    print(f"Ola, {nome}!")


print("\n chamando a funcao saudacao:")
saudacao("Alice")
saudacao("Bob")

# funcao com retorno
def quadrado(numero):
    resultado = numero ** 2
    return resultado

print("\nchamando funcao quadrado")

resultado_quadrado = quadrado(5)
print("resultado da funcao quadrado", resultado_quadrado)

# funcao com multiplos parametros

def soma(numero1, numero2):
    resultado = numero1 + numero2
    return resultado

print("\nchamando a funcao soma:")
numero1 = 20
numero2 = 50
resultado_soma = soma(numero1, numero2)
print("A soma do numero %s e numero %s e %s" % (numero1, numero2, resultado_soma))

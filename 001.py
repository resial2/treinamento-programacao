
def somar (a,b):
    return a + b

def multiplicar (a,b):
    return a * b

n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))

print("1 - Somar\n3 - Multiplicar")

opc = int(input('Opção selecionada: '))

if(opc == 1):
    resultado = somar(n1,n2)

elif(opc == 3):
    resultado = multiplicar(n1,n2)

print("Resultado: " + str(resultado))


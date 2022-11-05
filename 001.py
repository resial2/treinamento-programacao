def somar(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def multiplicar(n1, n2):
    return n1 * n2


def div(n1, n2):
    return n1 / n2


n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))

print('''
[1] Somar
[2] Subtrair
[3] Multiplicar
[4] Dividir
''')

escl = int(input("Qual sua escolha: "))

if escl == 1:
    resl = somar(n1, n2)
elif escl == 2:
    resl = sub(n1, n2)
elif escl == 3:
    resl = multiplicar(n1, n2)
elif escl == 4:
    resl = div(n1, n2)
else:
    print("Caiu na casa do krl!!!! kskksksksksk")
    resl = 0

print(f"O resultado é: {resl}")

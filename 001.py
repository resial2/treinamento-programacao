def div(n1, n2):
    return n1 / n2


def sub(n1, n2):
    return n1 - n2


n1 = int
n2 = int
resl = int


escl = int(input("digite 2 para divisão e 4 para subtração: "))
if escl == 2:
    n1 = int(input("digite o primeiro numero: "))
    n2 = int(input("digite o segundo numero: "))
    print(div(n1, n2))
elif escl == 4:
    n1 = int(input("digite o primeiro numero: "))
    n2 = int(input("digite o segundo numero: "))
    print(sub(n1, n2))



print("generador de secuencias personalizado".title())

inicio = int(input("inicio de la secuencia ").title())
fin = int(input("fin de la secuencia").title())
salto = int(input("salto de numero en la secuencia").title())

for i in range(inicio, fin + 1, salto):

    print(i)
import random

intentos = 7
numero_secreto = random.randint(1, 100)
adivinado = False

while intentos > 0 and not adivinado:
    try:
        intento = int(input("Escriba el número: "))
    except ValueError:
        print("Debe escribir un número entero.")
        continue

    intentos -= 1

    if intento == numero_secreto:
        adivinado = True
    elif intento < numero_secreto:
        print("El número secreto es MAYOR")
    else:
        print("El número secreto es MENOR")

if adivinado:
    print(f"¡Felicidades, mi compa! ¡Adivinaste el número, era {numero_secreto}!")
else:
    print(f"Se te acabaron los intentos. El número secreto era {numero_secreto}. ¡A reintentar!")

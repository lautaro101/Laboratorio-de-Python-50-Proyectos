vocal = ["a", "e", "i", "o", "u"]

letra = input("Ingrese una letra: ")

len(letra)

while len(letra) != 1:
    print("Error: Debe ingresar exactamente un solo carácter.")

    letra = input("Ingrese una letra nuevamente: ").lower().strip()

    

if letra in vocal:
    print("Es una vocal")


else:
    print("Es una consonante u otro carácter")
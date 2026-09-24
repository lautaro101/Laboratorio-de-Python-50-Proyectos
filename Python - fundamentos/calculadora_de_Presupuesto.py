print("Bienvenido")
print()
sueldo = float(input("Ingrese su sueldo mensual: ".title()))

print("Ingrese 3 gastos fijos mensuales")

n_1 = input("nombre del 1mer gasto".title())
gasto1 = float(input("Gasto N°1: "))
n_2 = input("nombre del 2do gasto".title())
gasto2 = float(input("Gasto N°2: "))
n_3 = input("nombre del 3ser gasto".title())
gasto3 = float(input("Gasto N°3: "))
print()
gasto_total =gasto1+gasto2+gasto3
calculo = sueldo - gasto_total

print(f"ingreso ${sueldo}, se gasto ${gasto_total} y sobro {calculo}".title())
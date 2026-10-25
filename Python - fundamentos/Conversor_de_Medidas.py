PULGADA_A_MM = 25.4
PULGADA_A_CM = 2.54 

medida_pulgada = float(input("Ingrese la medida en pulgadas: ").strip())

milimetros = round(medida_pulgada * PULGADA_A_MM, 2)
centimeto = round(medida_pulgada * PULGADA_A_CM, 2)

print(f"Su equivalencia a milimetros es: {milimetros}")
print(f"Su equivalencia a centimetros es: {centimeto}")

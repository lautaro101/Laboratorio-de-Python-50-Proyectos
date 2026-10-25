PRECIO_BOLSA_CEMENTO = 8500

CantidadDeBolsas = int(input("ingrese La Cantidad De Bolsas: ").strip())

if CantidadDeBolsas > 100:
    total = CantidadDeBolsas * PRECIO_BOLSA_CEMENTO 

    descuento = total * 0.20

    print("Decuento Aplicado: 20%")

    precio_final = total - descuento

    print(f"El total seria: ${precio_final}")

    envio = input("desea el envio? (si/no): ")

    if envio == "si":
        elegir = input("provincia o capital: ")
        
        if elegir == "provincia":
            print("el envio a provincia cuesta $5000")
            total_del_total = precio_final + 5000

            print(f"total a pagar es ${total_del_total}")
        elif elegir == "capital":
            print("el envio a capital es gratis")

            print(f"total a pagar es ${precio_final}")

        else:
            print("elija una opcion")

    

elif 50 <= CantidadDeBolsas <= 100:
    total = CantidadDeBolsas * PRECIO_BOLSA_CEMENTO

    descuento = total * 0.10

    print("Decuento Aplicado: 10%")

    precio_final = total - descuento

    print(f"El total seria: ${precio_final}")

    envio = input("desea el envio? (si/no): ")
    
    if envio == "si":
        elegir = input("provincia o capital: ")
            
        if elegir == "provincia":
            print("el envio a provincia cuesta $5000")
            total_del_total = precio_final + 5000
    
            print(f"total a pagar es ${total_del_total}")
        elif elegir == "capital":
            print("el envio a capital es gratis")
    
            print(f"total a pagar es ${precio_final}")
    
        else:
            print("elija una opcion")

elif 0 < CantidadDeBolsas < 50:
    total = CantidadDeBolsas * PRECIO_BOLSA_CEMENTO
    print(f"El total seria: ${total}")

    envio = input("desea el envio? (si/no): ")
    
    if envio == "si":
        elegir = input("provincia o capital: ")
            
        if elegir == "provincia":
            print("el envio a provincia cuesta $5000")
            total_del_total = precio_final + 5000
    
            print(f"total a pagar es ${total_del_total}")
        elif elegir == "capital":
            print("el envio a capital es gratis")
    
            print(f"total a pagar es ${precio_final}")
    
        else:
            print("elija una opcion")

else:
    print("Ingrese una cantidad valida")

    

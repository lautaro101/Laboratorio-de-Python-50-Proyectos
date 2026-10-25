AGE = 18
KEY_SECRET = "python123"

Enter_age = int(input("Ingrese su edad: "))
Enter_Key = input("Ingrese la clave: ").lower().strip()

if Enter_age >= AGE:
    if Enter_Key == KEY_SECRET:
        print("Correct Password")
        print("Access Granted")

    else:
        print("Incorrect Password")

else:
    print("Access denied. Sos menor de edad".title())
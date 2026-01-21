import os

print("---- BIENVENIDO(A) AL CAJERO AUTOMATICO ----")

pin_secreto = 1234
saldo = 100000
nombre = "Nayib"
intentos = 0
es_usuario_valido = False 

while intentos < 3 and es_usuario_valido == False:
    entrada = int(input(f"Intento {intentos+1}/3 - Ingrese su PIN: "))

    if entrada == pin_secreto:
        print(f"\nBienvenido(a) {nombre}!")
        es_usuario_valido = True
    else:
        print("PIN Incorrecto")
        intentos = intentos + 1

if es_usuario_valido == True:
    opcion = ""

    while opcion != "4":
        print("\n" + "="*15)
        print(f"SALDO ACTUAL: ₡{saldo}")
        print("="*15)
        print("1. Consultar saldo")
        print("2. Retirar efectivo")
        print("3. Depositar fondos")
        print("4. Salir")

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            print(f">> Su saldo disponible es: ₡{saldo}")

        elif opcion == "2":
            print("Billetes disponibles: " \
            "\n₡20000" \
            "\n₡10000" \
            "\n₡5000" \
            "\n₡2000" \
            "\n₡1000")

            retiro = int(input("Ingrese un monto a retirar: "))

            if retiro <= 0:
                print("Error: El monto debe de ser mayor a cero.")
            elif retiro > saldo:
                print("Error: Fondos insuficientes")
            elif retiro % 1000 != 0:
                print("Error: Solo se permiten montos múltiplos de ₡1000")

            else:
                pendiente = retiro

                b20 = pendiente // 20000 # Cuantas veces cabe 20000 en el monto de retiro?
                pendiente = pendiente % 20000 # Cuanto me sobra del monto de retiro?

                b10 = pendiente // 10000 
                pendiente = pendiente % 10000 

                b5 = pendiente // 5000 
                pendiente = pendiente % 5000 

                b2 = pendiente // 2000 
                pendiente = pendiente % 2000 

                b1 = pendiente // 1000 
                pendiente = pendiente % 1000 

                saldo = saldo - retiro 

                print("\n--- RETIRO EXITOSO ---")

                if b20 > 0: print(f"{b20} billetes de ₡20000")
                if b10 > 0: print(f"{b10} billetes de ₡10000")
                if b5 > 0: print(f"{b5} billetes de ₡5000")
                if b2 > 0: print(f"{b2} billetes de ₡2000")
                if b1 > 0: print(f"{b1} billetes de ₡1000")
                print(f"Nuevo saldo: ₡{saldo}")
        
        elif opcion == "3":
            deposito = int(input("Ingrese el monto a depositar: "))
            if deposito > 0:
                saldo = saldo + deposito 
                print(f"Deposito realizado. Nuevo saldo {saldo}")
        
        elif opcion == "4":
            print("¡Gracias por usar nuestro cajero!")

else:
    print("\n ACCESO DENEGADO")
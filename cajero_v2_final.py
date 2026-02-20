print("---- BIENVENIDO(A) AL CAJERO AUTOMATICO ----")

PIN = 1234
saldo = 100000
nombre = "Nayib"
intentos = 0
usuario_valido = False
INTENTOS_MAX = 3

# Validación del PIN
while intentos < INTENTOS_MAX and not usuario_valido:
    try:
        entrada = int(input(f"Intento {intentos+1}/{INTENTOS_MAX} - Ingrese su PIN: "))
    except ValueError:
        print("Debe ingresar solo números.")
        continue

    if entrada == PIN:
        print(f"\nBienvenido(a) {nombre}!")
        usuario_valido = True
    else:
        print("PIN incorrecto")
        intentos += 1

# Menú principal
if usuario_valido:
    continuar = "s"

    while continuar.lower() == "s":
        opcion = ""

        while opcion != "4":
            print("\n" + "="*20)
            print("MENÚ DE TRANSACCIONES")
            print("="*20)
            print("1. Consultar saldo")
            print("2. Retirar efectivo")
            print("3. Depositar fondos")
            print("4. Volver")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                print(f"Su saldo disponible es: ₡{saldo}")

            elif opcion == "2":
                retiro = int(input("Ingrese el monto a retirar: "))

                if retiro <= 0:
                    print("El monto debe ser mayor a cero.")
                elif retiro > saldo:
                    print("Fondos insuficientes.")
                elif retiro % 1000 != 0:
                    print("Solo se permiten montos múltiplos de ₡1000.")
                else:
                    saldo -= retiro
                    print("Retiro realizado con éxito.")
                    print(f"Nuevo saldo: ₡{saldo}")

            elif opcion == "3":
                deposito = int(input("Ingrese el monto a depositar: "))
                if deposito > 0:
                    saldo += deposito
                    print(f"Depósito realizado. Nuevo saldo: ₡{saldo}")
                else:
                    print("Monto inválido.")

            elif opcion == "4":
                print("Regresando al menú principal...")

            else:
                print("Opción inválida.")

        continuar = input("\n¿Desea realizar otra transacción? (s/n): ")

    print("\nTransacción finalizada, gracias por confiar en nuestro banco.")

else:
    print("\nACCESO DENEGADO")

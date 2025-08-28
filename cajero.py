import os 

saldo = 100000
isActive = True

os.system("clear")



while isActive:
    
    print("Bienvenido al cajero automático")
    print("1. Consultar saldo")
    print("2. Depositar dinero")
    print("3. Retirar dinero")
    print("0. Salir")
    
    opcion = int(input("\nSeleccione una opción: "))
    
    match opcion:
        case 1:
            os.system("clear")
            print(f"\nSu saldo actual es: ${saldo}")
            input("\nPresiona Enter para continuar...")
            os.system("clear")
        case 2:
            os.system("clear")
            deposito = int(input("\nIngrese la cantidad a depositar: "))
            if deposito > 0:
                saldo += deposito
                print(f"\nDepósito exitoso. Su nuevo saldo es: ${saldo}")
                input("\nPresiona Enter para continuar...")
                os.system("clear")
            else:
                print("\nCantidad inválida. Intente de nuevo.")
                input("\nPresiona Enter para continuar...")
                os.system("clear")
        case 3:
            os.system("clear")
            retiro = int(input("\nIngrese la cantidad a retirar: "))
            saldo -= retiro
            if retiro > 0 and retiro <= saldo:
                print(f"\nRetiro exitoso. Su nuevo saldo es: ${saldo}")
                input("\nPresiona Enter para continuar...")
                os.system("clear")
            else:
                print("\nCantidad inválida o saldo insuficiente. Intente de nuevo.")
                input("\nPresiona Enter para continuar...")
                os.system("clear")
        case 0:
            os.system("clear")
            print("\nGracias por usar el cajero automatico")
            isActive = False
        case _:
            print("\nOpción inválida. Intente de nuevo.")
            input("\nPresiona Enter para continuar...")
            os.system("clear")
            
   
        
        

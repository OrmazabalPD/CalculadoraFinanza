from dicc_finance import create_account,find_account_by_name, add_transaction,get_account_balance

def main():


    global accounts, global_accounts_id
    accounts = []
    global_accounts_id = 0
    

    while True:
        print("Bienvenido a la calculadora")
        print("1. Crear Cuenta")
        print("2. Buscar cuenta por nombre")
        print("3. Agregar Transacion")
        print("4. Consultar saldo de la cuenta")
        print("5. consultar el saldo total")
        print("6. Mostrar todas las cuentas")
        print("7. Salir")
    # captura la opcion de entrada

        try: 
            option = int(input("Ingrese la opcion deseada: "))

        except ValueError:
            print("Por favor ingrese la opcion correcta")
            continue    

        if option == 1:
            name  = input("Ingrese el nombre de la cuenta: ")
            account_type = input("ingrese el tipo de cuenta: ")
            account_id = create_account(accounts, name, account_type)
            account_id == global_accounts_id.id
            print(f"La cuenta '{name}' creada con el id ")

        elif option == 2:
            name = input("ingrese el nombre de la cuenta:")
            account = find_account_by_name(accounts, name)

            if account:
                print(f"La cuenta {name} existe")

            else:
                print(f"La cuenta {name} no existe")

        elif option == 3:  
            name = input("Ingrese el nombre de la transaccion: ")
            description = input("Ingrese el monto de la transaccion: ")

            try:
                amount = float(input("Ingrese el monto de la transaccion: "))
                add_transaction(accounts, name, description, amount)
                print("Transaccion agregada.")

            except ValueError:
                print("Por favor, ingrese un monto valido.")

        elif option == 4:

            name = input("Ingrese el nombre de la cuenta cuyo saldod desea obtener")
            balance = get_account_balance(accounts, name)

            if balance is not None:
                print(f"Saldo de la cuenta '{name}': {balance}")

        elif option == 5:
            total_balance = get_account_balance(accounts)
            print(f"Saldo total de todas las cuentas: {total_balance}")                    

        elif option == 6:

            if accounts:
                print("\nCuentas:")
                for account in accounts:
                    print(account)

            else:
                print("\nNo hay cuentas reistradas.")

        elif option == 7:  
            print("Saliendo...")
            break

        else:
            print("Por favor, ingrese una opción válida.")              



if __name__  == "__main__":
    main()

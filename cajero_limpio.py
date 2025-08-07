# -*- coding: utf-8 -*-
import random #importamos la libreria random para generar numeros aleatorios

def solicitar_pin():
    """Solicita el PIN de 4 digitos al usuario"""
    while True:
        pin = input("Ingrese su PIN de 4 digitos: ") #ingresamos el PIN de 4 digitos
        if len(pin) == 4 and pin.isdigit(): #si el PIN tiene 4 digitos y es numerico, mostramos un mensaje de acceso autorizado
            print("PIN valido. Acceso autorizado.") #mostramos un mensaje de acceso autorizado
            return True
        else:
            print("Error: El PIN debe tener exactamente 4 digitos numericos.")

def mostrar_menu():
    """Muestra el menu de operaciones disponibles"""
    print("\n" + "="*40) #mostramos el menu de operaciones disponibles
    print("        CAJERO AUTOMATICO") #mostramos el menu de operaciones disponibles
    print("="*40) #mostramos el menu de operaciones disponibles
    print("Que operacion desea realizar?") #mostramos el menu de operaciones disponibles
    print("1. Consulta de saldo") #mostramos el menu de operaciones disponibles
    print("2. Extraccion de dinero") #mostramos el menu de operaciones disponibles
    print("3. Salir") #mostramos el menu de operaciones disponibles
    print("="*40) #mostramos el menu de operaciones disponibles

def consultar_saldo(saldo):
    """Muestra el saldo disponible"""
    print(f"\nSu saldo disponible es: ${saldo:,}") #mostramos el saldo disponible
    print("="*40) #mostramos el menu de operaciones disponibles

def extraer_dinero(saldo):
    """Permite extraer dinero del cajero"""
    print(f"\nSaldo disponible: ${saldo:,}") #mostramos el saldo disponible
    
    try:
        monto = int(input("Ingrese el monto a retirar (multiplo de 100): ")) #ingresamos el monto a retirar
        
        # Validaciones
        if monto % 100 != 0:
            print("Error: El monto debe ser multiplo de 100.") #mostramos un error
            return saldo
        elif monto > saldo:
            print("Error: Saldo insuficiente.") #mostramos un error
            return saldo
        elif monto <= 0:
            print("Error: El monto debe ser mayor a 0.") #mostramos un error
            return saldo
        else:
            # Calculo de billetes
            billetes_1000 = monto // 1000 #calculamos los billetes de 1000
            restante = monto % 1000 #calculamos el resto

            billetes_500 = restante // 500 #calculamos los billetes de 500
            restante = restante % 500 #calculamos el resto

            billetes_100 = restante // 100 #calculamos los billetes de 100

            # Mostrar resultados
            print("\n" + "="*40) #mostramos el menu de operaciones disponibles
            print("        BILLETES ENTREGADOS") #mostramos el menu de operaciones disponibles
            print("="*40) #mostramos el menu de operaciones disponibles
            if billetes_1000 > 0:
                print(f"- Billetes de $1,000: {billetes_1000}") #mostramos los billetes de 1000
            if billetes_500 > 0:
                print(f"- Billetes de $500: {billetes_500}") #mostramos los billetes de 500
            if billetes_100 > 0:
                print(f"- Billetes de $100: {billetes_100}") #mostramos los billetes de 100
            
            nuevo_saldo = saldo - monto #calculamos el nuevo saldo
            print(f"\nMonto retirado: ${monto:,}") #mostramos el monto retirado
            print(f"Nuevo saldo: ${nuevo_saldo:,}") #mostramos el nuevo saldo
            print("="*40) #mostramos el menu de operaciones disponibles
            return nuevo_saldo

    except ValueError:
        print("Error: Debe ingresar un numero entero.") #mostramos un error
        return saldo

def main():
    """Funcion principal del cajero automatico"""
    print("="*50) #mostramos el menu de operaciones disponibles
    print("    BIENVENIDO AL CAJERO AUTOMATICO") #mostramos el menu de operaciones disponibles
    print("="*50) #mostramos el menu de operaciones disponibles
    
    # Simular insercion de tarjeta
    print("Tarjeta insertada correctamente.") #mostramos un mensaje de tarjeta insertada correctamente
    
    # Solicitar PIN
    if not solicitar_pin():
        return
    
    # Generar saldo aleatorio
    saldo_disponible = random.randint(90, 50000) #generamos un saldo aleatorio entre 90 y 50000
    
    while True:
        mostrar_menu() #mostramos el menu de operaciones disponibles
        
        try:
            opcion = int(input("Seleccione una opcion (1-3): ")) #ingresamos la opcion
            
            if opcion == 1:
                consultar_saldo(saldo_disponible) #mostramos el saldo disponible
            elif opcion == 2:
                saldo_disponible = extraer_dinero(saldo_disponible) #mostramos el saldo disponible
            elif opcion == 3:
                print("\nGracias por usar nuestro cajero automatico.") #mostramos un mensaje de gracias por usar nuestro cajero automatico
                print("Retire su tarjeta.") #mostramos un mensaje de retire su tarjeta
                break
            else:
                print("Error: Opcion no valida. Seleccione 1, 2 o 3.") #mostramos un error
                
        except ValueError:
            print("Error: Debe ingresar un numero valido.") #mostramos un error

if __name__ == "__main__":
    main()

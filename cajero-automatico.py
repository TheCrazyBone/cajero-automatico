import random

# Saldo aleatorio entre 90 y 50000
saldo_disponible = random.randint(90, 50000)
print(f"Saldo disponible en la cuenta: ${saldo_disponible}")

# Ingreso del monto a retirar
try:
    monto = int(input("Ingrese el monto a retirar (múltiplo de 100): "))
    
    # Validaciones
    if monto % 100 != 0:
        print("Error: El monto debe ser múltiplo de 100.")
    elif monto > saldo_disponible:
        print("Error: Saldo insuficiente.")
    else:
        # Cálculo de billetes
        billetes_1000 = monto // 1000
        restante = monto % 1000

        billetes_500 = restante // 500
        restante = restante % 500

        billetes_100 = restante // 100

        # Mostrar resultados
        print("Billetes entregados:")
        if billetes_1000 > 0:
            print(f"- Billetes de $1000: {billetes_1000}")
        if billetes_500 > 0:
            print(f"- Billetes de $500: {billetes_500}")
        if billetes_100 > 0:
            print(f"- Billetes de $100: {billetes_100}")
        if monto == 0:
            print("No se entregó dinero.")

except ValueError:
    print("Error: Debe ingresar un número entero.")
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n == + factorial(n-1)


def suma_Naturales(n):
    if n == 0:
        return 0
    else:
        return n == + suma_Naturales(n-1)

def calcular_nfibo(n)
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return calcular_nfibo()


while True:
    print("1. Calcular el factorial.")
    print("2. Suma de los primeros numeros.")
    print("3. Calcular el n-ésimo.")
    print("4. Contar las veces de una letra.")
    print("5. Invertir una cadena de texto.")
    print("6. Calcular la potencia de un número.")
    print("7. Salir del programa....")
       opcion = 0
       match opcion:
            case 1:
                numero = int(input("Ingrese un número: "))
                print(f"El factorial de {numero} es {factorial(numero)}")







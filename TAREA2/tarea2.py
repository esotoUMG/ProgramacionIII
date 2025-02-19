import os

def convertir_a_binario(numero): #CONVERTIR A BINARIO DESDE DECIMAL
    if numero < 0:
        return "Ingrese un número entero positivo"
    if numero == 0:
        return "0"
    return convertir_a_binario(numero // 2) + str(numero % 2)

def contar_digitos(numero): #CONTAR LOS DIGITOS
    numero = abs(numero)  #PARA QUE FUNCIONE CON NUMERO NEGATIVOS, HE AGREGADO EL ABS
    if numero == 0:
        return 0
    return 1 + contar_digitos(numero // 10)

def raiz_cuadrada_entera(numero): #RAIZ CUADRADA ENTERA
    if numero < 0:
        return "Ingrese un número positivo"
    return int(numero ** 0.5)

def convertir_a_decimal(romano): #CONVERSOR DE ROMANO A DECIMAL
    valores = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
        'D': 500, 'M': 1000
    }
    total = 0
    prev = 0
    for letra in reversed(romano):
        valor = valores.get(letra, 0)
        if valor < prev:
            total -= valor
        else:
            total += valor
        prev = valor
    return total

def suma_numeros_enteros(numero): #SUMA DE NUMEROS ENTEROS
    if numero < 0:
        return "Ingrese un número positivo"
    if numero == 0:
        return 0
    return numero + suma_numeros_enteros(numero - 1)

@staticmethod
def limpiarconsola():
    os.system("cls" if os.name=="nt" else "clear")

@staticmethod
def pausar():
    input("\nPresiona enter para continuar...")

#INICIA EL MENU
while True:
    limpiarconsola()
    print("----MENU DE OPCIONES----")
    print("1. Convertir a Binario")
    print("2. Contar dígitos")
    print("3. Raíz cuadrada entera")
    print("4. Convertir número romano a decimal")
    print("5. Suma de números enteros")
    print("6. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        numero = int(input("Ingrese un número entero: "))
        print(f"El número {numero} en binario es {convertir_a_binario(numero)}")
        pausar()
    elif opcion == '2':
        numero = int(input("Ingrese un número entero: "))
        print(f"El número {numero} tiene {contar_digitos(numero)} dígitos")
        pausar()
    elif opcion == '3':
        numero = int(input("Ingrese el número al cual quiere sacarle la raíz cuadrada entera: "))
        print(f"La raíz cuadrada entera de {numero} es {raiz_cuadrada_entera(numero)}")
        pausar()
    elif opcion == '4':
        romano = input("Ingrese el número romano que quiere convertir a decimal: ").upper()
        print(f"El número romano {romano} en decimal es {convertir_a_decimal(romano)}")
        pausar()
    elif opcion == '5':
        numero = int(input("Ingrese el número entero que quiere sumar: "))
        print(f"La suma de los números enteros es {suma_numeros_enteros(numero)}")
        pausar()
    elif opcion == '6':
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida")
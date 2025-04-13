"""
Ejercicio 1: Crear un programa que determine el valor máximo entre tres números. ¿Cuántas funciones y/o procedimientos son
necesarios para resolver este problema? ¿Cuántos parámetros?
"""

def encontrar_maximo(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

maximo = encontrar_maximo(num1, num2, num3)
print("El valor máximo es:", maximo)

"""
Ejercicio 2:Crear un programa que determine el valor máximo entre 10 números utilizando las funciones/procedimientos del
ejercicio anterior.
"""

def encontrar_maximo(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

numeros = []
for i in range(10):
    num = int(input(f"Ingrese el número {i+1}: "))
    numeros.append(num)

maximo_actual = numeros[0]

for i in range(1, 10):
    maximo_actual = encontrar_maximo(maximo_actual, numeros[i], numeros[i])

print("El valor máximo es:", maximo_actual)

"""
Ejercicio 3: Crear un programa que:
a) cargue dos vectores A y B, con N y M números enteros respectivamente
b) calcular la suma de los números cargados en cada vector.
c) si N y M son iguales, realice la suma de los vectores. Mostrar el vector resultante
¿Cuántas funciones y/o procedimientos son necesarios para resolver este problema?
"""

def cargar_vector(longitud):
    vector = []
    for i in range(longitud):
        num = int(input(f"Ingrese el elemento {i+1}: "))
        vector.append(num)
    return vector

def sumar_elementos(vector):
    suma = 0
    for elemento in vector:
        suma += elemento
    return suma

def sumar_vectores(vector_a, vector_b):
    resultado = []
    for i in range(len(vector_a)):
        resultado.append(vector_a[i] + vector_b[i])
    return resultado

n = int(input("Ingrese la cantidad de elementos para el vector A: "))
print("Cargando vector A:")
vector_a = cargar_vector(n)

m = int(input("Ingrese la cantidad de elementos para el vector B: "))
print("Cargando vector B:")
vector_b = cargar_vector(m)

suma_a = sumar_elementos(vector_a)
suma_b = sumar_elementos(vector_b)

print("Suma de elementos del vector A:", suma_a)
print("Suma de elementos del vector B:", suma_b)

if n == m:
    vector_resultado = sumar_vectores(vector_a, vector_b)
    print("Vector resultante de la suma:", vector_resultado)
else:
    print("Los vectores tienen distinta longitud, no se puede realizar la suma.")


"""
Ejercicio 4: Crear un programa que cargue una o más oraciones y luego indique la suma total de vocales y consonantes:
- Crear dos funciones, una para contar las vocales y otra para contar las consonantes que tiene cada palabra.
- Cada función tomará como parámetro una palabra.
- En el programa principal mostrar la cantidad total de vocales y la cantidad total de consonantes en el texto de
entrada.
"""

def contar_vocales(palabra):
    contador = 0
    for letra in palabra.lower():
        if letra in "aeiouáéíóúü":
            contador += 1
    return contador

def contar_consonantes(palabra):
    contador = 0
    for letra in palabra.lower():
        if letra.isalpha() and letra not in "aeiouáéíóúü":
            contador += 1
    return contador

texto = input("Ingrese una o más oraciones: ")
palabras = texto.split()

total_vocales = 0
total_consonantes = 0

for palabra in palabras:
    total_vocales += contar_vocales(palabra)
    total_consonantes += contar_consonantes(palabra)

print("Total de vocales:", total_vocales)
print("Total de consonantes:", total_consonantes)

"""
Ejercicio 5: Crear un programa que contenga un menú con las siguientes opciones:
- Calcular la potencia K de un número X.
- Obtener la cantidad de dígitos de un número X.
- Determinar si un número es capicúa.
Implementar funciones para cada opción del menú.
"""

def calcular_potencia(base, exponente):
    return base ** exponente

def contar_digitos(numero):
    return len(str(abs(numero)))

def es_capicua(numero):
    numero_str = str(abs(numero))
    return numero_str == numero_str[::-1]

while True:
    print("\nMenú de opciones:")
    print("1. Calcular la potencia K de un número X")
    print("2. Obtener la cantidad de dígitos de un número X")
    print("3. Determinar si un número es capicúa")
    print("4. Salir")
    
    opcion = input("Seleccione una opción (1-4): ")
    
    if opcion == "1":
        x = float(input("Ingrese el número base (X): "))
        k = int(input("Ingrese el exponente (K): "))
        resultado = calcular_potencia(x, k)
        print(f"{x} elevado a la {k} es igual a {resultado}")
    
    elif opcion == "2":
        x = int(input("Ingrese un número entero (X): "))
        digitos = contar_digitos(x)
        print(f"El número {x} tiene {digitos} dígitos")
    
    elif opcion == "3":
        x = int(input("Ingrese un número entero (X): "))
        if es_capicua(x):
            print(f"El número {x} es capicúa")
        else:
            print(f"El número {x} no es capicúa")
    
    elif opcion == "4":
        print("¡Hasta luego!")
        break
    
    else:
        print("Opción no válida. Intente nuevamente.")


"""
Ejercicio 6: Escriba un programa que para dos matrices A y B de números enteros de dimensiones MxN, realice la suma o el
producto de las matrices (a elección del usuario) y las cargue en otra matriz C.
Utilizar funciones y/o procedimientos para:
- cargar las matrices
- realizar la suma
- realizar el producto
- mostrar en pantalla una matriz
Invóquelas adecuadamente.
"""


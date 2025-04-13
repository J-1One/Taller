# Ejercicio 1: Contar dígitos de un número entero
def solicitar_numero():
    return int(input("Ingrese un número entero: "))

def contar_digitos(numero):
    contador = 0
    while numero != 0:
        numero //= 10
        contador += 1
    return contador

def mostrar_digitos():
    numero = solicitar_numero()
    print(f"El número tiene {contar_digitos(numero)} dígitos.")

# Ejercicio 2: Contar dígitos enteros y decimales
def solicitar_decimal():
    return float(input("Ingrese un número decimal: "))

def contar_digitos_decimal(numero):
    parte_entera = int(numero)
    parte_decimal = numero - parte_entera
    contador_entera = contar_digitos(parte_entera)
    contador_decimal = 0
    while parte_decimal > 0:
        parte_decimal *= 10
        digito = int(parte_decimal)
        parte_decimal -= digito
        contador_decimal += 1
    return contador_entera, contador_decimal

def mostrar_digitos_decimal():
    numero = solicitar_decimal()
    enteros, decimales = contar_digitos_decimal(numero)
    print(f"Parte entera: {enteros} dígitos, Parte decimal: {decimales} dígitos")

# Ejercicio 3: Mostrar números compuestos de una lista
def es_compuesto(numero):
    if numero < 2:
        return False
    divisor = 2
    while divisor * divisor <= numero:
        if numero % divisor == 0:
            return True
        divisor += 1
    return False

def mostrar_numeros_compuestos(lista):
    compuestos = [num for num in lista if es_compuesto(num)]
    print("Números compuestos:", compuestos)

# Ejercicio 4: Invertir un vector
def invertir_vector_aux(vector):
    return vector[::-1]

def invertir_vector_sin_aux(vector):
    for i in range(len(vector) // 2):
        vector[i], vector[-i - 1] = vector[-i - 1], vector[i]
    return vector

# Ejercicio 5: Filtrar números según criterios
def tiene_dos_pares(numero):
    pares = 0
    while numero > 0:
        if (numero % 10) % 2 == 0:
            pares += 1
        numero //= 10
    return pares == 2

def tiene_al_menos_dos_impares(numero):
    impares = 0
    while numero > 0:
        if (numero % 10) % 2 != 0:
            impares += 1
        numero //= 10
    return impares >= 2

def filtrar_lista(lista):
    return [num for num in lista if tiene_dos_pares(num) or tiene_al_menos_dos_impares(num)]

# Ejercicio 6: Insertar K a la derecha de cada múltiplo de K
def insertar_k(lista, k):
    resultado = []
    for num in lista:
        resultado.append(num)
        if num % k == 0:
            resultado.append(k)
    return resultado

# Ejercicio 7: Calcular promedios de filas y columnas en una matriz
def promedios_matriz(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    promedios_filas = [sum(fila) / len(fila) for fila in matriz]
    promedios_columnas = [sum(matriz[i][j] for i in range(filas)) / filas for j in range(columnas)]
    return promedios_filas, promedios_columnas

# Ejercicio 8: Filtrar números de matriz según factorial y diagonal
def factorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

def suma_diagonal_principal(matriz):
    return sum(matriz[i][i] for i in range(len(matriz)))

def filtrar_matriz_por_factorial(matriz):
    suma_diagonal = suma_diagonal_principal(matriz)
    elementos_validos = []
    for fila in matriz:
        for num in fila:
            if factorial(num) >= suma_diagonal:
                if num not in elementos_validos:
                    elementos_validos.append(num)
    return elementos_validos

# Ejercicio 9: Determinar si un elemento es punto silla
def es_punto_silla(matriz, k, h):
    valor = matriz[k][h]
    return valor == max(matriz[k]) and valor == min([matriz[i][h] for i in range(len(matriz))])

# Ejercicio 10: Determinar si una matriz es simétrica
def es_simetrica(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    if filas != columnas:
        return False
    for i in range(filas):
        for j in range(i, columnas):
            if matriz[i][j] != matriz[j][i]:
                return False
    return True

def factorial(n):
    if n == 0 or n == 1:   # caso base
        return 1
    else:
        return n * factorial(n - 1)  # caso recursivo

#Ejemplo

n = int(input("Ingrese un número: "))
for i in range(1, n + 1):
    print(f"{i}! = {factorial(i)}")

#-------------------------------------------------------------------------

def fibonacci(n):
    if n <= 1:  # casos base
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Ejemplo
pos = int(input("Ingrese la posición de Fibonacci: "))
print("Serie de Fibonacci:")
for i in range(pos):
    print(fibonacci(i), end=" ")

#-------------------------------------------------------------------------

def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

# Ejemplo 
b = int(input("Ingrese la base: "))
e = int(input("Ingrese el exponente: "))
print(f"{b}^{e} = {potencia(b, e)}")

#-------------------------------------------------------------------------

def decimal_a_binario(n):
    if n == 0:
        return ""
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

# Ejemplo
num = int(input("Ingrese un número decimal: "))
binario = decimal_a_binario(num)
print(f"El número {num} en binario es: {binario if binario != '' else '0'}")

#--------------------------------------------------------------------------

def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

# Ejemplo
texto = input("Ingrese una palabra: ").lower()
print("¿Es palíndromo?", es_palindromo(texto))

#------------------------------------------------------------------------

def suma_digitos(n):
    if n < 10:
        return n
    else:
        return (n % 10) + suma_digitos(n // 10)

# Ejemplo
num = int(input("Ingrese un número: "))
print(f"La suma de los dígitos es: {suma_digitos(num)}")

#------------------------------------------------------------------------

def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)

# Ejemplo
niveles = int(input("Ingrese la cantidad de bloques en el nivel más bajo: "))
print(f"Total de bloques necesarios: {contar_bloques(niveles)}")

#------------------------------------------------------------------------

def contar_digito(numero, digito):
    if numero == 0:
        return 0
    ultimo = numero % 10
    if ultimo == digito:
        return 1 + contar_digito(numero // 10, digito)
    else:
        return contar_digito(numero // 10, digito)

# Ejemplo
num = int(input("Ingrese un número: "))
dig = int(input("Ingrese el dígito a contar: "))
print(f"El dígito {dig} aparece {contar_digito(num, dig)} veces en {num}.")
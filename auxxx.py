# Ejemplo de lista
lista_numeros = [5, 15, 30, 1]

# Suponemos que el primer elemento de la lista es el máximo inicialmente
maximo_numero = lista_numeros[0]

# Recorremos el resto de la lista para encontrar el máximo
for numero in lista_numeros:
    if numero > maximo_numero:
        maximo_numero = numero

print("El número máximo es:", maximo_numero)

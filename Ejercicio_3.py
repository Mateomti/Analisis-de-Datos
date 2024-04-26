#Punto 1
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
frutas = ('manzana', 'platano', 'naranja', 'uva', 'piña')
#Punto 2
print(numeros[:3])

print(frutas[::2])

#Punto 3

for num in numeros:
    print(num)

for valor, indice in enumerate(frutas):
    print(f"Indice: {valor}, elemento: {frutas[valor]}")

#desafios
    
def extraer_pares_impares(lista):
    pares = []
    impares = []
    
    for num in lista:
        if num%2==0:
            pares.append(num)
        else:
            impares.append(num)
    return pares, impares

print(extraer_pares_impares([1,2,3,4,5,5,6]))

#Laboratorio de Python – Colecciones – Parte 2

#punto 1

tupla = (20, 40)
va = tupla
vb = tupla

print (va, vb)

#punto 2
lista_prod = []












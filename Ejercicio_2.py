#Punto 1

numeros = [1,2,3,4,5]
print(numeros)

#Punto 1.2

numeros.append(6)
print(numeros)

#Punto 1.3

print(f'La longitud de la lista es: {len(numeros)}')

#Punto 2

colores = {'rojo', 'amarillo', 'violeta'}
set(colores)
print(colores)

#Punto 2.1

colores.add('azul')
print(colores)

#Punto 3

persona = {'nombre': 'Mateo', 'edad':'22', 'ciudad': 'Rio Grande'}
print(persona) 

#Punto 3.2
persona['Ocupacion'] = 'Cocinero'
print(persona) 

#Punto 3.3
persona['ciudad'] = 'Ushuaia'
print(persona)

#Punto 4
for num in numeros:
    print(num*2)

#Punto 5

for color in colores:
    print(color.upper())

#Punto 6

for clave, key in persona.items():
    print(f'Clave: {clave} | Valor: {key}')


#Punto 7

numeros_cuadrados = {1 : 1**2, 2 : 2**2, 3:3**2, 4:4**2, 5:5**2}
print(numeros_cuadrados)
#Punto 1

nombre = 'Mateo Insaurralde'
a = 7
b= 3

print(f'Mi nombre es {nombre}, y la suma de 7 y 3 da: {a+b}')

#punto 2
print(
f'''a - b = {a-b}
a * b = {a*b}
a / b = {a/b}''')

#punto 3
if (a+b) % 2 == 0:
    print('La suma entre a y b es par.')
else:
    print('El numero es impar.')

#punto 4

for num in range(0, 5):
    print(num+1)

#punto 5

def saludar(nombre):
    return f'Hola {nombre}, bienvenido!'

print(saludar(nombre))

#punto 6

def multiplicar_por_2(x):
    return f'{x} multiplicado por 2 da: {x*2}'

print(multiplicar_por_2(3))

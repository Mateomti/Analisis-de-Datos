
datos = [

    {"Nombre": "Mateo", "Peso": 75, "Altura": 1.84},

    {"Nombre": "Renata", "Peso": 70, "Altura": 1.59},

    {"Nombre": "Flor", "Peso": 70, "Altura": 1.70},

    {"Nombre": "Facundo", "Peso": 85, "Altura": 1.78}

]

imc = [persona['Peso'] / persona['Altura']**2 for persona in datos]

print(imc)

def ClasificarIMC(imc):
  if imc < 18.5:
    print(f'Con un imc de: {imc}, su clasificacion es: "Bajo peso".')
  elif 	18.5 <= imc < 24.9:
    print(f'Con un imc de: {imc}, su clasificacion es: "Normal".')
  elif 25 <= imc < 29.9:
    print(f'Con un imc de: {imc}, su clasificacion es: "Sobrepeso".')
  elif 	30 <= imc < 34.9:
    print(f'Con un imc de: {imc}, su clasificacion es: "Obesidad Grado 1".')
  elif 	35 <= imc < 39.9:
    print(f'Con un imc de: {imc}, su clasificacion es: "Obesidad Grado 2".')
  elif imc >= 40:
    print(f'Con un imc de: {imc}, su clasificacion es: "Obesidad grado 3 (mórbida)".')

ClasificarIMC(27)

for persona in datos:
  res = f'Con un imc de: {imc}, su clasificacion es: "Bajo peso".' if persona['Peso'] / persona['Altura']**2 < 18.5 else f'Con un imc de: {imc}, su clasificacion es: "Normal".'
  print(res)


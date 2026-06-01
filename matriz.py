#matrices
notas = [
    [4.0, 3.5, 4.2],
    [5.0, 4.8, 4.5],
]

for fila in notas:
    print(fila)

promedio = sum(fila)/len(fila)
if promedio >= 3.0:
    print(promedio)
    print("Aprueba")
else: 
    print("No aprueba")


#FUNCIONES
def saludar():
    print("Bienvenido al sistema")

saludar()


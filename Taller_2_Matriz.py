n_estudiantes = int(input("Ingrese el número de estudiantes: "))
n_notas = int(input("Ingrese el número de notas por estudiante: "))

matriz_notas = [] 

for i in range (n_estudiantes):
    fila = []
    print(f"ingrese las {n_notas} notas del estudiante {i+1}: ")
    for j in range (n_notas):
        while True:
            try:
                nota = float(input(f"Nota {j+1}: "))
                fila.append(nota)
                break
            except ValueError:
                print("Error: Por favor, ingrese un número válido para la nota.") 
    matriz_notas.append(fila)

promedios = []
print("--- Promedios de cada estudiante ---")
for i, fila in enumerate(matriz_notas):
    promedio = sum(fila) / len(fila)
    promedios.append(promedio)
    print(f"Estudiante {i+1}: Notas = {fila}, | Promedio = {promedio:.2f}")

mejor = max(promedios)
posicion = promedios.index(mejor)
print(f"\nEl estudiante con el mejor promedio es el Estudiante {posicion+1} con un promedio de {mejor:.2f}")
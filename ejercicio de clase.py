def calcular_promedio(notas_estudiante):
    """Función que recibe una lista de notas y retorna el promedio"""
    suma = sum(notas_estudiante)
    promedio = suma / len(notas_estudiante)
    return promedio

# 1. Registrar datos con input
num_estudiantes = 3
num_materias = 3

# Pedir nombres de materias
print("=== CONFIGURACIÓN ===")
materias = []
for j in range(num_materias):
    nombre_materia = input(f"Ingresa el nombre de la materia {j+1}: ")
    materias.append(nombre_materia)

# Pedir nombres de estudiantes y sus notas
notas = []
nombres_estudiantes = []

print("\n=== REGISTRO DE NOTAS ===")
for i in range(num_estudiantes):
    nombre = input(f"\nNombre del estudiante {i+1}: ")
    nombres_estudiantes.append(nombre)

    notas_estudiante = []
    print(f"Ingresa las notas de {nombre}:")

    for j in range(num_materias):
        while True:
            try:
                nota = float(input(f" Nota de {materias[j]}: "))
                if 0 <= nota <= 5:
                    notas_estudiante.append(nota)
                    break
                else:
                    print(" Error: La nota debe estar entre 0 y 5")
            except ValueError:
                print(" Error: Ingresa un número válido")
    notas.append(notas_estudiante)

# 2. Calcular promedios y 3. Evaluar resultados
print("\n=== RESULTADOS FINALES ===")
aprobados = 0
reprobados = 0

for i in range(len(notas)):
    promedio = calcular_promedio(notas[i])

    print(f"\n{nombres_estudiantes[i]}:")
    for j in range(num_materias):
        print(f" {materias[j]}: {notas[i][j]}")
    print(f" Promedio: {promedio:.2f}")

    # Evaluar con ciclo condicional
    if promedio >= 3.0:
        print(f" Estado: APRUEBA ✓")
        aprobados += 1
    else:
        print(f" Estado: REPRUEBA ✗")
        reprobados += 1

print("\n=== RESUMEN ===")
print(f"Total aprobados: {aprobados}")
print(f"Total reprobados: {reprobados}")
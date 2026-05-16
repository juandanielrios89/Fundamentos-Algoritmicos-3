# Taller 1 - Fundamentos de Programación 3 
# Juan Daniel Rios Bustamante

'''1.	Crea un vector llamado nombres que guarde 
al menos 5 nombres de tus compañeros. Muestra 
cada nombre usando un ciclo.'''

print("Ejercicio 1: Vector de Nombres") 

nombres =  ["Santiago", "Luis", "Daniel", "David", "Sergio"] # Vector de nombres
print("Lista de compañeros:")  # Print para imprimir el encabezado
for nombre in nombres: # Itera sobre cada nombre en el vector y lo imprime
    print(nombre) 

'''2.	Declara un vector de 7 notas. Después de ingresar las notas por teclado, calcula y muestra:
o	a) La nota mayor
o	b) La nota menor
o	c) El promedio de notas
'''

print("\nEjercicio 2: Notas")

notas = [] # Vector para almacenar las notas ingresadas por el usuario
print("--- Ingreso de Notas ---") # Solicita al usuario que ingrese las notas
for i in range(7): # Itera 7 veces para ingresar las notas
    nota = float(input(f"Ingrese la nota {i+1}: "))  # Convierte la entrada a un número decimal (float) y la almacena en la variable nota
    notas.append(nota)

nota_mayor = max(notas) # Calcula la nota mayor
nota_menor = min(notas) # Calcula la nota menor
promedio = sum(notas) / len(notas) # Calcula el promedio de las notas

print("--- Resultados ---")
print(f"a) La nota mayor es: {nota_mayor}") # Imprime la nota mayor
print(f"b) La nota menor es: {nota_menor}") # Imprime la nota menor
print(f"c) El promedio de notas es: {promedio:.2f}") # Imprime el promedio de notas con dos decimales


'''3.	Crea un vector de 10 números enteros. 
Cambia el valor del quinto elemento por 99 y muestra el vector actualizado.'''
print("\nEjercicio 3: Vector de Números Enteros")

dieznumeros = [25, 31, 3, 41, 15, 65, 71, 87, 19, 10] # Vector de 10 números enteros
print("Vector original:", dieznumeros) # Imprime el vector original
dieznumeros[4] = 99
print("Vector actualizado:", dieznumeros) #imprime el vector actualizado con el quinto elemento cambiado a 99


'''4.	Haz un programa donde el usuario ingrese 5 edades. 
Luego, imprime solo las edades mayores o iguales a 18 años.'''
print("\nEjercicio 4: Edades")

edades = [] # Vector para almacenar las edades ingresadas por el usuario
print("--- Ingreso de Edades ---") 
for i in range(5): # Itera 5 veces para ingresar las edades
    edad = int(input(f"Ingrese la edad {i+1}: ")) # Convierte la entrada a un número entero (int) y la almacena en la variable edad
    edades.append(edad)  # Agrega la edad ingresada al vector de edades

print("--- Edades mayores o iguales a 18 años ---") 
for edad in edades: # Itera sobre cada edad en el vector de edades
    if edad >= 18: # Verifica si la edad es mayor o igual a 18
        print(edad)    # Imprime la edad si cumple la condición

"""5.	Modifica el vector de nombres del ejercicio 
1 eliminando el tercer nombre y muestra el vector resultante."""
print("\nEjercicio 5: Modificación del Vector de Nombres")

nombres =  ["Santiago", "Luis", "Daniel", "David", "Sergio"] 
print("Vector original:", nombres) # Imprime el vector original de nombres
del nombres[2]  # Elimina el tercer nombre (índice 2) del vector de nombres
print("Vector actualizado:", nombres) # Imprime el vector actualizado después de eliminar el tercer nombre
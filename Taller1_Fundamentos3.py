# Taller 1 - Fundamentos de Programación 3 
# Juan Daniel Rios Bustamante

'''1.	Crea un vector llamado nombres que guarde 
al menos 5 nombres de tus compañeros. Muestra 
cada nombre usando un ciclo.'''

nombres =  ["Santiago", "Luis", "Daniel", "David", "Sergio"]
print("Lista de compañeros:")
for nombre in nombres:
    print(nombre)

'''2.	Declara un vector de 7 notas. Después de ingresar las notas por teclado, calcula y muestra:
o	a) La nota mayor
o	b) La nota menor
o	c) El promedio de notas
'''

notas = []
print("--- Ingreso de Notas ---")
for i in range(7):
    nota = float(input(f"Ingrese la nota {i+1}: "))
    notas.append(nota)

nota_mayor = max(notas)
nota_menor = min(notas)
promedio = sum(notas) / len(notas)

print("--- Resultados ---")
print(f"a) La nota mayor es: {nota_mayor}")
print(f"b) La nota menor es: {nota_menor}")
print(f"c) El promedio de notas es: {promedio:.2f}")


'''3.	Crea un vector de 10 números enteros. 
Cambia el valor del quinto elemento por 99 y muestra el vector actualizado.'''

dieznumeros = [25, 31, 3, 41, 15, 65, 71, 87, 19, 10]
print("Vector original:", dieznumeros)
dieznumeros[4] = 99
print("Vector actualizado:", dieznumeros)


'''4.	Haz un programa donde el usuario ingrese 5 edades. 
Luego, imprime solo las edades mayores o iguales a 18 años.'''

edades = []
print("--- Ingreso de Edades ---")
for i in range(5):
    edad = int(input(f"Ingrese la edad {i+1}: "))
    edades.append(edad) 

print("--- Edades mayores o iguales a 18 años ---")
for edad in edades:
    if edad >= 18:
        print(edad)    

"""5.	Modifica el vector de nombres del ejercicio 
1 eliminando el tercer nombre y muestra el vector resultante."""

nombres =  ["Santiago", "Luis", "Daniel", "David", "Sergio"]
print("Vector original:", nombres)
del nombres[2]  # Elimina el tercer nombre (índice 2)
print("Vector actualizado:", nombres)
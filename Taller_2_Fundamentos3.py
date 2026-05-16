vector =  []
for i in range(15):
   while True:
        try: 
            valor = int(input(f"ingresa el valor {i+1}: "))
            vector.append(valor)    
            break
        except ValueError:
            print("Error: Por favor, ingrese un número entero válido.")

print("Vector original:", vector)

valor_mayor = max(vector)
valor_menor = min(vector)
posicion_mayor = vector.index(valor_mayor)
posicion_menor = vector.index(valor_menor)

print(f"El valor mayor es: {valor_mayor} y se encuentra en la posición: {posicion_mayor}")
print(f"El valor menor es: {valor_menor} y se encuentra en la posición: {posicion_menor}")

promedio = sum(vector) / len(vector)
print(f"El promedio de los valores es: {promedio:.2f}")

print("\n--- Modificación del Vector ---")
modificar_posicion = int(input("Ingrese la posición del valor a modificar (1-15): "))
nuevo_valor = int(input("Ingrese el nuevo valor: "))

if 1 <= modificar_posicion <= (len(vector)):
    while True:
        try:        
            vector[modificar_posicion - 1] = nuevo_valor
            print("Vector actualizado:", vector)
            break
        except ValueError:
            print("Error: Por favor, ingrese un número entero válido.")
else:   print("Error: La posición ingresada no es válida. Por favor, ingrese un número entre 1 y 15.")

# Muestra el vector actualizado
print("\n--- Base de datos actualizada ---")
print(f"Vector actualizado: {vector}")
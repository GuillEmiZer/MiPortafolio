"""
Hacer un algoritmo donde se ingresan 10 números enteros. Mostrar por pantalla el
número más grande ingresado y en qué posición se ingresó. Emitir mensaje de Error
si el dato ingresado no es un número entero.
"""

ITERACIONES = 10
conteo = 1
conteowhile = 0
numalto = 0
posicion = 0

while conteowhile < ITERACIONES:
    num = input(f"ingrese {conteo}° número entero: ")

    if num.isdigit():
        conteo +=1
        conteowhile +=1
        if int(num) > numalto:
            numalto = int(num)
            posicion = conteo
    else:
        print("¡ERROR! INGRESE UN NÚMERO ENTERO")

print("De los números ingresados el entero mas grandes es: ", numalto)
print(f"El número fue ingresado en la {posicion - 1}° posición")















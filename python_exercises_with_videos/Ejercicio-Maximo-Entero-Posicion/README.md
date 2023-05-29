README

Video - funcionamiento del programa con errores forzados: 
https://www.linkedin.com/feed/update/urn:li:activity:7054230546788347904/

-------------------------------------------------------------------------------------
DIAGRAMA DE FLUJO

Inicio

Declarar ITERACIONES = 10, conteo = 1, conteowhile = 0, numalto = 0, posicion = 0

Mientras conteowhile < ITERACIONES:
    
    Leer num
    
    Si num es un número entero:
    
        Incrementar conteo en 1
        Incrementar conteowhile en 1
        
        Si num > numalto:
            Asignar numalto = num
            Asignar posicion = conteo
    
    Si no:
    
        Mostrar "¡ERROR! INGRESE UN NÚMERO ENTERO"
    
Fin mientras

Mostrar "De los números ingresados el entero mas grandes es: ", numalto
Mostrar "El número fue ingresado en la", posicion - 1, "° posición"

Fin
-----------------------------------------------------------------------------------












negativos = 0

positivos = 0

suma_positivos = 0

suma_negativos = 0

num = 1

try:

    while num != 0:
        print("Ingrese un numero")
        num = int(input())
        
        
        if num > 0:
            positivos += 1
            suma_positivos += suma_positivos + num
            
        elif num < 0:
            negativos += 1
            suma_negativos += num
            

    

    promedio_positivos = suma_positivos / positivos

    promedio_negativos = suma_negativos / negativos

    print(f"Cantidad de positivos: {positivos}")
    print(f"Promedio positivos: {promedio_positivos}")

    print(f"Cantidad de negativos: {negativos}")
    print(f"Promedio negativos: {promedio_negativos}")
    
except ValueError as e:
    print("Error, solo se permiten numeros")
    
except ZeroDivisionError as e:
    print("Fin del programa")
    
        
    
    
    
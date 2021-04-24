#Obtener Promedio, La mayor nota y la menor.
Lista_Notas = []
suma_Notas = 0
Prom = 0

print()
def bienvenida():
    print("'------------------Bienvenido--------------------'\n")
    nombre = input("Ingrese su nombre: ")
    apellido =  input(f"Bienvenido {nombre}.\nIngrese su apellido: ")
    saludo = print(f"Bienvenido {nombre} {apellido}")

bienvenida()
print()
print("'-----------------Notas----------------------'\n")

while True:
    try:
        def notas():
            not1 = float(input("Ingrese la primera nota: "))
            not2 = float(input("Ingrese la segunda nota: "))
            not3 = float(input("Ingrese la tercera nota: "))
            not4 = float(input("Ingrese la cuarta nota: "))
            not5 = float(input("Ingrese la quinta nota: ")) 

            Lista_Notas.append(not1)
            Lista_Notas.append(not2)
            Lista_Notas.append(not3)
            Lista_Notas.append(not4)
            Lista_Notas.append(not5)

        notas()
        break
    except (TypeError, ValueError) :
            print('Ocurrio un problema: El valor ingresado es incorrecto\nIngrese un dato correcto')


    
for nota in Lista_Notas:

    suma_Notas= suma_Notas + nota
    Prom = suma_Notas / len(Lista_Notas)


    Nota_Menor= min(Lista_Notas)
    Nota_mayor =max(Lista_Notas)
                

print()
print("'------------------RESULTADOS-----------------------'\n")  
print(f"Lista de notas: {Lista_Notas}")
print(f"'El Promedio es: {Prom}'")
print(f"'Nota mayor: {Nota_mayor}'")
print(f"'Nota menor: {Nota_Menor}'")
                
    

    



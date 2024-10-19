def proceso_1():
    while True:
                print('Por favor, introduzca una puntuación en una escala de 1 a 5')
                point = input()
                
                if point.isdecimal():
                    point = int(point)
                    
                    if point <= 0 or point > 5:  
                        print('Indíquelo en una escala de 1 a 5')
                    else:
                        print('Por favor, introduzca un comentario')
                        comment = input()
                        post = f'punto: {point} comentario: {comment}'
                        file_pc = open("data.txt", 'a')
                        file_pc.write(f'{ post } \n')
                        file_pc.close()
                        break
                else:
                    print("Porfavor, Introduzca un valor entre el 1 y 5")


def proceso_2():
    print('Resultados hasta la fecha.')
    with open("data.txt", "r") as read_file:
        print(read_file.read())


def proceso_3():
 while True:
   if num == 3:
     print("Finalizado")
     break

   

while True:
    print("Seleccione el proceso que desa aplicar")
    print("1: Inrgresar puntuacion y comentario")
    print("2: Comprueba los resultados obtenidos hasta ahora")
    print("3: Finalizar")

    num= int(input("Ingrese el numero deseado:"))
    if num == 1:
        proceso_1()
    elif num == 2:
        proceso_2()
    elif num == 3:
        proceso_3()
        break
    else:
        print("Introduzca un numero del 1 al 3")

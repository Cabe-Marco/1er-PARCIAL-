import json

def leer_archivo(archivo_json: str) -> list:
    lista_jugadores = []
    with open(archivo_json, "r") as archivo:
        diccionario = json.load(archivo)
        lista_jugadores = diccionario["jugadores"]
    return lista_jugadores
 
def mostrar_Nombre_y_Posicion_de_Jugadores(lista_jugadores:list):       
    longitud_lista_jugadores = len(lista_jugadores)                     
    print("\n")                                                           
    for i in range(longitud_lista_jugadores):
        jugador_nombre = lista_jugadores[i]["nombre"]
        jugador_posicion = lista_jugadores[i]["posicion"]

        mensaje = "{0} - {1}".format(jugador_nombre,jugador_posicion)
        print(mensaje)
        
                                                        ### PROGRAMA ###
#mostrar_Nombre_y_Posicion_de_Jugadores(lista_jugadores) #PUNTO 1cx

def mostrar_jugador_y_su_indice(lista_jugadores:list):
    longitud_lista_jugadores = len(lista_jugadores)                       # Nombre Jugador - Posición. Ejemplo:     
    print("\n")                                                           # Michael Jordan - Escolta  
    for i in range(longitud_lista_jugadores):
        jugador_nombre = lista_jugadores[i]["nombre"]

        mensaje = "{0} - {1}".format(jugador_nombre,i)
        print(mensaje)

def estadisticas_de_jugador(indice_jugador:int,lista_jugadores:list):
      
    i= int(indice_jugador)
    jugador = lista_jugadores[i]["estadisticas"]
    return(jugador)
    

def generar_csv(nombre_archivo:str, lista, lista_jugadores,indice_jugador:int):
    with open(nombre_archivo, "w") as archivo:
        indice_jugador= int(indice_jugador)
        nombre_jugador = lista_jugadores[indice_jugador]["nombre"]
        posicion_jugador = lista_jugadores[indice_jugador]["posicion"]
        texto_nombre_y_posicion = "nombre: {0},posicion: {1}".format(nombre_jugador,posicion_jugador)
        texto = ""
        for i in lista:
            texto_estadisticas = ",{0}: {1} ".format(i,lista[i]) # i es el titulo del dato lista[i] es el dato
            texto += texto_estadisticas
            
        texto_nombre_y_posicion += texto    
        archivo.write(texto_nombre_y_posicion)

def imprimir_estadisticas_jugador_seleccionado():
    mostrar_jugador_y_su_indice(lista_jugadores)  #MUESTRO EL NOMBRE Y SU INDICE DE JUGADOR
    indice_jugador = input("Ingrese el indice del jugador que desee ") #se ingresa el indice del jugadora que queremos saber sus estadisticas
    estadisticas_del_jugador_seleccionado = estadisticas_de_jugador(indice_jugador,lista_jugadores)
    print(estadisticas_del_jugador_seleccionado)

lista_jugadores = leer_archivo(r"C:\Users\Marquillos\Desktop\PARCIAL 1ER PROGRAMACION\1er-PARCIAL-\Dream_Team.json") #creo una lista con los datos de todo los jugadores sin el nombre del team





#estadisticas_de_jugador(indice_jugador,lista_jugadores)

''' 
#3  Después de mostrar las estadísticas de un jugador seleccionado por el usuario, permite al usuario guardar las estadísticas de ese jugador 
en un archivo CSV. El archivo CSV debe contener los siguientes campos: nombre, posición, temporadas, puntos totales, 
promedio de puntos por partido, rebotes totales, promedio de rebotes por partido, asistencias totales, promedio de asistencias por partido, 
robos totales, bloqueos totales, porcentaje de tiros de campo, porcentaje de tiros libres y porcentaje de tiros triples.
'''

#print(lista_jugadores[0]["nombre"])
#generar_csv(r"C:\Users\Marquillos\Desktop\PROGRAMACION\ARCHIVOS\EXAMEN\Dr_Team.csv",estadisticas_del_jugador_seleccionado,lista_jugadores,indice_jugador)

#while(True):
print("\n")
print("MENU OPCIONES:")
print("Punto 1")
print("Punto 2")
print("Punto 3")
print("0 para Finalizar")

opcion = input("\nElige un opcion:......")

match (opcion):
    case "1":
        mostrar_Nombre_y_Posicion_de_Jugadores(lista_jugadores)
    case "2":
        imprimir_estadisticas_jugador_seleccionado(lista_jugadores)
    case "3":
        pass
    case _:
        break
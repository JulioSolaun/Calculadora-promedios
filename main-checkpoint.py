
import statistics as stad
import random

# Definición de la función
def ingresar_calificaciones():
    materias = []
    calificaciones = []
    #Imprimir posibles temas
    #Se utiliza variable tema para no confundirlo con la variable materia
    
    TEMAS = (
            "Introducción",
            "Primeros conceptos de Python",
            "Programación Básica",
            "Funciones",
            "Organización del código",
            "Aspectos avanzados",
            "Análisis de datos",
            "Visualización de datos"
            )
        #Imprimir materias que se pueden ingresar
    print("Las materias a introducir son:\n")
    for i in TEMAS:
        print (i)
    
    # Introducción de materias
    while True:
        tema = input("Introduzca el nombre de una materia: ")
    
        while tema not in TEMAS:
            print("Error: esa materia no pertenece al curso. Vuelva a intentarlo")
            tema = input("Introduce el nombre de una materia: ")
        
        materias.append(tema)
        
    # Introducción de calificaciones
        while True:
            try:
                nota = float(input("Introduce la nota (0-10): "))
        
                if 0 <= nota <= 10:
                    calificaciones.append(nota)
                    break
                else:
                    print("Error: la nota debe estar entre 0 y 10.")
        
            except ValueError:
                print("Error: debes introducir un número.")
        

            
        
    # Preguntar si desea continuar
        continuar = input("¿Deseas ingresar otra materia? (s/n): ").lower()
    
        if continuar != "s":
            break

    return materias, calificaciones

#Función para calcular el promedio de las calificaciones:
def promedio_calificaciones(calificaciones):
        return round(stad.mean(calificaciones), 2)
    
#Función para sacar una lista de lista de materias aprobadas y reprobadas
def estado_calificaciones(calificaciones, umbral=5.0):
    materias_aprobadas = []
    materias_reprobadas = []
    for i, j in zip(materias, calificaciones):
        if j >= umbral:
            materias_aprobadas.append(i)
        else:
            materias_reprobadas.append(i)
    return materias_aprobadas, materias_reprobadas


#Función buscar extremos
def encontrar_extremos(calificaciones, materias):
    materia_máxima = []
    materia_mínima = []
    for i,j in zip(materias,calificaciones):
        if j == max(calificaciones):
            materia_máxima.append(i)
        if j == min(calificaciones):
            materia_mínima.append(i)
    return materia_máxima, materia_mínima


def main():
#Ejecución función INGRESAR_CALIFICACIONES
    print("\nPrograma para introducir materias y calificaciones, así como calcular valores sobre las mismas")
    print("\nNO DA ÍNDICES DE LAS LISTAS, Sólo habria que poner la sentencia index antes de la lista")
    print("\nPara evitar errores en la introducción de materias, se ha definido una lista de posibles materias")

    materias, calificaciones = ingresar_calificaciones()
    
    print("\nLas materias con sus calificaciones son las siguientes: ")
    for i,j in zip(materias,calificaciones):
        print(i, j)

#Ejecución función PROMEDIO_CALIFICACIONES
    media_calificaciones = promedio_calificaciones(calificaciones)
    print("\nLa media de las calificaciones es: ", media_calificaciones)  

#Ejecución función ESTADO_CALIFICACIONES
    materias_aprobadas, materias_reprobadas = estado_calificaciones(calificaciones, umbral)
    
    print("\nLas materias aprobadas son: ")
    for i in materias_aprobadas:
        print (i)
    print("\nLas materias reprobadas son: ")
    for i in materias_reprobadas:
        print (i)

#Ejecución función ENCONTRAR_EXTREMOS
    materia_máxima, materia_mínima = encontrar_extremos(calificaciones, materias)
    
    print("\nLas materias con calificación máxima son:")
    for i in materia_máxima:
        print (i, max(calificaciones))
        
    print("\nLas materias con calificación mínimo son:")
    for i in materia_mínima:
        print (i, min(calificaciones))

    print("\n Gracias por utilizar la CALCULADORA DE PROMEDIOS!")

if __name__ == "__main__":
    main()

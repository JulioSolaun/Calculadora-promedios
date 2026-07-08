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
def calcular_promedio(calificaciones):
        return round(stad.mean(calificaciones), 2)
    
#Función para sacar una lista de lista de materias aprobadas y reprobadas
umbral=5.0
def determinar_estado(calificaciones, umbral):
    indice_materias_aprobadas = []
    indice_materias_reprobadas = []
    for indice, nota in enumerate(calificaciones):
        if nota >= umbral:
            indice_materias_aprobadas.append(indice)
        else:
            indice_materias_reprobadas.append(indice)
    return indice_materias_aprobadas, indice_materias_reprobadas


#Función buscar extremos
def encontrar_extremos(calificaciones):
    indices_materia_máxima = []
    indices_materia_mínima = []
    for indice, nota in enumerate(calificaciones):
        if nota == max(calificaciones):
            indices_materia_máxima.append(indice)
        if nota == min(calificaciones):
            indices_materia_mínima.append(indice)
    return indices_materia_máxima, indices_materia_mínima


def main():
#Ejecución función INGRESAR_CALIFICACIONES

    materias, calificaciones = ingresar_calificaciones()

    while len(materias) == 0:
        print("Se deben ingresar materias y calificaciones para poder hacer los cálculos")
        materias, calificaciones = ingresar_calificaciones()        
    
    print("\nLas materias con sus calificaciones son las siguientes: ")
    for i,j in zip(materias,calificaciones):
        print(i, j)

#Ejecución función CALCULAR_PROMEDIO
    media_calificaciones = calcular_promedio(calificaciones)
    print("\nLa media de las calificaciones es: ", media_calificaciones)  

#Ejecución función DETERMINAR_ESTADO
    indice_materias_aprobadas, indice_materias_reprobadas = determinar_estado(calificaciones, umbral)
    
    print("\nLos índices de las materias aprobadas son: ", indice_materias_aprobadas)
    print("\n Las materias aprobadas son: ")
    for i in indice_materias_aprobadas:
        print(materias[i], "-", calificaciones[i])
              
    print("\nLos índices de las materias reprobadas son: ", indice_materias_reprobadas)
    print("\n Las materias reprobadas son: ")
    for i in indice_materias_reprobadas:
        print(materias[i], "-", calificaciones[i])

#Ejecución función ENCONTRAR_EXTREMOS
    indices_materia_máxima, indices_materia_mínima = encontrar_extremos(calificaciones)
    
    print("\nLos indices con calificación máxima son:", indices_materia_máxima)
    for i in indices_materia_máxima:
        print(materias[i], "-", calificaciones[i])    
  
    print("\nLas materias con calificación mínimo son:", indices_materia_mínima)
    for i in indices_materia_mínima:
        print(materias[i], "-", calificaciones[i])       
   

    print("\n Gracias por utilizar la CALCULADORA DE PROMEDIOS!")

if __name__ == "__main__":
    main()

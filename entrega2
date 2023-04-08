nombres = ''' 'Agustin', 'Alan', 'Andrés', 'Ariadna', 'Bautista', 'CAROLINA', 'CESAR', 
'David', 'Diego', 'Dolores', 'DYLAN', 'ELIANA', 'Emanuel', 'Fabián', 'Facundo', 
'Francsica', 'FEDERICO', 'Fernanda', 'GONZALO', 'Gregorio', 'Ignacio', 'Jonathan',  
'Joaquina', 'Jorge', 'JOSE', 'Javier', 'Joaquín' , 'Julian', 'Julieta', 'Luciana',
 'LAUTARO', 'Leonel', 'Luisa', 'Luis', 'Marcos', 'María', 'MATEO', 'Matias', 
'Nicolás', 'Nancy', 'Noelia', 'Pablo', 'Priscila', 'Sabrina', 'Tomás', 'Ulises', 
'Yanina' '''
notas1 = [81, 60, 72, 24, 15, 91, 12, 70, 29, 42, 16, 3, 35, 67, 10, 57, 11, 69,
12, 77, 13, 86, 48, 65, 51, 41, 87, 43, 10, 87, 91, 15, 44,
85, 73, 37, 42, 95, 18, 7, 74, 60, 9, 65, 93, 63, 74]
notas2 = [30, 95, 28, 84, 84, 43, 66, 51, 4, 11, 58, 10, 13, 34, 96, 71, 86, 37,
64, 13, 8, 87, 14, 14, 49, 27, 55, 69, 77, 59, 57, 40, 96, 24, 30, 73,
95, 19, 47, 15, 31, 39, 15, 74, 33, 57, 10]

def crear(nombres, notas1, notas2):
    estudiantes = zip(nombres.split(", "), notas1, notas2)
    estud_dic = {}
    for nombre, nota1, nota2 in estudiantes:
	    estud_dic[nombre] =(nota1, nota2)
    return estud_dic


def promedio_por_estudiante(estudiantes):
    promedios = {}
    for estudiante in estudiantes:
        notas = estudiantes[estudiante]
        promedio = sum(notas) / len(notas)
        promedios[estudiante] = promedio
        print(f"estudiante:  {estudiante}, promedio: {promedio}")
    return promedios
    
def promedio_general(promedios):
    if len(promedios) > 0:
        promedio_general = sum(map(lambda x: x[1], promedios.items())) / len(promedios)
    else:
        promedio_general = 0
    print(f"promedio general: {promedio_general:.2f}")
    return promedio_general


def promedio_alto(promedios):
   return  max(promedios.items(), key=lambda estudiante: estudiante[1])[0]

def promedio_min(promedios):
    return  min(promedios.items(), key=lambda estudiante: estudiante[1])[0]

    
nombres = nombres.replace("\n", "")
estudiantes= crear(nombres, notas1, notas2)
prom= promedio_por_estudiante(estudiantes)
promedio_general(prom)
print (f"el alumno con mayor promedio: {promedio_alto(prom)}")
print (f"el alumno con menor promedio: {promedio_min(prom)}")

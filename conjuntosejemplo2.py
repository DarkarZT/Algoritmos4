algoritmos = {"Ana","Carlos","Diana", "Eduardo", "Fernanda","Gabriel","Helena","Ivan"}

bases_datos = {"Carlos","Diana", "Juan", "Karen", "Gabriel", "Luis", "Maria"}

redes = {"Diana", "Eduardo", "Gabriel", "Karen", "Natalia", "Oscar", "Ivan"}

Estudiantes_En_Todas = algoritmos & bases_datos & redes
Estudiantes_En_Una = algoritmos.union(bases_datos, redes)

informacion = {}

for estudiante in Estudiantes_En_Una:
    materias = []
    if estudiante in algoritmos:
        materias.append("algoritmos")
    if estudiante in bases_datos:
        materias.append("bases de datos")
    if estudiante in redes:
        materias.append("redes")
    
    informacion[estudiante] = materias
    
 
print("estan en todas", Estudiantes_En_Una)




print("Estan solo en 1", informacion)
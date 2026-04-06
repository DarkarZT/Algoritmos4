# import heapq

# class Nodo:
#     def __init__(self, nombre, prioridad, orden):
#         self.nombre = nombre,
#         self.prioridad = prioridad,
#         self.orden = orden
    
# print("Cuantos pacientes hay ?")
# n = int(input(""))
# datos = []
# while 0 < n:
#     nombre = input("Cual es el nombre del paciente")
#     prioridad = int(input("Cual es la prioridad del paciente"))
#     orden= int(input("Orden de llegada"))
#     dato = Nodo(nombre, prioridad, orden)
#     datos.append(dato)
#     n -=1

# datos.sort(key=lambda x: (x.prioridad, x.orden))


# print("Orden de atención de los pacientes:")
# for paciente in datos:
#     print(f"Paciente: {paciente.nombre}, Prioridad: {paciente.prioridad}, Orden de llegada: {paciente.orden}")

import heapq

n = int(input("Cuantos pacientes hay ?"))
lista={}

while n < 0:
    nombre = input("Cual es el nombre del paciente")
    prioridad = int(input("Cual es la prioridad del paciente"))
    orden= int(input("Orden de llegada"))
    tupla = tuple(nombre, prioridad, orden)
    lista.append(tupla)
    n -=1

    

heapq.heapify(lista)


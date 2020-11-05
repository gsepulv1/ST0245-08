class Alumno:
    def __init__(self, nombre, edad, nota):
        self.nombre = nombre
        self.edad = edad
        self.nota = nota
    def __str__(self):
       return self.nombre+' - '+str(self.edad)+' años :'+str(self.nota)
class Nodo:
    def __init__(self, datos):
        self.datos = datos
        self.siguiente = None

primero = None
alumno = Alumno('Alex', 30, 8.9)
nodo = Nodo(alumno)
nodo.siguiente = primero
primero = nodo
alumno = Alumno('Pepe', 27, 3.7)
nodo = Nodo(alumno)
nodo.siguiente = primero
primero = nodo
n = primero
while n != None:
 print(n.datos)
 n = n.siguiente

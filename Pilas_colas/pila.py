class Pila:
#El método __init__ es el primer método que se ejecuta cuando se crea un objeto  
     def __init__(self):
         self.items = []

     def incluir(self, item):
         self.items.append(item)

     def extraer(self):
         return self.items.pop()

     def tamano(self):
         return len(self.items)  

     def inspeccionar(self):
         return self.items[len(self.items)-1]    



p=Pila()
p.incluir('lunes')   
print(p.inspeccionar())  
print(p.tamano())
p.incluir('martes')
print(p.inspeccionar())  
print(p.tamano()) 
p.incluir('miercoles')
print(p.inspeccionar())  
print(p.tamano()) 
p.incluir('Jueves')
print(p.inspeccionar())  
print(p.tamano()) 
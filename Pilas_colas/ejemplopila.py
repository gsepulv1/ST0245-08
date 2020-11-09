class pila:
    def __init__ (self):
        self.items = []
#Metodos  
    #2.3
    def apilar(self,items):
        self.items.append(items)
    #2.4
    def size (self):
        return len(self.items)
    #2.5
    def lastElement(self):
        return self.items[len(self.items)-1]
    #2.6 
    def remover(self):
        try:
            self.items.remove(len(self.items)-1)
        except:
            raise ValueError("La pila está vacia")

pila1= pila()            
pila1.apilar(25)
print(pila1.lastElement())
 
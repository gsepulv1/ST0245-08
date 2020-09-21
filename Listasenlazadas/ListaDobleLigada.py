#Definicion de nodo Doble
class NodoDoble:
    def __init__(self,value,siguiente,previo):
        self.data = value
        #almacena la prodicion del siguiente nodo
        self.next = siguiente
        #almacena la posicion del nodo anterior
        self.prev = previo
    
class ListaDoblementeEnlazada:
    def __init__(self):
        #Definimos la cabeza
        self.__head = NodoDoble(None,None,None)
        #Definimos la cola
        self.__tail = NodoDoble(None,None,None)
        #Asignamos la cabeza y la cola 
        self.__head.next = self.__tail
        self.__tail.prev = self.__head
        self.__size = 0
    #para calcular el tamaño
    def get_size(self):
        return self.__size
    #Evalua si la lista es nula
    def is_empty(self):
      return self.get_size() == 0
    #Metodo para insetar
    def insert(self,value):
        if self.__size == 0:
            #si el tamaño de la lista es 0
            nuevo = NodoDoble(value,self.__tail,self.__head)
            self.__head.next = nuevo
            self.__tail.prev = nuevo
            # Si ya tiene elementos
        else:
            nuevo = NodoDoble(value,self.__tail,self.__tail.prev)
            self.__tail.prev.next = nuevo
            self.__tail.prev = nuevo
        self.__size += 1
    #recorrer la lista y imprimir
    def transversal(self):
        curr_Node = self.__head.next
        while curr_Node.next != None:
            print(curr_Node.data,"->",end=" ")
            curr_Node = curr_Node.next
        print("")
    #iprimir 
    def reverse_transversal(self):
        curr_Node = self.__tail.prev
        while curr_Node.prev != None:
            print(curr_Node.data,"->",end=" ")
            curr_Node = curr_Node.prev
        print("")
    #para encontrar la cabeza
    def find_from_head(self,value):
      curr_Node = self.__head
      encontrado = None
      while curr_Node.data != value:
        curr_Node = curr_Node.next
       
      if curr_Node.data == value:
        encontrado = curr_Node
       
      return encontrado
    # para encontrar la cola
    def find_from_tail(self,value):
      curr_Node = self.__tail
      encontrado = None
      while curr_Node.data != value:
        curr_Node = curr_Node.prev
       
      if curr_Node.data == value:
        encontrado = curr_Node
       
      return encontrado
    # Eliminar  dede la cabeza
    def remove_from_head(self,value):
      cur_Node = self.find_from_head(value)
      cur_Node.prev.next = cur_Node.next
      cur_Node.next.prev = cur_Node.prev
      cur_Node.next = None
      cur_Node.prev = None
      
      
      
    # eliminar desde la cola
    def remove_from_tail(self, value):
      cur_Node = self.find_from_tail(value)
      cur_Node.prev.next = cur_Node.next
      cur_Node.next.prev = cur_Node.prev
      cur_Node.next = None
      cur_Node.prev = None
      
      
    #insertar entre dos nodos
    def insert_between(self, value, predecesor, sucesor):
      predecesor = self.find_from_head(predecesor)
      sucesor = self.find_from_head(sucesor)

      if predecesor.next != sucesor:
         print("Los nodos no son consecutivos")
      else:
        nuevo = NodoDoble(value,sucesor,predecesor)
        predecesor.next = nuevo
        sucesor.prev = nuevo
        


#Evaluemolo
def main():

    ldl = ListaDoblementeEnlazada()

    print(f"Tamaño = {ldl.get_size()}")

    ldl.insert(10)

    ldl.insert(20)

    ldl.insert(30)

    ldl.insert(40)

    ldl.insert(50)

    ldl.transversal()
    ldl.reverse_transversal()

    ldl.insert_between(15,10,20)

    ldl.transversal()

    ldl.remove_from_head(15)

    ldl.transversal()
    
    print(f"Tamaño = {ldl.get_size()}")

main()      

class ListNode:
    def __init__(self,datoInicial):
        self.dato = datoInicial
### Podemos crear varias instancias de esta clase, 
# cada una almacenando datos de nuestra elección. 
# En el siguiente ejemplo, creamos tres instancias, cada una almacenando un valor entero     
a = ListNode( 11 )
b = ListNode( 52 )
c = ListNode( 18)
#####Ahora, suponga que agregamos un segundo campo de datos a la clase ListNode
class ListNode :
     def __init__( self, data ) :
          self.dato = datoInicial
          self.next = None
###Dado que el siguiente campo puede contener una referencia a cualquier tipo de objeto,
#  podemos asignarle una referencia a uno de los otros objetos ListNode. 
#  Por ejemplo, supongamos que asignamos b al siguiente campo del objeto a:
a.next = b
b.next = c
print(a.dato)
print(a.next.dato)
print(a.next.next.dato)
#imprimir nodos 

def traversal( head ):
    curNode = head 
    while curNode is not None : 
        print curNode.data 
        curNode = curNode.next

def unorderedSearch( head, target ):
    curNode = head 3 
    while curNode is not None and curNode.data != target :
        curNode= curNode.next 
    return curNode is not None

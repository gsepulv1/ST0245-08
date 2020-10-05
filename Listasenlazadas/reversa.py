class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class SinglyLinkedList:
    def __init__(self, he):
        self.he = he
    def length(self):
        current = self.he
        if current is not None:
            count = 1
            while current.next is not None:
                count += 1
                current = current.next
            return count
        else:
            return 0
    def insert(self, data, position):
        new_node = Node(data)
        if position == 0:
            new_node.next = head.he
            head.he = new_node
        else:
            current = head.he
            k = 1
            while current.next is not None and k < position:
                current = current.next
                k += 1
            new_node.next = current.next
            current.next = new_node   
    def reverse(self):
        pre=sig= None
        i= self.he
       
        while  i:
            sig=i.next
            i.next =pre
            pre=i
            i=sig
        self.he=pre

#creamos la lista
head= SinglyLinkedList(Node(1))
#rellenamos la lista
for i in range(2,6):
    head.insert(i, i-1)
#mostramos la lista
current = head.he
while current is not None:
    print(current.data)
    current = current.next 

head.reverse()
current = head.he
while current is not None:
    print(current.data)
    current = current.next           
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self, head):
        self.head = head

    def length(self):
        current = self.head
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
            new_node.next = linked_list.head
            linked_list.head = new_node
        else:
            current = linked_list.head
            k = 1
            while current.next is not None and k < position:
                current = current.next
                k += 1
            new_node.next = current.next
            current.next = new_node

    def delete(self, position):
        if position != 1:
            current = self.head
            k = 1
            while current.next is not None and k < position - 1:
                current = current.next
                k += 1
            if current.next is not None:
                current.next = current.next.next
                return True
            else:
                return False
        else:
            self.head = self.head.next
            return True
#creamos la lista
linked_list = SinglyLinkedList(Node(1))

#rellenamos la lista
for i in range(2,10):
    linked_list.insert(i, i-1)

#insertamos un elemento
linked_list.insert(999,3)

#eliminamos un elemento
linked_list.delete(6)

#mostramos la lista
current = linked_list.head
while current is not None:
    print(current.data)
    current = current.next            
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None



class SinglyLinkedList:
    def __init__(self):
        self.head = None


    def insert_first(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_end(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node

    def insert_middle(self, pos, data):
        if pos == 0:
            self.insert_first(data)
            return

        new_node = Node(data)
        temp = self.head

        for _ in range(pos - 1):
            if temp is None:
                print("Position out of bounds")
                return
            temp = temp.next

        if temp is None:
            print("Position out of bounds")
            return

        new_node.next = temp.next
        temp.next = new_node

    def delete_first(self):
        if self.head:
            self.head = self.head.next

    def delete_end(self):
        if not self.head:
            return

        if not self.head.next:
            self.head = None
            return

        temp = self.head
        while temp.next.next:
            temp = temp.next

        temp.next = None

    def delete_middle(self, pos):
        if pos == 0:
            self.delete_first()
            return

        temp = self.head

        for _ in range(pos - 1):
            if temp is None or temp.next is None:
                print("Position out of bounds")
                return
            temp = temp.next

        if temp.next:
            temp.next = temp.next.next

    def display(self):
        temp = self.head

        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")



s = SinglyLinkedList()

print("Insert First:")
s.insert_first(10)
s.display()

print("Insert End:")
s.insert_end(20)
s.display()

print("Insert Middle:")
s.insert_middle(1, 15)
s.display()

print("Delete First:")
s.delete_first()
s.display()

print("Delete End:")
s.delete_end()
s.display()
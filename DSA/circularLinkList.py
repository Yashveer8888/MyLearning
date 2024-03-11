class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CLinkedList:
    def __init__(self):
        self.head = None
        
    # add node in last
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            return
        last_node = self.head
        while last_node.next != self.head:
            last_node = last_node.next
        last_node.next = new_node
        new_node.next = self.head
        print(f'append {new_node.data}')
    
    # add node in beginning
    def prepend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            return
        last_node = self.head
        while last_node.next != self.head:
            last_node = last_node.next
        new_node.next = self.head
        self.head = new_node
        last_node.next = new_node
        print(f'append {new_node.data}')

    # delete node
    def deleteNode(self, data):
        if not self.head:
            return
        if self.head.data == data:
            if self.head.next == self.head:
                self.head = None
            else:
                current_node = self.head
                while current_node.next != self.head:
                    current_node = current_node.next
                current_node.next = self.head.next
                self.head = self.head.next
            return
        prev_node = None
        current_node = self.head
        while current_node.next != self.head:
            if current_node.data == data:
                break
            prev_node = current_node
            current_node = current_node.next
        if current_node.data != data:
            print("Data not found in the list")
            return
        prev_node.next = current_node.next
        print(f'delete {data}')

    # delete index node
    def deleteAtIndex(self, index):
        if index == 0:
            if self.head.next == self.head:
                self.head = None
            else:
                current_node = self.head
                while current_node.next != self.head:
                    current_node = current_node.next
                current_node.next = self.head.next
                self.head = self.head.next
            return
        prev_node = None
        current_node = self.head
        count = 0
        while count < index:
            if current_node.next == self.head:
                print("Index out of range")
                return
            prev_node = current_node
            current_node = current_node.next
            count += 1
        prev_node.next = current_node.next
        print(f'delete index {index} data = {current_node.data}')

    # print LinkedList
    def print_list(self):
        if not self.head:
            print("Empty list")
            return
        current_node = self.head
        while True:
            print(current_node.data, end="->")
            current_node = current_node.next
            if current_node == self.head:
                break
        print(f"{self.head.data}\n")


if __name__ == "__main__":
    linked_list = CLinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.append(4)
    linked_list.append(5)
    linked_list.append(6)
    linked_list.append(7)
    linked_list.append(8)
    linked_list.append(9)
    linked_list.prepend(0)
    linked_list.print_list()
    linked_list.deleteNode(6)
    linked_list.deleteAtIndex(3)
    linked_list.print_list()

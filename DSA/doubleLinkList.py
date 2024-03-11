class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.pre = None

class DLinkedList:
    def __init__(self):
        self.head = None
        
    # add node at the end
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        print(f"append {data}")
    
    # add node at the beginning
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        print(f"prepend {data}")

    # delete node by value
    def deleteNode(self, data):
        current_node = self.head
        while current_node:
            if current_node.data == data:
               print(f"delete node {data}")
               break
            elif current_node.next==self.head:
               print(f"node is not found")
            current_node = current_node.next
        current_node.next = current_node.next.next
        current_node = current_node.next

    # delete node by index
    def deleteAtIndex(self, index):
        if index == 0:
            self.head = self.head.next
            print(f"delete index node {index}")
            return

        current_node = self.head
        for i in range(index - 1):
            if current_node.next:
                current_node = current_node.next
            else:
                print(f"Index {index} out of range.")

        if not current_node.next:
            print(f"Index {index} out of range.")

        current_node.next = current_node.next.next
        print(f"delete index node {index}")

    # print DLinkedList
    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end="<->")
            current_node = current_node.next
        print("None")

if __name__ == "__main__":
    linked_list = DLinkedList()
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
    linked_list.deleteNode(9)
    linked_list.deleteAtIndex(3)
    linked_list.print_list()

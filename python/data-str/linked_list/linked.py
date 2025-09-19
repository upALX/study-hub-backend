from turtle import pos
# from node import Node

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def get_next(self):
        return self.next

    def __repr__(self) -> str:
        return self.data
    

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
       
    def __repr__(self) -> str:
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None") 

        return " -> ".join(nodes)
    
    def append(self, data):
        if not self.head:
            self.head = Node(data=data)
            return
        node = self.head
        while node.next:
            node = node.next
        node.next = Node(data=data)
    
    def add(self, data):
        node = Node(data=data)
        node.next = self.head
        self.head = node

    def insert(self, data, position):

        if position == 0:
            self.add(data=data)
        elif position == func.lenght():
            self.append(data=data)
        elif position >= 0 or postion < func.lenght():
            node = self.head
            for _ in range(position - 1):
                node = node.next
            new_node = Node(data=data)
            new_node.next = node.next
            node.next = new_node
        else:
            raise Exception("Position out of range")
        return self.__repr__()
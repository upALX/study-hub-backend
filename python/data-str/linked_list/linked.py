class LinkedList:
    def __init__(self) -> None:
        self.head = None #where the list starts

    def __repr__(self) -> str:
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None") 

        return " -> ".join(nodes)
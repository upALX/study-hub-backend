
def remove(self, data):

    if self.head is None:
        raise Exception("List is empty")
    
    if self.head.data == data:
        self.head = self.head.next
        self.size -= 1
        return self.__repr__()
    
    current_node = self.head
    preview_node = None

    #anterior muda ref para o proximo
    #proximo muda ref para o atual
    for _ in range(self.size):
        preview_node = current_node
        current_node = current_node.next
        if current_node.data == data:
            if current_node.next is None:
                self.remove_last()
                self.size -= 1
                return self.__repr__()
            
            else:
                preview_node.next = current_node.next
                current_node.next = None
                self.size -= 1
                return self.__repr__()


class Stack:
    '''
    Stack is a LIFO
    '''
    def __init__(self) -> None:
        self.items = []

    def push(self, item):
        #self.items.append(item)
        self.items = [item] + self.items
    
    def pop(self):
        if (not self.isEmpty()):
            item = self.items[0]
            self.items = self.items[1:]
            return item
            # lastElement = self.items[-1] # Save the last element to return
            # del(self.items[-1]) # remove last element
            # return lastElement
        else:
            None

    def isEmpty(self):
        return self.items == []

    def __str__(self):
        return 'Stack: ' + ', '.join(str(self.items))

    # def __repr__(self) -> str:
    #     return self.__str__()

    def printStack(self):
        print(self.items)


class Queue:
    '''
    Queue is FIFO
    '''
    def __init__(self) -> None:
        self.items = []
    
    def isEmpty(self):
        if self.items == None:
            return True
        return False
    
    def enqueue(self, item):
        self.items.insert(0, item)
        # or self.items = [item] + self.items
    
    def dequeue(self):
        if self.isEmpty():
            return None
        item = self.items[-1]
        self.items = self.items[0:-1] # -1 get last item
        return item
        #return self.items.pop()
    
    def size(self):
        return len(self.items)
    
    # def __str__(self):
    #     return 'Queue: ' + ', '.join(self.items)

    # def __repr__(self) -> str:
    #     return self.__str__()

    def display(self):
        print(self.enqueue)


# if __name__ == '__main__':
#     s = Queue()
#     s.enqueue('Latte')
#     s.enqueue('Cappu')
#     s.display()
''' Node class is a node in the linked list'''
from objects import Customer

class Node:
    def __init__(self, value):
      self.value = value
      self.next = None

''' LinkedList class is the linked list implementation'''
class LinkedList:
    def __init__(self):
      self.head = None
    
    def is_empty(self):
        return not self.head
    
    # This function add new node in the front of the linked list
    def add_to_front(self, node):
        if self.is_empty():
            self.head = node
        else:
            # Connect head with new node
            node.next = self.head
            self.head = node
    
    # This function add item to linked list
    def add(self, new_node):
        if self.is_empty():
            self.head = new_node
        else:
            # Find the last element in linked list
            last = self.head
            while last.next != None:
                last = last.next
            # Add the last node by new node
            last.next = new_node
    
    # This function search a item in linked list
    def search(self, search_value):
        if self.is_empty():
            print("Empty linked list")
            return
        # Traverse all nodes in linked list
        target = self.head
        while target != None:
            if target.value == search_value:
                print(f"The key {search_value} exists")
                break
            target = target.next
        else:
            print(f"{search_value} is not exist")
    
    # This function remove a node in linked list base on a key
    def remove(self, key):
        if self.is_empty():
            print("Empty linked list")
            return
        target_node = self.head
        prev_node = None
        while target_node.value != key:
            prev_node = target_node
            target_node = target_node.next
        
        # Connect previous node with target node
        prev_node.next = target_node.next
    
    def update(self, original_value, update_value):
        # start searching through the connected nodes to find the data we want to update
        start_n = self.head
        while(start_n != None):
            if(start_n.value == original_value):
                #if the data is found, update the node data with the updated data
                start_n.value = update_value
                print(original_value, "is updated to", update_value)
                return
            else:
                start_n = start_n.next
        print("Data not found")

    
    def __str__(self):
        list = ""
        # current is the first node in the linkedlist
        current = self.head

        while current != None:
            list += f"{current.value}" + '\n'
            current = current.next
        list += "None"
        return list

# if __name__ == '__main__':
#     c1 = Customer('Nguyen', 'Nina', '0450343022', 'Paypal')
#     c2 = Customer('Tran', 'Jim', '0450343234', 'Paypal')
#     c3 = Customer('Richy', 'Tomkinson', '13434343', 'Cash')
#     ctemp = Customer('NNguyen', 'Nina', '0450343022', 'Paypal')

#     ll = LinkedList()
#     ll.add(Node(c1))
#     ll.add(Node(c2))
#     ll.add(Node(c3))
#     print("Before")
#     print(ll)
#     # ll.search(c2)
#     # ll.remove(c2)
#     # print("After")
#     # print(ll)

#     ll.update(c1, ctemp)
#     print("After")
#     print(ll)
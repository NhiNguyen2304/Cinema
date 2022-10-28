import random


class Customer:
    def __init__(self, fname, lname, phone, payment_method, screenNo) -> None:
        self.firstname = fname
        self.lastname = lname
        self.phoneno = phone # phone number should in string formatting (leading zero, prefix)
        self.payment_method = payment_method
        self.no_of_screen = screenNo
        
    
    def __str__(self) -> str:
        return f"{self.firstname} {self.lastname}, phone: {self.phoneno}, payment: {self.payment_method}, screen number: {self.no_of_screen}"
    
    def to_string(self):
        return self.__str__()
    

    # Compare To 
    # def __lt__ (self, other):
    #     if self.firstname + " " + self.lastname > other.firstname + " " + other.lastname:
    #         return self.firstname + " " + self.lastname < other.firstname + " " + other.lastname
    #     return self.firstname + " " + self.lastname < other.firstname + " " + other.lastname

    # def __gt__ (self, other):
    #     return other.__lt__(self)

    # def __eq__ (self, other):
    #     return self.firstname + " " + self.lastname == other.firstname + " " + other.lastname

    # def __ne__ (self, other):
    #     return not self.__eq__(other)

    def isEmpty(self):
        if self == None:
            return True
        return False
    
    def compare_to (self, other):
        '''
        Descripion: compare customer lastname + firstname
        Output: _ current customer name < other cus name => -1
                _ current customer name > other cus name => 1
                _ current customer name = other cus name => 0
        '''
        current_name = f"{self.lastname + self.firstname}"
        other_name = f"{other.lastname + other.firstname}"
        if current_name < other_name:
            return -1
        if current_name == other_name:
            return 0
        else:
            return 1

    def set_no_of_screen(self, customer):
        self = customer
        self.no_of_screen += 1

    def get_no_of_screen(self):  
        return self.no_of_screen
    
    def get_first_name(self):
        return self.firstname
    
    def get_last_name(self):
        return self.lastname
    
    def get_phoneno(self):
        return self.phoneno

    def get_payment(self):
        return self.payment_method
        
# class CustomerCollection:
#     def __init__(self) -> None:
#         self.customers = []
#     def find(self, first_name, last_name):
#         query_customer = Customer(first_name, last_name, '', '', '')

#         for customer in self.customers:
#             if customer.compare_to(query_customer) == 0:
#                 return customer.phoneno, customer.no_of_screen
#         return None, None
#     def insert(self, Customer):
#         self.customers.append(Customer)
    
#     # def insert_existing(self, ob_customer):
#     #     self.customers.add(Node(ob_customer))
#     def delete(self, first_name, last_name):
#         query_customer = Customer(first_name, last_name, '', '','')
#         #customer_idx = 0
#         for i, customer in enumerate(self.customers):
#             if customer.compare_to(query_customer) == 0:
#                 del self.customers[i]
#                 return None

#             #customer_idx += 1
#     # def delete(self, phoneNo):
#     #    self.customers.remove(phoneNo)
    
#     def display(self):
#         for customer in self.customers:
#             print(customer)

#     # def sort(self, algorithm='bubble'):
#     #     if algorithm == 'bubble':
#     #         self.bubble_sort()
#     #     if algorithm == 'selection':
#     #         self.selection_sort()
#     #     if algorithm == 'insertion':
#     #         self.insertion_sort()

#     def insertion_sort(self):
#         for i in range(1, len(self.customers) - 1 + 1):
#             v = self.customers[i]
#             j = i - 1
#             while j >= 0 and self.customers[j].compare_to(v) == 1:
#                 self.customers[j + 1] = self.customers[j]
#                 j = j - 1
#             self.customers[j + 1] = v  
    
#     # def selection_sort(self):
#     #     for i in range(0, len(self.customers) - 2 + 1):
#     #         small = i
#     #         for j in range(i + 1, len(self.customers) - 1 + 1):
#     #             if self.customers[j].compare_to(self.customers[small]) == -1:
#     #                 small = j
#     #         temp = self.customers[i]
#     #         self.customers[i] = self.customers[small]
#     #         self.customers[small] = temp
#     #         #(self.customers[i], self.customers[small]) = (self.customers[small], self.customers[i])
    
#     # def bubble_sort(self):
#     #     for i in range(0, len(self.customers) - 2 + 1):
#     #         for j in range(1, len(self.customers) - 2 - i):
#     #             if self.customers[j + 1].compare_to(self.customers[j] == -1):
#     #                 #swapped = True
#     #                 temp = self.customers[j]
#     #                 self.customers[j] = self.customers[j + 1]
#     #                 self.customers[j + 1] = temp
#     #                 #arr[j], arr[j + 1] = arr[j + 1], arr[j]
#     #         # if not swapped:
#     #         #     return

# if __name__ == '__main__':
#     c1 = Customer('Nina', 'Nguyen','0450343022', 'Paypal', random.randint(0,10))
#     c2 = Customer('Jim', 'Tran', '0450343234', 'Paypal', random.randint(0,10))
#     c3 = Customer('Richy', 'Tomkinson', '13434343', 'Cash', random.randint(0,10))
#     ctemp = Customer('Nina', 'NNguyen','0450343022', 'Paypal', random.randint(0,10))

#     ll = CustomerCollection()
#     ll.insert(c1)
#     ll.insert(c2)
#     ll.insert(c3)
#     ll.insert(ctemp)

#     # ll.add(Node(c1))
#     # ll.add(Node(c2))
#     # ll.add(Node(c3))
#     print("Before")
#     ll.display()
#     ll.delete('Nina', 'NNguyen')
#     # ll.search(c2)
#     # ll.remove(c2)
#     # print("After")
#     # print(ll)

#     # ll.update(c1, ctemp)
#     print("After")
#     ll.display()
#     print(ll.find('Jimsd', 'Tran'))
from linkedlist import LinkedList, Node

class Customer:
    def __init__(self, lname, fname, phone, payment_method) -> None:
        self.lastname = lname
        self.firstname = fname
        self.phoneno = phone # phone number should in string formatting (leading zero, prefix)
        self.payment_method = payment_method
        #self.no_of_screen += 1
        
    
    def __str__(self) -> str:
        return f"{self.firstname} {self.lastname}, phone: {self.phoneno}, payment: {self.payment_method}"
    
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
    
    def compare_to (self, other):
        current_name = f"{self.lastname + self.firstname}"
        other_name = f"{other.lastname + other.firstname}"
        if current_name < other_name:
            return -1
        if current_name > other_name:
            return 1
        else:
            return 0

class CustomerCollection:
    def __init__(self) -> None:
        self.customers = LinkedList()
    def find(self, first_name, last_name):
        query_customer = Customer(first_name, last_name, '')

        for customer in self.customers:
            if customer.compare_to(query_customer) == 0:
                return customer.phoneno
    
    def insert(self, first_name, last_name, phoneno, payment_method):
        self.customers.add(Node(Customer(first_name, last_name, phoneno, payment_method)))
    
    def insert_existing(self, ob_customer):
        self.customers.add(Node(ob_customer))
    
    def delete(self, phoneNo):
       self.customers.remove(phoneNo)
    
    def display(self):
        print(self.customers)

    def sort(self, algorithm='bubble'):
        if algorithm == 'bubble':
            self.bubble_sort()
        if algorithm == 'selection':
            self.selection_sort()
        if algorithm == 'insertion':
            self.insertion_sort()

    def insertion_sort(self):
        for i in range(1, len(self.customers) - 1 + 1):
            v = self.customers[i]
            j = i - 1
            while j >= 0 and self.customers[j].compare_to(v) == 1:
                self.customers[j + 1] = self.customers[j]
                j = j - 1
            self.customers[j + 1] = v  
    
    def selection_sort(self):
        for i in range(0, len(self.customers) - 2 + 1):
            small = i
            for j in range(i + 1, len(self.customers) - 1 + 1):
                if self.customers[j].compare_to(self.customers[small]) == -1:
                    small = j
            temp = self.customers[i]
            self.customers[i] = self.customers[small]
            self.customers[small] = temp
            #(self.customers[i], self.customers[small]) = (self.customers[small], self.customers[i])
    
    def bubble_sort(self):
        for i in range(0, len(self.customers) - 2 + 1):
            for j in range(1, len(self.customers) - 2 - i):
                if self.customers[j + 1].compare_to(self.customers[j] == -1):
                    #swapped = True
                    temp = self.customers[j]
                    self.customers[j] = self.customers[j + 1]
                    self.customers[j + 1] = temp
                    #arr[j], arr[j + 1] = arr[j + 1], arr[j]
            # if not swapped:
            #     return

if __name__ == '__main__':
    c1 = Customer('Nguyen', 'Nina', '0450343022', 'Paypal')
    c2 = Customer('Tran', 'Jim', '0450343234', 'Paypal')
    c3 = Customer('Richy', 'Tomkinson', '13434343', 'Cash')
    ctemp = Customer('NNguyen', 'Nina', '0450343022', 'Paypal')

    ll = CustomerCollection()

    ll.insert('Nguyen', 'Nina', '0450343022', 'Paypal')
    ll.insert('Tran', 'Jim', '0450343234', 'Paypal')
    ll.insert('Richy', 'Tomkinson', '13434343', 'Cash')
    # ll.add(Node(c1))
    # ll.add(Node(c2))
    # ll.add(Node(c3))
    print("Before")
    ll.display()
    ll.delete(c1)
    # ll.search(c2)
    # ll.remove(c2)
    # print("After")
    # print(ll)

    # ll.update(c1, ctemp)
    print("After")
    ll.display()
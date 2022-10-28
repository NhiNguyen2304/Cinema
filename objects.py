class Customer:
    def __init__(self, lname, fname, phone, payment_method, screen) -> None:
        self.lastname = lname
        self.firstname = fname
        self.phoneno = phone # phone number should in string formatting (leading zero, prefix)
        self.payment_method = payment_method
        self.no_of_screen = screen
        
    
    def __str__(self) -> str:
        return f"{self.firstname} {self.lastname}, phone: {self.phoneno}, payment: {self.payment_method}"
    
    def to_string(self):
        return self.__str__()
    

    # Compare To 
    def __lt__ (self, other):
        if self.firstname + " " + self.lastname > other.firstname + " " + other.lastname:
            return self.firstname + " " + self.lastname < other.firstname + " " + other.lastname
        return self.firstname + " " + self.lastname < other.firstname + " " + other.lastname

    def __gt__ (self, other):
        return other.__lt__(self)

    def __eq__ (self, other):
        return self.firstname + " " + self.lastname == other.firstname + " " + other.lastname

    def __ne__ (self, other):
        return not self.__eq__(other)
    
    def compare_to (self, other):
        current_name = f"{self.lastname + self.firstname}"
        other_name = f"{other.lastname + other.firstname}"
        if current_name < other_name:
            return -1
        if current_name > other_name:
            return 1
        else:
            return 0

    def get_no_of_screen(self):  
        return self.no_of_screen
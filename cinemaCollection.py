import random
from customize_collections import Queue
from customer import Customer


class Cinema:
    capacity = 5
    def __init__(self):
        # cinema fix capacity
        self.seat = []
        self.capacity = 10

    def __str__(self) -> str:
        return f"Cinema is displaying movie (capacity: {self.capacity})"

    def add_customer(self, Customer):
        for i in range(self.capacity):
            self.seat.append(Customer)


class LineCollection:
    def __init__(self) -> None:
        self.waiting_line = Queue()
    
    def add_to_line(self, Customer):
        self.waiting_line.enqueue(Customer)
    
    def display_waiting_line(self):
        index = 0
        print(self.waiting_line.items.__str__())
        # for x in self.waiting_line.items:
        #     index += 1
        #     print(f'Waiting line {index}: {x}')

    def pick_customer(self):
        customer = self.waiting_line.dequeue()
        print(f'Serving customer: {customer}')
        return customer
    
    def clear_line(self):
        self.waiting_line = Queue()

# if __name__ == '__main__':
#     cinema = Cinema()
#     cinema_capacity = 5

#     # TODO: initial 2 type of Customer: customer in DB, customer in waiting queue
#     # customer in waiting: + 1 no of screen, already saved customer: random no of screen
#     c0 = Customer('Nina', 'Nguyen','0450343022', 'Paypal', random.randint(1, 10))
#     c1 = Customer('Jim', 'Tran', '0450343234', 'Paypal', random.randint(1, 10))
#     c2 = Customer('Richy', 'Tomkinson', '13434343', 'Cash', random.randint(1, 10))
#     c3 = Customer('Nina', 'NNguyen','0450343022', 'Paypal', 9)

#     c4 = Customer('Coco', 'Tran','34234545454', 'Paypal', 0)

#     line = LineCollection()

#     # Demonstrate customer already in cinema database
#     customers = CustomerCollection()
#     customers.insert(c0)
#     customers.insert(c1)
#     customers.insert(c2)
#     customers.insert(c3)

#     # names = ['a','b']
#     # for name in names:
#     #     globals()[name] = 0

#     # for i in range(10):
#     #     globals()['variable{}'.format(i)] = 0

#     # for i in range(cinema_capacity):
#     #     line.add_to_line(globals()['c{}'.format(i)])


#     # Demonstrate for customer in line (with 0 no_of_screen)
#     wc0 = Customer('Nina', 'Nguyen','0450343022', 'Paypal', 0)
#     wc1 = Customer('Jim', 'Tran', '0450343234', 'Paypal', 0)
#     wc2 = Customer('Richy', 'Tomkinson', '13434343', 'Cash', 0)
#     wc3 = Customer('Nina', 'NNguyen','0450343022', 'Paypal', 0)
#     wc4 = Customer('Coco', 'Tran','34234545454', 'Paypal', 0)

#     line.add_to_line(wc4)
#     line.add_to_line(wc0)
#     line.add_to_line(wc1)
#     line.add_to_line(wc2)
#     line.add_to_line(wc3)
    
#     #line.display_waiting_line()

#     # Servicing customers with cinema capacity
#     for i in range(cinema.capacity):
#         customer_in_queue = line.pick_customer()

#         # Check if customer is new customer or not
#         # If customer is new customer => insert into current customer list
#         # If customer already in database => add to cinema
#         phoneNo, no_of_screen = customers.find(customer_in_queue.get_first_name(), customer_in_queue.get_last_name())
#         if (phoneNo == None):
#             print(f'New customer: {customer_in_queue.get_first_name()}')
#             customers.insert(customer_in_queue)
#         else:
#             if no_of_screen == 9:
#                 print(f'Congrat!!! Customer: {customer_in_queue} has a free ticket after 10 screenings')
#         cinema.seat.append(customer_in_queue)
#         # Check if customer has 10 screens to get a free tickets.
#         # if customers.get_no_of_screen() == 9:
#         #     print(f'Congrat!!! Customer: {customer_in_queue} has a free ticket after 10 screenings')
    

        
    
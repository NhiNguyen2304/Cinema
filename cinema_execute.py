from os import getcwd
import random
import csv
from cinemaCollection import LineCollection, Cinema
from customerCollection1 import Customer
from binary_search_tree import BTree
from moviesCollection import MovieCollection, Movie


def prepare_db_data():
    '''
    Description: This function is used to generate cinema database
                _ Load sample DB cinema customers by csv file (db.csv)
    Output: return database customers in binary search tree  
    '''
    c0 = Customer('Nina', 'Nguyen','0450343022', 'Paypal', 9)

    # inital binary search tree with root
    db_customer = BTree(c0)

    # Db csv file with 1000 rows
    with open('db.csv', newline='') as csv_file:
        reader = csv.reader(csv_file)
        next(reader, None)  # Skip the header.
        # Unpack the row directly in the head of the for loop.
        for fname, lname, phone, payment_method, screenNo in reader:
            # Convert the numbers to floats.
            fname = fname
            lname = lname
            phone = phone
            payment_method = payment_method
            screenNo = screenNo
            # Now create the Student instance and append it to the list.
            db_customer.insert(Customer(fname, lname, phone, payment_method, screenNo))
    
    return db_customer
    
def prepare_waiting_line():
    '''
    Description: This function is used to generate customers in wait in line to be served
                _ Load sample_waiting_line.csv to get customers in wait list
                _ Use Queue data structure to push customer with rule: First In First Out
    Output: return customer in line queue
    '''
    waiting_line = LineCollection()

    # Read customers from sample waitingLine csv
    with open('sample_waiting_line.csv', newline='') as csv_file:
        reader = csv.reader(csv_file)
        next(reader, None)  # Skip the header.
        # Unpack the row directly in the head of the for loop.
        for fname, lname, phone, payment_method, screenNo in reader:
            # Convert the numbers to floats.
            fname = fname
            lname = lname
            phone = phone
            payment_method = payment_method
            screenNo = screenNo
            # Now create the Student instance and append it to the list.
            waiting_line.add_to_line(Customer(fname, lname, phone, payment_method, 0))

    return waiting_line

def bind_object(customer):
    '''
    Description: This method plus 1 into served customer no of screen
    '''
    fname = customer.get_first_name()
    lname = customer.get_last_name()
    phone = customer.get_phoneno()
    pMethod = customer.get_payment()
    screen_no = customer.get_no_of_screen()
    screen_no += 1
    return Customer(fname, lname, phone, pMethod, screen_no)

def serve_customer(cinema, db_customer, customer_queue):

    cinema = Cinema()
    # Servicing customers with cinema capacity
    for i in range(cinema.capacity):
        customer_in_queue = customer_queue.pick_customer()

        # Check if customer is new customer or not
        # If customer is new customer => insert into current customer list
        # If customer already in database => add to cinema
        found_customer = db_customer.search(Customer(customer_in_queue.get_first_name(), customer_in_queue.get_last_name(), '', '', ''))
        
        # New customer case
        if (found_customer == None):
            print(f'New customer: {customer_in_queue.get_first_name()}. Please add this customer into Cinema DB')
            #customer_in_queue = customer_in_queue.set_no_of_screen()
            print(f'Customer screen: {customer_in_queue.get_no_of_screen() + 1}')
            
            
            # Prepare for customer object before insert into db
            binded_cus = bind_object(customer_in_queue)
            print(f'Add this new customer: {customer_in_queue.get_first_name()} >> to DB')
            print("")
            db_customer.insert(binded_cus)
            cinema.seat.append(binded_cus)
        # Customer already in DB case
        else:
            if found_customer.get_no_of_screen() == cinema.capacity - 1:
                print(f'Congrat!!! Customer: {customer_in_queue} has a free ticket after 10 screenings')
            # else:
            #     print('Update customer no of screening, information')
            
            print('Update customer no of screening')
            binded_cus = bind_object(found_customer)
            cinema.seat.append(binded_cus)
            print("")

    # If the movie is sold out, all customers are told to leave
    print("Movie's ticket is sold out! Please comeback tomorrow!")
    print("")
    customer_queue.clear_line()
    return cinema

def remove_customer(customer_tree, customer):
    customer_tree.delete(customer)

if __name__ == '__main__':
    print(getcwd())
    db_customer = prepare_db_data()
    customer_queue = prepare_waiting_line()

    cinema = Cinema()
    serving_cinema = serve_customer(cinema, db_customer, customer_queue)

    #Simulate receive new movies at random times,
    movies = MovieCollection()

    # copy for favourite movie
    fav_movie = Movie('Titanic', 200)

    #inital movie list with some movies
    m2 = Movie("Spider men", 135)
    m3 = Movie("Avatar", 225)
    movies.insert(m2)
    movies.insert(m3)

    # Random receive movie (use random generates a number from 0 => 3.)
    if random.randint(0,3) == 3:
        m1 = Movie('Normal people', 120)
        movies.insert(m1)
    else:
        movies.insert(fav_movie)
        

    print("")
    print("######################################################################")
    print(f'Cinema is displaying {movies.displayMovie()} minutes. With customers:')
    for cus in serving_cinema.seat:
        print(cus)
    
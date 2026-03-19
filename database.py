import csv
from customer import Customer

class CustomerDatabase:
    def __init__(self):
        self.customers = []       #list to store customer details 

    def add_customer(self, customer):
        self.customers.append(customer)    #add to the list 

    def save_to_csv(self, filename):                         #save customers to csv
        with open(filename, "w", newline="") as file:  
            writer = csv.writer(file)

            writer.writerow(["name", "phone_number", "plan"])          #write header

            for customer in self.customers:
                writer.writerow([customer.name, customer.phone_number, customer.plan])    #write each customer
    
    def load_from_csv(self, filename):               #load customer from csv
        self.customers = []               #clear list for no duplications

        with open(filename, "r") as file:               #read mode
            reader = csv.reader(file)                   #reads each row
            next(reader)       #skips the header row

            for row in reader:
                name, phone_number, plan = row
                customer = Customer(name, phone_number, plan)    #creates a customer object from file 
                
                self.customers.append(customer)       #add to list


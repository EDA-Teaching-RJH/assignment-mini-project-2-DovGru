import csv

class CustomerDatabase:
    def __init__(self):
        self.customer = []       #list to store customer details 

    def add_customer(self, customer):
        self.customer.append(customer)    #add to the list 

    def save_to_csv(self, filename):                         #save customers to csv
        with open(filename, "w", newline="") as file:  
            writer = csv.writer(file)

            writer.writerow(["name", "phone_number", "plan"])          #write header

            for customer in self.customers:
                writer.wrterow([customer.name, customer.phone_number, customer.plan])    #write each customer
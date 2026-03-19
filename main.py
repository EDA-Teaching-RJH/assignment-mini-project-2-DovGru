from customer import Customer
from database import CustomerDatabase

db = CustomerDatabase()

while True:
    print("\nEE Customer Management System")
    print("1. Display Customer")
    print("2. Add Customer")
    print("3. Save to database")
    print("4. Load from database")
    print("5. Exit")

    choice = input("Choose an option from above: ")

    if choice == "1":                        #option 1 display customers
        if len(db.customers) == 0:
            print("No customers found.")
        else:
            for customer in db.customers:
                print(customer)

    elif choice == "2":                                     #option 2 add a customer
        name = input("Enter customer's name: ")
        phone_number = input("Enter phone number: ")
        plan = input("Enter plan (SIMO, PAYM, PAYG): ")

        try:                                                #error handling
            customer = Customer(name, phone_number, plan)
            db.add_customer(customer)
            print("Customer added successfully.")
        except ValueError as e:
            print("Error:", e)

    elif choice == "3":                       #save to csv
        db.save_to_csv("customers.csv")
        print("Customer saved to file.")

    elif choice == "4":                       #load from csv
        db.load_from_csv("customers.csv")
        print("Customers loaded from file.")

    elif choice == "5":                     #exit program
        print("Closing program down...")
        break

    else:                                   #invalid option
        print("Invalid choice, please select from the given option in the menu.")

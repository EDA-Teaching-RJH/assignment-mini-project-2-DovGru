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
from validator import is_valid_name, is_valid_phone, is_valid_plan

class Customer:                      #constructor with class to create a new customer object 
    def __init__(self, name, phone_number, plan):
        if not is_valid_name(name):                
            raise ValueError("Invalid name")       #validation, cant be empty 
        
        if not is_valid_phone(phone_number):
            raise ValueError("Invalid phone number")     #follow UK number format validation using regex
        
        if not is_valid_plan(plan):
            raise ValueError("Invalid plan")        #check its in the plans list 
        
        self.name = name                         #assign values to the object
        self.phone_number = phone_number
        self.plan = plan 

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone_number}, Plan: {self.plan}"      #display info

class PayMonthlyCustomer(Customer):                     #subclass for PAYM customer inherits from customer
    def __init__(self, name, phone_number, plan, contract_length):
        super().__init__(name, phone_number, plan)                #use parent class constructor for the details already there 

        self.contract_lenght = contract_length               #additional attribute
    
    def __str__(self):
        return f"{super().__str__()}, Contract: {self.contract_length} months"             #include contract length
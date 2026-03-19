import re 

def is_valid_name(name):
    return name.strip() != ""          #strip spaces and make sure there is not empty name.

def is_valid_phone(phone_number):
    phone_format = r"^07\d{9}$"                 #UK phone number style 
    return re.match(phone_format, phone_number) is not None

def is_valid_plan(plan):
    valid_plans = ["SIMO", "PAYM", "PAYG"]    #EE plan types
    return plan in valid_plans

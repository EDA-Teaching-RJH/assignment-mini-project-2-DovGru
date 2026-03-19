import pytest
from customer import Customer

def test_create_customer():
    customer = Customer("Jeff", "07223675907", "SIMO")                 #create customer and check values were store properly

    assert customer.name == "Jeff"
    assert customer.phone_number == "07223675907"
    assert customer.plan == "SIMO"

def test_customer_str():
    customer = Customer("Jeff", "07223675907", "SIMO")

    assert str(customer) == "Name: Jeff, Phone: 07223675907, Plan: SIMO"

def test_invalid_name():
    with pytest.raises(ValueError):
        Customer("", "07223675907", "SIMO")

def test_invalid_phone():
    with pytest.raises(ValueError):
        Customer("Jeff", "3445", "SIMO")

def test_invalid_plan():
    with pytest.raises(ValueError):
        Customer("Jeff", "07223675907", "PHONE")
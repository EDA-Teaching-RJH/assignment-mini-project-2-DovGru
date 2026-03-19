from validator import is_valid_name, is_valid_phone, is_valid_plan

def test_valid_name():
    assert is_valid_name("Jeff") == True

def test_empty_name():
    assert is_valid_name("") == False

def test_spaces_name():
    assert is_valid_name("    ") == False

def test_valid_phone():
    assert is_valid_phone("07333444555") == True

def test_invalid_phone_short():
    assert is_valid_phone("07555") == False

def test_invalid_phone_start():
    assert is_valid_phone("09888333222") == False

def test_valid_plan():
    assert is_valid_plan("SIMO") == True

def test_invalid_plan():
    assert is_valid_plan("PAYMONTHLY") == False
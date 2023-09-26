from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    assert make_full_name("Sally", "Brown") == "Brown; Sally"
    assert make_full_name("John", "Smith") == "Smith; John"
    assert make_full_name("Jane", "Doe") == "Doe; Jane"

def test_extract_family_name():
    assert extract_family_name("Brown; Sally") == "Brown"
    assert extract_family_name("Smith; John") == "Smith"
    assert extract_family_name("Doe; Jane") == "Doe"

def test_extract_given_name():
    assert extract_given_name("Brown; Sally") == "Sally"
    assert extract_given_name("Smith; John") == "John"
    assert extract_given_name("Doe; Jane") == "Jane"

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])

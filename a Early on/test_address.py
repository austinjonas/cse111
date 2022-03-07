from address import extract_city, extract_state, extract_zipcode
import pytest

def test_extract_city():
    extract_city("street, city, state") == "city"

def test_extract_state():
    extract_state("street, city, state") == "state"

def test_extract_zip_code():
    extract_zipcode("state, city, street, zip") == "zip"


pytest.main(["-v", "--tb=line", "-rN", __file__])
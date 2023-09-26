from names import make_full_name, extract_given_name, extract_family_name

import pytest

def test_make_full_name():

    assert make_full_name("Flavia", "Bezerra") == "Bezerra; Flavia"
    assert make_full_name("Juan", "Perez") == "Perez; Juan" 
    assert make_full_name("Jessica", "Raposo") == "Raposo; Jessica"
    #assert make_full_name(Flavia, Bezerra)=="Bezerra;Flavia"

def test_extract_family_name():

    assert extract_family_name("Bezerra; Flavia") == "Bezerra"

pytest.main(["-v", "--tb=line", "-rN", __file__])
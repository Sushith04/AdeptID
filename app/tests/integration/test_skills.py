#Integration testing for reverse string
import pytest
from app.app import app

#The list_send_text below is a list of all inputs
list_send_text = ["asd", "ada23112", "#$$FD99", "res eg\'78y56", "78t i\"ju';", ".;'p[mo8.;[", "", "134;..452@!@#$%^&*(", b"7878dsbh4;.qd4", 798]
#The list_expected_text below is a list of all expected outputs
list_expected_text = ["dsa", "21132ada", "99df$$#", "65y87'ge ser", ";'uj\"i t87", "[;.8om[p';.", "", "(*&^%$#@!@254..;431", b"4dq.;4hbsd8787", 897]

#Helper function that returns the actual and expected values
def send_request(app, send_text, data_rev):
    json_send = {"skill_title": send_text}
    actual = app.test_client().post('/skills/reverse-skill-title', json=json_send)
    expected = {"skill_title" : send_text, "reversed_skill_title": data_rev}
    return actual.json, expected

#This asserts the actual and expected values
@pytest.mark.parametrize('send_text, data_rev', list(zip(list_send_text[:-2], list_expected_text[:-2])))          
def test_integration_reverse_string(app, send_text, data_rev):
    actual, expected = send_request(app, send_text, data_rev)
    assert actual == expected

#This asserts the JSON type error
def test_integration_bytes_string_error():
    error_text = "Object of type bytes is not JSON serializable"
    try:
        actual, expected = send_request(app, list_send_text[8], list_expected_text[8])
    except Exception as error_:
        print(error_)
        assert error_text == str(error_)

#This asserts the int type error
def test_integration_int_error():
    error_text = "'int' object is not subscriptable"
    try:
        actual, expected = send_request(app, list_send_text[9], list_expected_text[9])
    except Exception as error_:
        assert error_text == str(error_)
from app.services import skills_service
import pytest

list_send_text = ["asd", "ada23112", "#$$FD99", "res eg\'78y56", "78t i\"ju';", ".;'p[mo8.;[", "", b"7878dsbh4;.qd4", 798]
list_expected_text = ["dsa", "21132ada", "99df$$#", "65y87'ge ser", ";'uj\"i t87", "[;.8om[p';.", "", b"4dq.;4hbsd8787", 897]

def send_request(send_text, data_rev):
    actual = skills_service.reverse_skill_title(send_text)
    expected = {"skill_title" : send_text, "reversed_skill_title": data_rev}
    return actual, expected
            
@pytest.mark.parametrize('send_text, data_rev', list(zip(list_send_text[:-1], list_expected_text[:-1])))
def test_reverse_string(send_text, data_rev):
    actual, expected = send_request(send_text, data_rev)
    assert actual == expected

def test_int_error():
    error_text = "'int' object is not subscriptable"
    try:
        actual, expected = send_request(list_send_text[8], list_send_text[8])
    except Exception as error_:
        assert error_text == str(error_)
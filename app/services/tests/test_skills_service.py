from app.services import skills_service
import pytest

list_send_text = ["asd", "ada23112", "#$$FD99", "res eg\'78y56", "78t i\"ju';", b"7878dsbh4;.qd4", ".;'p[mo8.;[", "", 798]

def send_req(send_text) -> None:
    actual = skills_service.reverse_skill_title(send_text)
    data_rev = send_text[::-1].lower()
    expected = {"skill_title" : send_text, "reversed_skill_title": data_rev}
    return actual, expected
            
def test_case_1():
    actual, expected = send_req(list_send_text[0])
    assert actual == expected

def test_case_2():
    actual, expected = send_req(list_send_text[1])
    assert actual == expected

def test_case_3():
    actual, expected = send_req(list_send_text[2])
    assert actual == expected

def test_case_4():
    actual, expected = send_req(list_send_text[3])
    assert actual == expected

def test_case_5():
    actual, expected = send_req(list_send_text[4])
    assert actual == expected

def test_case_6():
    actual, expected = send_req(list_send_text[5])
    assert actual == expected

def test_case_7():
    actual, expected = send_req(list_send_text[6])
    assert actual == expected

def test_case_8():
    actual, expected = send_req(list_send_text[7])
    assert actual == expected

def test_case_9():
    error_text = "'int' object is not subscriptable"
    try:
        actual, expected = send_req(list_send_text[8])
    except Exception as error_:
        assert error_text == str(error_)

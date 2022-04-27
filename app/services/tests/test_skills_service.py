from app.services import skills_service

def send_req(send_text) -> None:
    actual = skills_service.reverse_skill_title(send_text)
    data_rev = send_text[::-1].lower()
    expected = {"skill_title" : send_text, "reversed_skill_title": data_rev}
    assert actual == expected

def test_reverse_skill_title():
    count = 0
    error_text = "'int' object is not subscriptable"
    list_send_text = ["asd", "ada23112", "#$$FD99", "reseg78y56", "78t iju';", "7878dsbh4;.qd4", ".;'p[mo8.;[", "", 798]
    for send_text in list_send_text:
        try:
            send_req(send_text)
            count = count+1
            print("Test", count, "passed")
        except Exception as error:
            assert error_text == str(error)
            print("Error test passed")
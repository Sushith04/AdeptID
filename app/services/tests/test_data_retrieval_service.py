from app.services.data_retrieval_service import DataRetrieval
import json

data_retrieval_service_object = DataRetrieval()
with open('tests_data_unit.json','r',encoding='UTF-8') as fp:    
    tests_list = json.load(fp)['test_data']

def send_req(query: dict) -> None:
    return data_retrieval_service_object.get_data_query(query)
       
        
def test_case_d1():
    assert send_req(tests_list[0][0]) == tests_list[0][1]

def test_case_d2():
    assert send_req(tests_list[1][0]) == tests_list[1][1]

def test_case_d3():
    assert send_req(tests_list[2][0]) == tests_list[2][1]

def test_case_d4():
    assert send_req(tests_list[3][0]) == tests_list[3][1]

def test_case_d5():
    assert send_req(tests_list[4][0]) == tests_list[4][1]

def test_case_d6():
    assert send_req(tests_list[5][0]) == tests_list[5][1]

def test_case_d7():
    assert send_req(tests_list[6][0]) == tests_list[6][1]

def test_case_d8():
    assert send_req(tests_list[7][0]) == tests_list[7][1]

def test_case_d9():
    assert send_req(tests_list[8][0]) == tests_list[8][1]

def test_case_d10():
    assert send_req(tests_list[9][0]) == tests_list[9][1]

def test_case_d11():
    assert send_req(tests_list[10][0]) == tests_list[10][1]

def test_case_d12():
    assert send_req(tests_list[11][0]) == tests_list[11][1]

def test_case_d13():
    assert send_req(tests_list[12][0]) == tests_list[12][1]

def test_case_d14():
    assert send_req(tests_list[13][0]) == tests_list[13][1]

def test_case_d15():
    assert send_req(tests_list[14][0]) == tests_list[14][1]

def test_case_d16():
    assert send_req(tests_list[15][0]) == tests_list[15][1]

def test_case_d17():
    assert send_req(tests_list[16][0]) == tests_list[16][1]

def test_case_d18():
    assert send_req(tests_list[17][0]) == tests_list[17][1]

def test_case_d19():
    assert send_req(tests_list[18][0]) == tests_list[18][1]

def test_case_d20():
    assert send_req(tests_list[19][0]) == tests_list[19][1]

def test_case_d21():
    assert send_req(tests_list[20][0]) == tests_list[20][1]

def test_case_d22():
    assert send_req(tests_list[21][0]) == tests_list[21][1]

def test_case_d23():
    assert send_req(tests_list[22][0]) == tests_list[22][1]

def test_case_d24():
    assert send_req(tests_list[23][0]) == tests_list[23][1]

def test_case_d25():
    assert send_req(tests_list[24][0]) == tests_list[24][1]


from app.services.data_retrieval_service import DataRetrieval
import pytest
import json

data_retrieval_service_object = DataRetrieval()
with open('tests_data_unit.json','r',encoding='UTF-8') as fp:    
    tests_list = json.load(fp)['test_data']

def send_request(query: dict):
    
    return data_retrieval_service_object.get_data_query(query)
       
@pytest.mark.parametrize('actual, expected', tests_list)
def test_data_retrieval(actual, expected):
    assert send_request(actual) == expected
from app.services.data_retrieval_service import DataRetrieval
import json
import pytest

data_retrieval_service_object = DataRetrieval()
with open('tests_data_integration.json','r',encoding='UTF-8') as fp:    
    tests_list = json.load(fp)['test_data']

def send_req(app, query: dict):
    return app.test_client().post('/api/get-employment-count', json=query).json
       
@pytest.mark.parametrize('actual, expected', tests_list)  
def test_integration_data_retrieval(app, actual, expected):
    assert send_req(app, actual) == expected
    
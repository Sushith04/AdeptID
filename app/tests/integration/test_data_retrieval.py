#Integration testing for data retrieval service
from app.services.data_retrieval_service import DataRetrieval
import json
import pytest

#The tests_list below is a json file which holds all the inputs and expected outputs
data_retrieval_service_object = DataRetrieval()
with open('tests_data_integration.json','r',encoding='UTF-8') as fp:    
    tests_list = json.load(fp)['test_data']

#Helper function that returns the actual value
def send_req(app, query: dict):
    return app.test_client().post('/api/get-employment-count', json=query).json
       
#This asserts the actual and expected values
@pytest.mark.parametrize('actual, expected', tests_list)  
def test_integration_data_retrieval(app, actual, expected):
    assert send_req(app, actual) == expected
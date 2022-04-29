#Unit testing for data retrieval service
from app.services.data_retrieval_service import DataRetrieval
import pytest
import json

#The tests_list below is a json file which holds all the inputs and expected outputs
data_retrieval_service_object = DataRetrieval()
with open('tests_data_unit.json','r',encoding='UTF-8') as fp:    
    tests_list = json.load(fp)['test_data']

#Helper function that returns the actual value
def send_request(query: dict):
    return data_retrieval_service_object.get_data_query(query)
       
#This asserts the actual and expected values
@pytest.mark.parametrize('actual, expected', tests_list)        
def test_data_retrieval(actual, expected):
    return_value = send_request(actual)
    return_value = return_value if(type(return_value)==dict) else return_value.json
    assert return_value == expected
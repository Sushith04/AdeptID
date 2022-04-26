import json
import csv

class DataRetrieval(object):
    def __init__(self):
        self.data_json = {}
        self.data_json_cities = {}        
        self.get_data_json()

    """ Here we convert the data from CSV file to a JSON file to access the data easily and fast """
    def get_data_json(self) -> None:
        fp = open('data.csv', 'r', encoding='UTF-8')
        cr = csv.reader(fp, delimiter=',')
        
        for row in list(cr.__iter__())[1:]:
            if(not self.data_json.get(row[2], None)):
                self.data_json[row[2]] = {"name":row[3],"emp":{}}
            try:
                emp_cnt = int(row[4],10) if(row[4]) else 0  
            except:
                emp_cnt = 0
            self.data_json[row[2]]["emp"][int(row[0],10)] = emp_cnt
            if(not self.data_json_cities.get(row[1]), None):
                self.data_json_cities[row[1]] = int(row[0],10)
        fp.close()
        fp = open('employment.json','w', encoding='UTF-8')
        json.dump(self.data_json, fp, indent=4)
        fp.close()

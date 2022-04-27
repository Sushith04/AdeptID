import json
import csv

class DataRetrieval(object):
    def __init__(self):
        self.data_json = {}
        self.data_json_cities = {}        
        self.get_data_json()
        self.data_json_cities_rev = {value:key for key, value in self.data_json_cities.items()}

    #Here we convert the data from CSV file to a JSON file to access the data easily and fast
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
        # This code is used to show how the converted JSON file looks
        # fp = open('employment.json','w', encoding='UTF-8')
        # json.dump(self.data_json, fp, indent=4)
        # fp.close()

    #Checks whether the city input is empty, valid or not valid
    def check_city(self, city_name: str) -> bool:
        return False if(city_name == '' or not self.data_json_cities.get(city_name, None)) else True
        
    #Checks whether the OCC_Code input is empty, valid or not valid
    def check_occ(self, occ_code: str) -> bool:
        return False if(occ_code == '' or not self.data_json.get(occ_code, None)) else True

    #Returns data if only the city name is given and is valid
    def get_city_data(self, city_name:str, city_code: int) -> dict:
        ret = {city_name : []}
        for val in self.data_json.values():
            try:
                ret[city_name].append({"job": val['name'], "employment_count": val['emp'][city_code]})
            except:
                pass
        return ret
    
    #Returns data if only the OCC_Code is given and is valid
    def get_occ_data(self, occ_code: str) -> dict:
        extract_occ = self.data_json[occ_code]
        ret = {}
        for emp_ in extract_occ['emp'].keys():
            ret[self.data_json_cities_rev[emp_]] = []
            ret[self.data_json_cities_rev[emp_]].append({"job": extract_occ['name'], "employment_count": extract_occ['emp'][emp_]})
        return ret
    
    #Returns data if both city name and OCC_Code are given and are valid
    def get_city_occ_data(self, city_code: int, occ_code: str) -> dict:
        extract_occ = self.data_json[occ_code]
        try:
            return {self.data_json_cities_rev[city_code]: [{"job": extract_occ['name'], "employment_count": extract_occ['emp'][city_code]}]} 
        except:
            raise Exception("Data Does Not Exist")
      
    #The query will be passed here to retrieve the data
    def get_data_query(self, query) -> dict:
        try:
            city_value = query.get('city', '') 
            occ_value = query.get('occ_code', '') 
            
            city_check = self.check_city(city_value)
            occ_check = self.check_occ(occ_value)
            
            #Raises an exception if either of the city input or the OCC_Code input is empty or not valid
            if(type(city_value)!= str or type(occ_value)!= str or not city_check and not occ_check):
                raise Exception("Please Check the Inputs")
            #Returns data related to the city as the entered OCC_Code value is empty
            elif(city_check and occ_value == ''):
                return self.get_city_data(city_value, self.data_json_cities[city_value]) 
            #Raises an exception if OCC_Code does not exist in the given city
            elif(city_check and not occ_check):
                raise Exception("Please Check OCC Code")
            #Returns data related to the OCC_Code as the entered city value is not valid
            elif(not city_check and occ_check):
                return self.get_occ_data(occ_value)
            #Returns data if both the values are correct
            else:
                return self.get_city_occ_data(self.data_json_cities[city_value], occ_value)    
            
        #Catches the exceptions and returns them
        except Exception as _e:
            return {"ERROR" : str(_e)}
        return ret
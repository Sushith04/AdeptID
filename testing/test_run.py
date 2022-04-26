import requests
import threading
import random
import string
import json
import csv

THREADS = 100
DATA_LEN_BEG = 10
DATA_LEN_END = 100
URL = "http://127.0.0.1:5000/skills/reverse-skill-title"

def run_thread(data: str):
    data_rev = data[::-1].lower()
    req = requests.post(url=URL, json={"skill_title":data})
    req_json = json.loads(req.content.decode())
    if(req.status_code == 200):
        print(f"[+] Integrity : {data == req_json['skill_title']} Process: {data_rev == req_json['reversed_skill_title']} Data : {data}") 
        #pass                
    else:
        print(f"[x] Error: {req.status_code}")

def stress_test_reverse():
    threads = []
    for i in range(THREADS):    
        rand_len = random.randint(DATA_LEN_BEG, DATA_LEN_END)
        data = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=rand_len))
        threads.append(threading.Thread(target=run_thread, args=(data,)))
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

def csv_to_json():
    fp = open('data.csv', 'r', encoding='UTF-8')
    cr = csv.reader(fp, delimiter=',')
    data_json_cities = {}
    data_json = {}
    for row in list(cr.__iter__())[1:]:
        if(not data_json.get(row[2], None)):
            data_json[row[2]] = {
                       "name" : row[3],
                       "emp" : {
                           
                       }
                }
        try:
            emp_cnt = int(row[4],10) if(row[4]) else 0  
        except:
            emp_cnt = 0
        data_json[row[2]]["emp"][row[0]] = emp_cnt
        if(not data_json_cities.get(row[0], None)):
            data_json_cities[row[0]] = row[1]
    fp.close()
    fp = open('data_2.json','w', encoding='UTF-8')
    json.dump(data_json, fp, indent=4)
    fp.close()
    
    print(f"Cities : {data_json_cities}")

if __name__ == "__main__":
    #main()
    csv_to_json()
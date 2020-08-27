import os
import sys
from datetime import datetime

req_path=input("enter req path :")

if not os.path.exists(req_path):
    print("the given path is not exists")
    sys.exit(1)
if os.path.isfile(req_path):
    print("is file")
    sys.exit(2)
age=50
today=datetime.now()

list=os.listdir(req_path)

if len(list)==0:
    print("there is no files in this")
    sys.exit(3)
else:
    '''
    req_ex=input("enter req extension .py/.log/.txt :")
    req_f=[]
    for each in list:
        if each.endswith(req_ex):
            req_f.append(each)
    if len(req_f)==0:
        print("there is no files")
    else:
        print(req_f)
        '''

    for each in list:
        each_f=os.path.join(req_path,each)
        if os.path.isfile(each_f):
            file_c=datetime.fromtimestamp(os.path.getctime(each_f))
            diff=(today-file_c).days
            if diff > age:
                print(f"{each}=============>{diff}")


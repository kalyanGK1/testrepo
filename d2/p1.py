import csv

file="file.csv"

fo=open(file,'w',newline="")


csv_w=csv.writer(fo,delimiter=",")


my_data=[['S_no','Server_ip','Os','Env'],[1,'172.31.2.12','Ubuntu','dev'],[1,'172.31.2.12','Ubuntu','dev'],[1,'172.31.2.12','Ubuntu','dev']]
csv_w.writerows(my_data)


fo.close()

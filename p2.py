import csv

file="file.csv"


fo=open(file,'w',newline="")

csv_w=csv.writer(fo,delimiter=",")
my_data=[['s.no','name','age'],[1,'kalyan','23'],[2,'pradeep',30]]

csv_w.writerows(my_data)

fo.close()

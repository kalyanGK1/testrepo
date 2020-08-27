import json


file="file.json"

fo=open(file,'w')


my_dict={'builders': [{'type': 'amazon-ebs','region': "{{user `region`}}",'access_key':  "{{user `region`}}",'secret_key':  "{{user `region`}}",'instance_type':  "{{user `region`}}",'ssh_username':  "{{user `region`}}",'vpc_id':  "{{user `region`}}",'subnet_id':  "{{user `region`}}",'source_ami':  "{{user `region`}}",'ami_name':  "{{user `region`}}"}],'provisioners': [{'type': 'shell','scripts': ['./shell1.sh','./shell2.sh','./shell3.sh']}]}


json.dump(my_dict,fo,indent=4)

fo.close()


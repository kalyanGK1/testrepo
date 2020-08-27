import json

file="file.json"

fo=open(file,'w')

my_dict={'variables': {'access_key': "",'secret_key': ""},'builders': [{'type': 'amazon-ebs','access_key': "{{user `acees_key`}}",'secret_key': "{{user `acees_key`}}",'region': 'us-east-1','vpc_id': "{{user `acees_key`}}",'subnet_id': "{{user `acees_key`}}",'source_ami': "{{user `acees_key`}}",'ssh_username': "{{user `acees_key`}}",'ami_name': "{{user `acees_key`}}",'instance_type': "{{user `acees_key`}}"}],'provisioners': [{'type': 'shell','scripts': ['./shell1.sh','./shell1.sh','./shell1.sh']}]}

'''
my_dict={'Version': '2012-10-17','Statement': [{'Effect': 'Allow','Action': 'ec2:*','Resource': '*'},{'Effect': 'Deny','Action': ['ec2:TerminateInstances','ec2:StopInstances'],'Resource': 'arn:aws:ec2:*:638261181:instance/*','Condition': {'StringEquals': {'ec2:ResourceTag/env': 'prod'}}}]}
'''

json.dump(my_dict,fo,indent=4)

fo.close()

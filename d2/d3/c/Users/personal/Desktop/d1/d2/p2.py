import json


file="file.json"

fo=open(file,'w')


my_dict={'Version': '2012-10-17','Statement': [{'Effect': 'Allow','Action': 'ec2:*','Resource': '*'},{'Effect': 'Deny','Action': ['ec2:TerminateInstances','ec2:StopInstances'],'Resource': 'arn:aws:ec2:*634416617:instance/*','Condition': {'StringEquals': {'ec2:ResourceTag/env': 'prod'}}}]}
json.dump(my_dict,fo,indent=4)

fo.close()

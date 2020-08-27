#!/bin/bash


if [[ $# -eq 0 ]]
then
	echo "Plz Provide Atleast One Pkg Name After $0"
	exit 1
fi	

if [[ $(id -u) -ne 0 ]]
then
        echo "Your Not A Root User........"
        echo "You Have Root Or Sudo Provilisers To Do This Activity"
	exit 2
else
	echo "Your A Root User And Ur Authorized To Perform This Activity"

fi

for each in $@
do
	if which $each &>/dev/null
	then
		echo "$each Is Already Present..."
	else
		echo "$each is Installing...."
		apt install -y $each &>/dev/null
	        if [[ $? -ne 0 ]]
		then
			echo "Enable To Download The Pacakge"
	        fi
	fi	

	
done	


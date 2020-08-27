for each in $(ls)
do
	if [[ -x $each ]]
	then
		echo $each
	fi	
done	

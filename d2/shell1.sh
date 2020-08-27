cat server_info.txt |awk NR!=1{print} |while read ip user pkg1 pkg2
do
	ssh -n -o StrictHostKeyChecking=No $user@$ip apt install -y $pkg1 $pkg2
done

cat server_info.txt |awk NR!=1{print} | while read server_ip user pkg1 pkg2
do
	echo "$server_ip" "$user" "$pkg1" "$pkg2"
done	


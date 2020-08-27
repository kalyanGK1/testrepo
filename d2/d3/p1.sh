src=/c/Users/personal/Desktop/d1/d2/
dest=/c/Users/personal/Desktop/d1/d2/d3
edt=$(date '+%b_%d_%Y_%H_%M_%S')
[[ -e $dest ]] || mkdir $dest
tar -cvzpf $dest/mywebsite.com_bkup_${edt}.tar.gz $src

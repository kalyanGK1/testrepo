src=/c/Users/personal/Desktop/d1/d2/
dest=/c/Users/personal/Desktop/d1/d2/d3
edt=$(date '+%b_%d_%Y_%H_%M_%s')
tar -cvzpf $dest/mywebsite.com.{edt}.tar.gz $src

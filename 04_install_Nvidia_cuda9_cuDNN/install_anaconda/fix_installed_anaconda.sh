sudo chown -R curie:curie /home/curie/anaconda3
#https://blossomnoodles.github.io/cnBlogs/2018/04/30/Ubuntu18.04-Tensorlow-install.html
#再删去系统中除了anaconda3之外的conda,只留这个anaconda3里面的conda
#pip目录的属主不是sudo的root用户
#http://blog.sina.com.cn/s/blog_a046022d0102w2ux.html

sudo chown root /home/curie/.cache/pip
sudo chown root /home/curie/.cache/http

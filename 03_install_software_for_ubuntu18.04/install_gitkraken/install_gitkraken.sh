#https://www.jianshu.com/p/d353ba325b19
#debian环境下安装gitkraken无法启动的解决方案
whereis gitkraken
cd /usr/bin
./gitkraken
# libgnome-keyring.so.0: cannot open shared object file: No such file or directory
# https://github.com/GNOME/libgnome-keyring
# https://askubuntu.com/questions/776440/gitkraken-and-kubuntu-installs-but-doesnt-run
sudo apt install libgnome-keyring-common libgnome-keyring-dev

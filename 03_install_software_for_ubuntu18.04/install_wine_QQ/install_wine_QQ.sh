# https://www.cnblogs.com/dudujerry/p/9763518.html
# https://github.com/wszqkzqk/deepin-wine-ubuntu
wget -qO- https://raw.githubusercontent.com/wszqkzqk/deepin-wine-ubuntu/master/online_install.sh | bash -e
# https://github.com/wszqkzqk/deepin-wine-containers-for-ubuntu
# 最好开个ssr
wget https://raw.githubusercontent.com/wszqkzqk/deepin-wine-containers-for-ubuntu/master/deepin.com.qq.im_8.9.19983deepin23_i386.deb
sudo apt --fix-broken install
sudo apt-get install deepin-wine-uninstaller
sudo apt-get install gnome-menus
sudo apt-get install desktop-file-utils
sudo apt-get install mime-support
sudo apt-get install hicolor-icon-theme
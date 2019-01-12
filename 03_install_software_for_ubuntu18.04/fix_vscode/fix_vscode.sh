#https://blog.csdn.net/wenyun_kang/article/details/69389784 code的配置文件被加上了root权限 
cd ~/.config 
chmod 777 Code
cd Code
chmod 777 installSource  logs  machineid  User
cd ~/.config
sudo rm -rf ./Code/ 

# https://blog.csdn.net/xianqin_ma/article/details/79525519
# 这是权限问题，安装时root权限创建了 ~/.nv/但是起里面没权限读写，故解决方法是删去~/.nv/文件夹或其内容。
# 解决方法至于rm -f ~/.nv/

cd ~/.nv
sudo rmdir /home/curie/.nv/ComputeCache

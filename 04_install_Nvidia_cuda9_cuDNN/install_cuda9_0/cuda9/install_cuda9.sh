# https://blossomnoodles.github.io/cnBlogs/2018/04/30/Ubuntu18.04-Tensorlow-install.html
# sudo apt-get install freeglut3-dev build-essential libx11-dev libxmu-dev libxi-dev libgl1-mesa-glx libglu1-mesa libglu1-mesa-dev

# !!!
# sudo mkdir /usr/local/cuda-9.0 
# chmod 777 /usr/local/cuda-9.0 
# 复制 cuda_9.0.176_384.81_linux.run到/usr/local/cuda-9.0 
# cd /usr/local
# sudo ln -s /usr/local/cuda-9.0 cuda     # create the symbolic link
cd /usr/local/cuda
sudo chmod 777 *.runfile    # give permission to run all the runfile files
sudo ./cuda_9.0.176_384.81_linux.run -toolkit -samples -silent -override #


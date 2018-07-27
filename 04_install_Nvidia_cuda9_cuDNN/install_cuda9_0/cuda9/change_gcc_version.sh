gcc --version   # check ubuntu 18.04 gcc version, you will find it's 7.3.0
sudo apt install gcc-5 g++-5
sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-5 50   # you will find that message that tells you the gcc-5 is set to be automatic.
sudo update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-5 50   # similiar message as gcc
# https://blog.csdn.net/chunchun362425965/article/details/51566851

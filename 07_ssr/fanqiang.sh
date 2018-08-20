#！/bin/bash
#shadow.sh
#screen python ~/shadowsocksr/shadowsocks/local.py -c /etc/shadowsocks.json
python ~/shadowsocksr/shadowsocks/local.py -c /etc/shadowsocks.json
# /etc/init.d/polipo restart
# https://www.jianshu.com/p/a0f3268bfa33 4 - Ubuntu 16.04 + SSR翻墙
# https://blog.csdn.net/helinbin/article/details/56015572 python Address already in use 端口已经被占用的解决方法
# http://www.baavpn.com/modules/node.php
# 平时就打开个终端 python ~/shadowsocksr/shadowsocks/local.py -c /etc/shadowsocks.json
# 想停止就按 ctrl c 而不是ctrl z 来正常结束

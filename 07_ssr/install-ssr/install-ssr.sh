# https://www.mystery0.vip/2018/08/23/Ubuntu%20Server%2018.04%20LTS%20%E4%BD%BF%E7%94%A8Shadowsocks-ShadowsocksR%E8%AE%BF%E9%97%AE%E4%BA%92%E8%81%94%E7%BD%91/
# Ubuntu Server 18.04 LTS 使用Shadowsocks-ShadowsocksR访问互联网
sudo apt-get install privoxy
sudo apt-get install proxychains4
wget https://github.com/the0demiurge/CharlesScripts/blob/master/charles/bin/ssr
sudo mv ssr /usr/local/bin
sudo chmod 766 /usr/local/bin/ssr
ssr install
# ssr help
# ssr start
# ssr stop
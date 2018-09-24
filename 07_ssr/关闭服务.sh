service polipo stop
service NetworkManager stop
# 不想用代理时，polipo不断提示connection failed就很烦
# 这样把他关掉，想再开就/etc/init.d/polipo restart

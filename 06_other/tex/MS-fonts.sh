sudo mkdir -p /usr/share/fonts/winFonts
sudo cp /media/curie/OS/Windows/Fonts/*.ttf /usr/share/fonts/winFonts/
sudo chmod 644 /usr/share/fonts/winFonts/*.ttf
cd /usr/share/fonts/winFonts/
sudo mkfontscale 
#（创建雅黑字体的fonts.scale文件，它用来控制字体旋转缩放）
sudo mkfontdir 
#（创建雅黑字体的fonts.dir文件，它用来控制字体粗斜体产生）
sudo fc-cache -fv 
#（建立字体缓存信息，也就是让系统认识雅黑）

#本文来自 炽天使_晓 的CSDN 博客 ，全文地址请点击：https://blog.csdn.net/qq183837971/article/details/78235144?utm_source=copy 

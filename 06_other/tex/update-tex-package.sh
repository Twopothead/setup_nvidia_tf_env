#http://bbs.ctex.org/forum.php?mod=viewthread&tid=45392

# dsfont
sudo chmod 777 -R /usr/local/share/texmf
sudo chmod 777 -R /var/lib/texmf
texhash
# Letting TeX 'know' about the file means running a program that builds a database of file locations. There are graphical interfaces to do this, but the way that works on all operating systems is to use the Command Prompt/Terminal and type texhash.
# This will build the databases for your tree (the one that is in your home folder). Once the 'hash' is created TeX should be able to find your file. For recent TeXLive distributions, this step is not necessary for files in the local folde
#本文来自 algondon 的CSDN 博客 ，全文地址请点击：https://blog.csdn.net/u010801696/article/details/79410545?utm_source=copy 

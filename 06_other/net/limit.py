# -*- coding:utf-8 -*-
import requests
import json 
# login_url = 'http://net.njau.edu.cn/'
login_url = 'http://172.16.0.3/' # 教学楼
#login_url = 'http://172.16.0.4/' # 宿舍
query_url = 'http://172.16.0.3/1.htm'
wbdata = requests.get(query_url).text
login_out_url = 'http://172.16.0.3/F.htm'
# print(wbdata)
# time='2229      ';flow='333437    ';fsele=1;fee='46900 
# (time) minutes　; (flow) kB ;(fee)/10000 = ?元 ,每月送5元
# (flow) should <4608000= 45000*1024; fee should >0 
import re
accounts = []
#f = open("user.txt", "r") # 读取user.txt文件的账户和密码信息
f = open("17_user_passwd.txt", "r") # 读取user.txt文件的账户和密码信息

for user in f:     
    tmp = []  # 每一行的信息临时列表 
    tmpUser = user
    # tmpUser, tmpPassword = user.split(" ", 1)    # 以空格拆分出每一行的用户名和密码，并存入tmpUser和tmpPassword变量中    
    tmp.append(tmpUser.strip())      
    # tmp.append(tmpPassword.strip())    # 把tmp列表存入account列表中    
    accounts.append(tmp)    # 读取每一行
f.close()
# for i in range (1,len(accounts)):
#     print(accounts[i][0])

def subString_time_flow_fee(template):
    #template = "我要'歌手名'的'歌曲名'"
    rule = r"time='(.*?)';flow='(.*?)';fsele"
    # rule = r'<(.*?)>' # "我要<歌手名>的<歌曲名>"
    # https://blog.csdn.net/mp624183768/article/details/81411601
    slotList = re.findall(rule, template)
    time =  int(slotList[0][0])
    flow =  int(slotList[0][1])
    rule_fee = r";fee='(.*?)'"
    feeList = re.findall(rule_fee, template)
    fee = int(feeList[0])
    return (time,flow,fee)
(time,flow,fee) = subString_time_flow_fee(wbdata)
print("[time]:",time,"[flow]:",flow,"[fee]:",fee)
print("已使用时间 Used time : ",time,"Min;","已使用流量 Used flux : ",int(flow/1024)," MByte;","余额 Balance : ",fee/10000,"RMB.")
# def login_out():
#     login_out_data = requests.get(login_out_url).text
# def login_in():
#      password = 123456    
#      user = 20216111
# #http://172.16.0.3:9002/0
#      login_headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:41.0) Gecko/20100101 Firefox/41.0'}
#      form1_value={'DDDDD':user,'upass':password,'0MKKey':''
#      ,'0MKKey':''
#      ,'Referer':'http://net.njau.edu.cn/'}
#      form1_data = json.dumps(form1_value)
#      l_response = requests.post(url=login_url, headers=login_headers,data=form1_data)
#      l_response.encoding = 'utf-8'
#      l_r=l_response.text
#      print(l_r)
#      return l_r.find('Msg')<0
     
# print("ok?",login_in())
# 每1小时自动执行    linux下比较方便，直接设置 crontab即可。
# login_out()
# # print(wbdata)
#https://www.cnblogs.com/dirge/p/5616168.html
# https://blog.csdn.net/cx943024256/article/details/78883088#222-%E9%81%87%E5%88%B0%E7%9A%84%E9%97%AE%E9%A2%98
#表单中仅仅使用用户名和密码无法正常登录，这是仔细查看网页源代码，会发现表单中还有好几项在代码的前一段。也就是<input... 开头的部分。所以我们在username 、password 这两项之外还要把这些额外的内容添加上。



#https://blog.csdn.net/lzk354060641/article/details/78442996?locationNum=10&fps=1



# account = []
# # You should modify bookingdate '2018-10-22,2018-10-23,2018-10-24,2018-10-25,2018-10-26,2018-10-27,2018-10-28',
# import time
# f = open("userID_pwd.txt", "r") # 读取user.txt文件的账户和密码信息
# for user in f:     
#     tmp = []  # 每一行的信息临时列表    
#     tmpUser, tmpPassword = user.split(" ", 1)    # 以空格拆分出每一行的用户名和密码，并存入tmpUser和tmpPassword变量中    
#     tmp.append(tmpUser.strip())      
#     tmp.append(tmpPassword.strip())    # 把tmp列表存入account列表中    
#     account.append(tmp)    # 读取每一行
# f.close()
# userID = account[0][0]
# pwd = account[0][1]
# print("userID:",userID," pwd:",pwd)

# import urllib
# import json
# import requests
# from requests.exceptions import RequestException
# import random 

# sess = requests.session() # 创建可传递cookies的会话
# mac_user = 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
# linux_user = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
# # from fake_useragent import UserAgent
# # ua = UserAgent()
# # random_user = ua.random


# def login_get_cookie_value():
#     login_url = "http://seatbook.njau.edu.cn/login.action"
#     Cookie = ""
#     login_headers_to_send = {
#     'Accept': 'application/json, text/javascript, */*; q=0.01',
#     'Accept-Encoding': 'gzip, deflate', 
#     'Accept-Language': 'en,zh-CN;q=0.9,zh;q=0.8,zh-TW;q=0.7',
#     'Connection': 'keep-alive', 
#     'Content-Length': '26', 
#     'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',

#     'Host': 'seatbook.njau.edu.cn', 
#     'Origin': 'http://seatbook.njau.edu.cn', 
#     'Referer': 'http://seatbook.njau.edu.cn/', 
#     'User-Agent': mac_user , 
#     'X-Requested-With': 'XMLHttpRequest',
#     }

#     login_form_data = 'userID='+userID+'&'+'pwd='+pwd
#     l_response = requests.post(url=login_url, headers=login_headers_to_send,data=login_form_data)
#     # l_response = sess.post(url=login_url, headers=login_headers_to_send,data=login_form_data)
#     l_response.encoding = 'utf-8'
#     l_r=l_response.text
#     cookies_dict =l_response.cookies.get_dict()
#     cookie_value =""
#         #print(cookies) {'JSESSIONID': 'ECD5ACD7D345BFF7BB832C43B7BA6B65'}
#     if 'JSESSIONID' in l_response.cookies.get_dict():
#         cookie_value = l_response.cookies.get_dict()['JSESSIONID']
#         print("[login state]:",l_r)
#         #print(cookies_value) FD69262EE72DB9D1B6D137C97F13D42A
#     return cookie_value 

# def get_form_data_values(seat_id):
#     form_data_values={
#         'bookingdate': '2018-10-22,2018-10-23,2018-10-24,2018-10-25,2018-10-26,2018-10-27,2018-10-28',
#         'seatid': seat_id}
#     return form_data_values


# def get_cookie_headers():
#     cookie_value = login_get_cookie_value()
#     headers_to_send = {
#     'Accept': 'application/json, text/javascript, */*; q=0.01',
#     'Accept-Encoding': 'gzip, deflate', 
#     'Accept-Language': 'en,zh-CN;q=0.9,zh;q=0.8,zh-TW;q=0.7',
#     'Connection': 'keep-alive', 
#     'Content-Length': '111', 
#     'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
#     'Cookie': "JSESSIONID=" + cookie_value,
#     'Host': 'seatbook.njau.edu.cn', 
#     'Origin': 'http://seatbook.njau.edu.cn', 
#     'Referer': 'http://seatbook.njau.edu.cn/booking/chooseDate.jsp', 
#     'User-Agent': mac_user , 
#     'X-Requested-With': 'XMLHttpRequest',
#     }
#     return headers_to_send

# reserve_url = "http://seatbook.njau.edu.cn/booking.action"
# attempt_counter = 0 
# global_cookie_headers = get_cookie_headers()
# def update_global_cookie_headers():
#     global_cookie_headers = get_cookie_headers() # get another cookie


# while(1):
#     seat_id = random.randint(90,170) 
#     # A001-A192 图书馆四楼学习室
#     form_data = json.dumps(get_form_data_values(seat_id))
#     print("[the ",attempt_counter,"th attempt]:",attempt_counter)
#     # headers_to_send = get_cookie_headers() # get another cookie
#     headers_to_send = global_cookie_headers
#     if (attempt_counter % 40) == 0:
#         update_global_cookie_headers()
#     response = requests.post(url=reserve_url, headers=headers_to_send,data=form_data)
#     print("[Booking]:     seat_id=",seat_id)
#     # response = sess.post(url=reserve_url, headers=headers_to_send,data=form_data)
#     response.encoding = 'utf-8'
#     r=response.text
#     print("[library msg]:",r)
#     print('--------------------------------------------------------------')
#     attempt_counter += 1
#     # time.sleep(random.uniform(0.1, 0.5))
#     time.sleep(random.uniform(1, 10))
#     # 服务器限制了部分User-Agent的访问
#     # no-referrer-when-downgrade  https://blog.csdn.net/python_neophyte/article/details/82562330


# # #找出表单提交到的页面
# # #还是要利用浏览器的开发者工具。转到network选项卡，并勾选Preserve Log（重要！）。在浏览器里登录网站。然后在左边的Name一栏找到表单提交到的页面。怎么找呢？看看右侧，转到Headers选项卡。首先，在General那段，Request Method应当是POST。其次最下方应该要有一段叫做Form Data的，里面可以看到你刚才输入的用户名和密码等。也可以看看左边的Name，如果含有login这个词，有可能就是提交表单的页面（不一定！）。
# # #这里要强调一点，“表单提交到的页面”通常并不是你填写用户名和密码的页面！所以要利用工具来找到它。
# # https://www.cnblogs.com/chenxiaohan/p/7654667.html#two
import requests
import re
import base64
import rsa
import random
import time
import binascii
from rsaen1 import RSAKey

class GetLogin:
    #设置http协议版本
    #http.client.HTTPConnection._http_vsn = 10
    #http.client.HTTPConnection._http_vsn_str = 'HTTP/1.0'

    #建立会话，维持连接
    sessions = requests.Session()

    def __init__(self, username, passward):                       
        self.username = username
        self.passward = passward

    #获取cookie
    #url = "http://jwgl8.ujn.edu.cn/jwglxt/"
    #res = requests.get(url)
    #cookie = res.cookies.get("JSESSIONID")
    #print(type(cookie))

    #获取punlic_key
    def getPublicKeyAndEncrypt(self):
        print("获取publicKey并加密...")
        date = str(int(time.time()))+str(random.randint(100,999))
        url_publicKey = "http://jwgl8.ujn.edu.cn/jwglxt/xtgl/login_getPublicKey.html?time="+date
        res_publicKey = self.sessions.get(url_publicKey)
        exponent = res_publicKey.json()["exponent"]
        modulus = res_publicKey.json()["modulus"]
        #HB = HB64()
        #b_exponent = HB.b642hex(exponent)
        #b_modulus = HB.b642hex(modulus)
        b1_exponent = binascii.hexlify(base64.b64decode(exponent)).decode("utf-8")
        b1_modulus = binascii.hexlify(base64.b64decode(modulus)).decode("utf-8")
        rsa_1 = RSAKey()
        rsa_1.setPublic(b1_modulus,b1_exponent)                         
        cry_data = rsa_1.encrypt(self.passward)
        en1_passwd = base64.b64encode(binascii.unhexlify(cry_data)).decode("utf-8")
        self.passward = en1_passwd
        
    #获取csrftoken
    def getCsrftoken(self):
        print("获取token...")
        url_1 = "http://jwgl8.ujn.edu.cn/jwglxt/xtgl/login_slogin.html?language=zh_CN"
        res_token = self.sessions.get(url_1)
        token = re.findall(r"<input type=\"hidden\" id=\"csrftoken\" name=\"csrftoken\" value=\"(.*)\"/>",res_token.text)
        token = token[0]
        self.csrftoken = token

    # 获取login
    def getLogin(self):    
        print("获取登录状态...")
        url_login = "http://jwgl8.ujn.edu.cn/jwglxt/xtgl/login_slogin.html"
        data_param = {
            
                    "csrftoken":self.csrftoken,
                    "yhm":self.username,
                    "mm":self.passward,
                    "mm":self.passward
            }
        length = str(len(str(data_param)))
        headers_login = {
                "Host": "jwgl8.ujn.edu.cn",
                "Connection": "keep-alive",
                "Cache-Control": "max-age=0",
                "Content-Length": length,
                "Origin": "http://jwgl8.ujn.edu.cn",
                "Upgrade-Insecure-Requests":"1",
                "Content-Type": "application/x-www-form-urlencoded",
                "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
                "Referer": "http://jwgl8.ujn.edu.cn/jwglxt/xtgl/login_slogin.html?language=zh_CN&_t=1555972905286"+str(int(time.time())),
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",

            }
        
        res_login = self.sessions.post(url_login,headers = headers_login,data = data_param)
        
        flag = 0
        if(res_login.headers.get("Set-Cookie")):
            flag = 1
        return flag
        


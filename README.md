

## 登录过程简要说明

>### 注意
>* *http协议是无状态的，也就是说一次连接过后它并不会记住这一次的连接行为。对于有登录且在登陆后有后续操作的行为我们需使服务器有一种行为记住我们的登陆状态.即cookies,由服务器生成保存在客户端。*
>* *在python中requests库对http请求进行了封装，提供了对消息的处理函数。对于cookies设置了session会话函数进行自动保存，不用额外获取cookies，一个session即一系列连续的操作。*
>* *准备工作数据包分析，可以使用浏览器自带开发者工具，推荐使用Fiddler*
>* *此事例环境python3*
>### 步骤说明
> 1. 获取csrftoken
>>* token在登录页面前端由js生成
>>* 向http://jwgl8.ujn.edu.cn/jwglxt/xtgl/login_slogin.html?language=zh_CN发送get请求，获取返回的html页面
>>* pythin正则表达式获取html内容中的csrftoken的value值

> 2. 获取exponent和modulus生成公钥
>>* 向http://jwgl8.ujn.edu.cn/jwglxt/xtgl/login_getPublicKey.html?time=...."发送get请求
>>* 注意在请求最后要加上时间戳，原网页使用js生成的13位时间戳，但在python中只能精确到秒即10位。本实例在10位后加上了随机产生的三位整数。也可以直接乘以1000。
>>* 接受到的exponent和modulus为base64编码的字符串，作处理后生成publicKey(后面会说到具体处理)。加密算法采用rsa。

> 3. 获取登录状态，即登录成功将状态保存到session
>>* 向http://jwgl8.ujn.edu.cn/jwglxt/xtgl/login_slogin.html发送post请求
>>* post中携带数据

                data = {
                        "csrftoken":
                        "yhm":用户名
                        "mm":密码(加密后)
                        "mm":密码(加密后)
                         }

>>* fiddler抓取数据包复制headers作为此次请求数据头

> 4. 获取课表
>>* 向http://jwgl8.ujn.edu.cn/jwglxt/kbcx/xskbcx_cxXsKb.html?gnmkdm=N2151发送post请求

                data = {
                    "xnm":学年
                    "xqm":学期，第一或第二学期         
                    }
>>* 获取返回的json数据，并提取所需的数据

## 函数API

> 1. Class GetLogin:
>>* __init__(self, username, passward)------//初始化
>>* getCsrftoken()    ------//获取token
>>* getPublicKeyAndEncrypt() ------//获取exponent和modulus并生成PublicKey然后加密密码
>>* getLogin()------//获取登录状态

> 2. Class GetInfo(GetLogin):
>>* __init__(self,username,password,school_year,semester)------//继承GetLOgin，需要用到GetLogin里的session会话
>>* getCourse()------//获取课表，处理数据

> 3. Class Connection(GetInfo):
>>* __init__(self,username,password,school_year,semester)------//继承GetInfo，需要用到GetInfo里有session会话的getCourse
>>* formatData()------//格式化键盘输入数据
>>* isExistUserCourse()------//检测数据库是否有备份，有则直接取出，没有则调用getCourse,并存入数据库
>>* courseHandle()------//将处理后的课表数据插入到数据库
>>* getCourseFromMysql------//()从数据库读取符合键盘输入的数据

> 4. Class RSAKey:
>>* setPublic(self, N, E)------//将exponent和modulus由hex转为十进制 
>>* encrypt(self, text)------//加密密码，并处理加密后密文

## start.py 测试
>* 见start.py文件

## exponent和modulus处理以及加密说明：
>* e和m作为生成rsa公钥的两个参数
>* 原始为base64字符串
>* python库base64解码base64编码，将解码后的字符再转换成hex(由binascii库完成)。此步骤也可自行编码完成。
>* 由十六进制的exponent和modulus生成publicKey,用于之后加密
>* 加密采用rsa算法。返回十六进制密文。
>* 将十六进制的密文处理后再转为base64编码作为post请求的参数

## 附注
>* mysql数据库v8.0 
>* 数据库名course 表名school_timetable
>* 表字段名
>>* username:学生学号
>>* course_name：课程名称
>>* week：星期
>>* time：时间（节数）
>>* teacher_name：授课教师
>>* address：地点
>>* which_week：单双周
>>* school_year：学年
>>* semester：学期

    

    


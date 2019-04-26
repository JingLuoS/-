from ConnMysql import Connection

flag = 1
while flag==1:
    username = input("请输入用户名：")     #教务系统用户名 12位学号
    password = input("请输入密码：")      #密码
    school_year = input("请输入学年(如2018-2019)：")   #学年
    semester = input("请输入学期1/2：")   #学期
    #格式数据
    school_year = school_year.split("-")[0]
    if semester =="2":
        semester = "12"
    else:
        semester = "3"
    getInfo = Connection(username,password,school_year,semester)
    getInfo.getCsrftoken()  #获取token
    getInfo.getPublicKeyAndEncrypt()    #获取exponent和modulus 生成publicKey并加密密码
    flag = getInfo.getLogin()   #获取登录状态返回flag标志
    if(flag==1):
        print("用户名或密码不正确,请再次输入\n")

getInfo.isExistUserCourse()    #判断数据库是否有备份 若没有则联网获取并存入数据库
result = getInfo.getCourseFromMysql()   #从数据库获取信息
getInfo.closeDB()   #关闭数据库
for i in result:
    print(" ".join(i))

import pymysql
from Info import GetInfo

#Connection--->继承GetInfo--->继承getLogin
class Connection(GetInfo):

    def __init__(self,username,password,school_year,semester):
        super().__init__(username, password,school_year,semester)

    db = pymysql.connect("localhost","root","******","course")
    
    #格式化数据
    def formatData(self):
        if self.semester =="12":
            self.semester_altered = "2"
        else:
            self.semester_altered = "1"
        self.schoo_lyear_altered= self.school_year+"-"+str(int(self.school_year)+1)
   
    #检查数据库是否有备份
    def isExistUserCourse(self):
        print("检测数据库是否有备份...")
        self.formatData()
        cursor = self.db.cursor()
        sql = "select * from school_timetable where username = '"+self.username+"' and school_year = '"+self.schoo_lyear_altered+"' and semester='"+self.semester_altered+"'"
        cursor.execute(sql)
        result = cursor.fetchone()
        if(result):
            return None
        else:
            print("数据库无备份...")
            self.one_list = self.getCourse()
            self.courseHandle()
            
    #插入课表到数据库course表school_timetable
    def courseHandle(self):
        print("将数据插入数据库...")
        for i in self.one_list:
            cursor = self.db.cursor()
            sql = ("insert into school_timetable(username,course_name,week,time,teacher_name,address,which_week,school_year,semester) values('"
                   +self.username+"','"+i["课程名称"]+"','"+i["星期"]+"','"
                   +i["时间"]+"','"+i["教师"]+"','"+i["地点"]+"','"+i["上课周"]
                   +"','"+i["学年"]+"','"+i["学期"]+"')")
            try:
                cursor.execute(sql)
                self.db.commit()
                print("log....插入数据库成功")
            except:
                self.db.rollback()
    
    #从数据库获取信息
    def getCourseFromMysql(self):
        print("从数据库获取信息...")
        self.formatData()
        schoolyear = self.school_year+"-"+str(int(self.school_year)+1)
        cursor = self.db.cursor()
        sql = "select * from school_timetable where username = '"+self.username+"' and school_year = '"+self.schoo_lyear_altered+"' and semester='"+self.semester_altered+"'"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

        #关闭数据库
    def closeDB(self):
        self.db.close()

            
           
            



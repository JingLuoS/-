from Login import GetLogin
import requests

#GetInfomation 继承GetLOgin
class GetInfo(GetLogin):

    def __init__(self,username,password,school_year,semester):
        super().__init__(username, password)
        self.school_year = school_year
        self.semester = semester

    #获取课表
    def getCourse(self):
        print("联网获取课表...")
        self.formatData()
        url_course = "http://jwgl8.ujn.edu.cn/jwglxt/kbcx/xskbcx_cxXsKb.html?gnmkdm=N2151"
        data_param_course = {
                    "xnm":self.school_year,
                    "xqm":self.semester
                    #"gndm":"N2151"
            }
        res_course = self.sessions.post(url_course,data=data_param_course)
        all_info = res_course.json()["kbList"]
        year = res_course.json()["xsxx"]["XNMC"]
        middle_semester = res_course.json()["xsxx"]["XQM"]
        if middle_semester =="12":
            middle_semester = "2"
        else:
            middle_semester = "1"
        list_all=  []
        for i in all_info:
            dic = dict()
            dic["课程名称"] = i["kcmc"]
            dic["上课周"] = i["zcd"]
            dic["星期"] = i["xqjmc"]
            dic["时间"] = i["jc"]
            dic["教师"] = i["xm"]
            dic["地点"] = i["cdmc"]
            dic["学年"]= year
            dic["学期"] = middle_semester
            list_all.append(dic)
        return list_all


    # 添加其他
    # def .....

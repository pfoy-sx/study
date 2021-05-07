#coding:utf8
class SchoolMember(object):
    '''学校成员基类'''
    MEMBERCOUNT = 0
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex =sex
        self.enroll()

    def enroll(self):
        """实例化后进行注册"""
        print("Just enroll a new school member [ %s ]" % self.name)
        SchoolMember.MEMBERCOUNT += 1

    def info(self):
        for k,v in self.__dict__.items():
            print(k,v,)
        print("-------------------END------------------")

class TeacherMember(SchoolMember):
    '''教师类'''
    def __init__(self,name,age,sex,sarly,course):
        #SchoolMember.__init__(self,name,age,sex)   #经典类继承,现在不用该方法
        super(TeacherMember,self).__init__(name,age,sex)  #新式类继承，现在基本上用该方法
        self.sarly = sarly
        self.course = course

    def tearching(self):
        print("[%s] is tearching %s " % (self.name,self.course))

class StudyMember(SchoolMember):
    def __init__(self,name,age,sex,course,tuition):
        #SchoolMember.__init__(self,name,age,sex)     #经典类继承,现在不用该方法
        super(StudyMember,self).__init__(name,age,sex)  #新式类继承，现在基本上用该方法
        self.course = course
        self.tuition = tuition
        self.amount = 0

    def pay_tuition(self,amount):
        print("Student [ %s ] has just pay %s to buy %s " % (self.name,self.amount,self.course))
        self.amount += amount

t1 = TeacherMember("Alix",38,"N/A",8000,"python")
s1 = StudyMember("Beam",25,"Man","python",100000)
s2 = StudyMember("Mity",25,"Lady","python",80000)


print("注册数量：%s" % SchoolMember.MEMBERCOUNT)
t1.info()
s1.info()
s2.info()
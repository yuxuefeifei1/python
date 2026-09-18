#创建类
class CuteCat:
    def __init__(self,cat_name,cat_age,cat_color):
        self.name=cat_name
        self.age=cat_age
        self.color=cat_color
    def speak(self):
        print("喵"*self.age)
    def think(self,content):
        print(f"小猫{self.name}在思考{content}...")

cat1=CuteCat("Jojo",2,"橘色")
print(f"小猫{cat1.name}的年龄是{cat1.age}岁，花色是{cat1.color}")
cat1.speak()
cat1.think("现在去抓沙发还是去撕纸箱")



class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = {"语文": 0, "数学": 0, "英语": 0}

    def set_grade(self, course, grade):
        if course in self.grades:
            self.grades[course] = grade

    def print_grade(self):
        print(f"学生{self.name}(学号:{self.student_id})的成绩为：")
        for course in self.grades:
            print(f"{course}:{self.grades[course]}分")

lin=Student("小林", "0001")
chen=Student("小陈", "0002")

chen.set_grade("语文", 92)
chen.set_grade("数学", 94)
chen.print_grade()


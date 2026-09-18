##1. super () 不止调用 init
##super()不只是用来调用父类__init__，也可以调用父类普通方法。
##class Animal:
##    def say(self):
##        print("发出声音")
##
##class Dog(Animal):
##    def say(self):
##        super().say()   # 执行父类的say
##        print("汪汪汪")
##
##
##
##2. 重写 (override)
##子类写一个和父类同名方法，就会覆盖父类版本。
##Human、Cat 继承 Mammal，如果子类写def breath(self):，就会替换父类 breath。
##注意：不是修改父类代码，只改变子类对象行为。
##
##
##
##3. 多继承（一个类继承多个父类）
##语法：class 类名(父类1,父类2):
##class A:
##    def fun_a(self):
##        print("A")
##class B:
##    def fun_b(self):
##        print("B")
##
##class C(A,B):
##    pass
##
##c=C()
##c.fun_a()
##c.fun_b()
##⚠️ MRO 方法解析顺序：当多个父类有同名方法，按照继承顺序查找。可以用类名.__mro__查看查找顺序。
##
##
##4. 类属性 vs 实例属性
##你代码全部使用实例属性(self.xxx)。
##实例属性：每个对象各自独立，写在__init__里面，self.xxx
##类属性：属于这个类本身，所有对象共享，写在class内部、def外面。
##class Cat:
##    species = "猫科动物"   # 类属性，全部Cat对象共用
##    def __init__(self,name):
##        self.name = name  # 实例属性，每个猫自己的名字
##访问：Cat.species或者cat_obj.species
##
##
##
##5. 私有属性 / 私有方法（伪私有）
##Python 没有真正严格私有，用双下划线__开头实现名称改写。
##class Staff:
##    def __init__(self,name):
##        self.__password = "123456" # 私有属性，外部不能直接obj.__password访问
##    def get_pwd(self):
##        return self.__password
##单下划线_xxx只是约定，提醒使用者不要随便修改，语法上外部仍然可以访问。
##
##
##6. 魔术方法（特殊方法）
##除了__init__，其他常用魔术方法：
##__str__：print(对象)的时候自动调用，返回字符串，用来打印对象信息
##class Cat(Mammal):
##    def __str__(self):
##        return f"猫：{self.name}"
##__repr__：调试展示对象；
##__len__：支持len(对象)。
##
##
##
##7. isinstance () 判断对象属于哪个类
##tom = Cat("汤姆","公")
##print(isinstance(tom,Cat))      # True
##print(isinstance(tom,Mammal))   # True，继承关系也返回True
##issubclass(Cat,Mammal) 判断 Cat 是不是 Mammal 的子类。
##
##
##
##8. pass 占位符
##当类 / 方法暂时不想写实现，写pass，语法不会报错。
##class Test:
##    pass
##
##
##9. 继承设计小原则
##继承描述is‑a关系：Cat is a Mammal猫是哺乳动物，适合继承。
##如果是has‑a（拥有）关系，不要用继承，使用组合：类里面包含另一个类的对象作为属性。







class Human:
    def __init__(self,name,sex):
        self.name=name
        self.sex=sex
        self.num_eyes=2
        self.has_tail=False
    def breath(self):
        print(self.name+"在呼吸...")
    def poop(self):
        print(self.name+"在拉屎...")
    def read(self):
        print(self.name+"在阅读...")



class Cat:
    def __init__(self,name,sex):
        self.name=name
        self.sex=sex
        self.num_eyes=2
        self.has_tail=True
    def breath(self):
        print(self.name+"在呼吸...")
    def poop(self):
        print(self.name+"在拉屎...")
    def scrach_sofa(self):
        print(self.name+"在抓沙发...")






class Mammal:
    def __init__(self,name,sex):
        self.name=name
        self.sex=sex
        self.num_eyes=2
    def breath(self):
        print(self.name+"在呼吸...")
    def poop(self):
        print(self.name+"在拉屎...")


class Human(Mammal):
    def __init__(self,name,sex):
        super().__init__(name,sex)
        self.has_tail=False
    def read(self):
        print(self.name+"在阅读...")
        
class Cat(Mammal):
    def __init__(self,name,sex):
        super().__init__(name,sex)
        self.has_tail=True
    def scratch_sofa(self):
        print(self.name+"在抓沙发...")





class Staff:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def print_info(self):
        print(self.name+"的工号为"+self.id)


class FullTimeStaff(Staff):
    def __init__(self,name,id,monthly_salary):
        super().__init__(name,id)
        self.monthly_salary=monthly_salary
    def calculate_monthly_pay(self):
        return self.monthly_salary
    

class PartTimeStaff(Staff):
    def __init__(self,name,id,daily_salary,work_days):
        super().__init__(name,id)
        self.daily_salary=daily_salary
        self.work_days=work_days
    def calculate_monthly_pay(self):
        return self.daily_salary*self.work_days


zhangsan=FullTimeStaff("张三","001","6000")
lisi=PartTimeStaff("李四","002",230,15)
zhangsan.print_info()
lisi.print_info()
print(zhangsan.calculate_monthly_pay())
print(lisi.calculate_monthly_pay())








































        

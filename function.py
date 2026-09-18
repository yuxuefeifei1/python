#① 位置参数 vs 关键字参数
def calc(a,b):
    print(a+b)

calc(2,3)         #位置参数：按顺序对应 a=2，b=3
calc(b=3,a=2)     #关键字参数：不用管顺序，写清楚参数名


#② 默认参数（形参给默认值），⚠️坑：默认参数尽量不要写列表、字典这种可变对象
def calc_bmi(weight, height=1.70):
    return weight / height**2

calc_bmi(60)          #height不写，自动height=1.70
calc_bmi(60,1.80)     #手动覆盖默认height


#③ 形式参数 (形参)、实际参数 (实参) 区分
#   def f(x): 这里 x 叫形参，只是占位
#   f(100) 这里 100 叫实参，真正传给函数的数据


#2. return 重点（你已经在用，加深理解）
#return 会立刻结束函数，return 后面的代码不会执行
def test():
    return 10
    print("这句话永远不会运行！")


#没有写return的函数，默认返回 None
#可以一次性返回多个值，用元组接收
def get_info():
    return 180,75
h,w = get_info()


#变量作用域【非常重要】
#局部变量：函数里面创建的变量，函数外面不能访问。
#全局变量：函数外面定义的变量，函数内部可读；想要修改全局变量要写global。
num = 100 #全局变量
def fun():
    a = 10 #局部变量，函数外面拿不到
    global num
    num = 200

fun()
print(num)
# print(a) 报错！a只在函数内部存在


#函数文档字符串（docstring）
#给函数写说明，别人能看懂这个函数干什么、参数是什么。
def calculate_BMI(weight, height):
    """
    计算BMI身体质量指数
    :param weight: 体重(kg)
    :param height: 身高(m)
    :return: bmi数值
    """
    bmi = weight / height**2
    return bmi


#函数嵌套 & 函数可以作为参数（简单了解）
def outer():
    def inner():
        print("内部函数")
    inner()
outer()


#常见易错坑
#1.调用函数的时候，括号不能丢：calculate_BMI 只是函数本身，calculate_BMI() 才是执行。
#2.参数数量要匹配：定义 2 个形参，调用就要传 2 个实参（除非设置默认参数）。
#3.print 和 return 的区别：
#  print：只是在屏幕打印文字，不会把数据交给外面程序。
#  return：把结果返回出来，外面可以赋值给变量继续计算。
#4.很多新手混淆：函数内部 print，外部拿不到计算结果，一定要 return。


#匿名函数 lambda（认识即可）
#简短的小计算，不用写完整 def。
add = lambda x,y : x+y
print(add(2,3))




central_angle=160
radius=30
sector_area=(central_angle/360)*radius**2*3.14
print("此扇形的面积为"+str(sector_area))
print(f"此扇形的面积为{sector_area:.0f}")
print("此扇形的面积为{sector_area:.2f}".format(sector_area=sector_area))
print("此扇形的面积为{0:.3f}".format(sector_area))





def calculate_sector_area():      #函数定义 def 函数名(参数):
    central_angle=160
    radius=30
    sector_area=(central_angle/360)*radius**2*3.14
    print(f"此扇形的面积为{sector_area:.0f}")
calculate_sector_area()




def calculate_sector_area(central_angle,radius):
    sector_area=(central_angle/360)*radius**2*3.14
    print(f"此扇形的面积为{sector_area:.0f}")
calculate_sector_area(1,1000)
calculate_sector_area(1000,1)
calculate_sector_area(20,20)




def calculate_sector_area(central_angle,radius):
    sector_area=(central_angle/360)*radius**2*3.14
    print(f"此扇形的面积为{sector_area:.0f}")       #函数内部搭配 f‑string 格式化输出
    return sector_area
calculate_sector_area_1=calculate_sector_area(1,1000)
print(calculate_sector_area_1)




def calculate_BMI(weight,height):
    BMI=weight/height**2
    return BMI
BMI=calculate_BMI(95,1.81)
print(BMI)
if BMI<=18.5:
     print("此BMI值属于偏瘦范围")
elif 18.5<BMI<=25:
    print("此BMI值属于正常范围")
elif 25<BMI<=30:
    print("此BMI值属于偏胖范围")
else:
    print("此BMI值属于肥胖范围")






def calculate_BMI(weight, height):
    BMI = weight / height ** 2

    if BMI <= 18.5:
        category = "偏瘦"
    elif BMI <= 25:
        category = "正常"
    elif BMI <= 30:
        category = "偏胖"
    else:
        category = "肥胖"

    print(f"您的BMI分类为：{category}")
    return BMI               #return 返回结果（拿到函数输出值，可以赋值给变量）



result=calculate_BMI(95,1.81)         #调用函数、接收返回值 变量 = 函数(实参)
print(result)




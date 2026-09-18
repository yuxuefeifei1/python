##1. 三角函数易错知识点
##math.sin()、math.cos() 的参数是弧度，不是角度。
##如果你想使用角度计算，需要额外转换：
##math.sin(math.radians(30))
##2.运算符作用	                        示例
##  +	加法	                        5 + 2
##  -	减法	                        5 - 2
##  *	乘法	                        5 * 2
##  /	浮点除法（永远返回小数）        5 / 2 → 2.5
##  //	向下取整整除	                5 // 2 → 2
##  %	取余数（模运算）	        5 % 2 → 1
##  **	幂运算	                        3 ** 2 = 9
##3.复合赋值运算符（写代码高频使用）
##简化变量自更新写法：
##n = 10
##n += 2   # 等价于 n = n + 2
##n -= 3   # n = n - 3
##n *= 2   # n = n * 2
##n /= 2
##n //= 2
##n %= 2
##n **= 2
##4.math 库常用补充函数（搭配你现有三角函数、开方学习）
##import math
##math.fabs(-9.2)   # 浮点数绝对值
##math.floor(3.9)    # 向下取整 →3
##math.ceil(3.1)     # 向上取整 →4
##math.exp(2)        # e的2次方
##math.log(10)       # 自然对数
##math.log10(100)    # 以10为底对数
##math.tan(math.pi/4)# 正切函数
##math.radians(60)    # 角度 → 弧度
##math.degrees(math.pi) # 弧度 → 角度
##5.运算优先级（避免公式写错，求根公式非常依赖）
##优先级从高到低：
##括号 ()
##幂运算 **
##乘、除、取余 * / // %
##加、减 + -
##示例：不加括号会完全算错：
##6. 负数开平方的区别
##math.sqrt() 不支持负数，会直接报错；
##如果要计算复数根，需要导入 cmath 库：
##import cmath
##print(cmath.sqrt(-4))
##7. 四舍五入
##内置函数，不需要导入 math：
##round(3.1415, 2)  # 保留2位小数



import math   #导入标准数学库 import math
print(math.sin(1))
print(math.pi)     #常量调用：圆周率 math.pi
print(math.cos(math.pi))   #基础三角函数：正弦 math.sin()、余弦 math.cos()




a = 1
b = 9
c = 20
print((-b+math.sqrt(b**2-4*a*c))/(2*a))
print((-b-(b**2-4*a*c)**(1/2))/(2*a))




a = 1
b = 9
c = 20

x1 = (-b + math.sqrt(b**2 - 4*a*c)) / (2*a)   #平方根函数：math.sqrt()
x2 = (-b - math.sqrt(b**2 - 4*a*c)) / (2*a)

print(x1)
print(x2)

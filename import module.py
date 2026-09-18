#1、给模块 / 函数起别名 as（非常常用）
#①模块起别名
import statistics as st
data = [69,124,-32,27,217]
print(st.mean(data))
print(st.median(data))
#②函数起别名
from statistics import mean as avg, median as mid
data = [69,124,-32,27,217]
print(avg(data))
print(mid(data))



#2、三种导入方式对比（重点）
##写法	                               调用方式	                         优缺点
##import statistics	               statistics.mean()	         ✅不会名字冲突；代码写得长一点
##from statistics import mean,median     mean()	                         ✅写代码简短；⚠️如果自己定义同名变量，会覆盖函数
##from statistics import *	       mean()	                         ✅写得最短；❌不推荐，容易发生名字冲突，不知道函数来自哪个模块


#⚠️坑：如果你自己写一个变量叫mean = 100，后面再调用mean()就直接报错，函数被你的变量覆盖掉了。
from statistics import mean
mean = 100   # 自己定义变量mean，把导入的mean函数覆盖！
print(mean([1,2,3])) # 报错！数字100不是函数


#3、查看模块里面有什么东西
import statistics
print(dir(statistics)) # 打印这个模块全部可用函数名字


#4、部分导入：只导入一部分，不是全部
from statistics import mean, median, mode
# 只有mean、median、mode可以直接用，其他函数不能直接调用


#5、自己写的 py 文件怎么 import（本地模块）
#假如你当前文件夹有一个文件叫tools.py，里面写了函数：
# tools.py
def add(a,b):
    return a+b
#同目录另一个文件，就可以导入：
import tools
print(tools.add(2,3))

#或者
from tools import add
print(add(2,3))
#⚠️必须两个文件放在同一个文件夹下面，才能 import 成功！ 这是新手最高频踩坑。



#6、补充小规则
##1.import 一般统一写在代码最开头，习惯上不要写在循环、if 里面。
##2.如果模块不存在（拼写错、没有安装第三方库），报ModuleNotFoundError。
##标准库如statistics：Python 自带，直接 import，不用安装。
##第三方库如numpy：需要先在终端执行pip install numpy，才可以 import。



#7、容易混淆
##标准库：python 自带，直接 import（statistics、math、random）
##第三方库：需要 pip 安装之后才能导入










#import 语句
import statistics       #模块。函数名调用
median=statistics.median([69,124,-32,27,217])
mean=statistics.mean([19,-5,36])
print(median)
print(mean)


#from...import...语句
from statistics import median,mean          #导入指定函数，直接写函数名
median=median([69,124,-32,27,217])
mean=mean([19,-5,36])
print(median)
print(mean)



#from...import*
from statistics import*              #通配符，导入模块全部功能
median=median([69,124,-32,27,217])
mean=mean([19,-5,36])
print(median)
print(mean)














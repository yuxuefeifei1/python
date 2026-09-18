#1. 变量命名规则（很重要，避免报错）
#只能由字母、数字、下划线组成；
#不能以数字开头；
#严格区分大小写 Name 和 name 是两个变量；
#不能使用 Python 关键字（if、for、print、class等）。


#2. 推荐命名风格
#普通变量：小写下划线 student_score（蛇形命名，Python 标准）
#不要用拼音简写、无意义名字 a、b，尽量语义化


#3.num_int = 10        # 整数 int
#  num_float = 3.14    # 浮点数 float
#  text = "hello"      # 字符串 str
#  flag = True         # 布尔值 bool（True/False）
#  lst = [1,2,3]       # 列表
#  查看类型：print(type(变量名))

#4. 常量约定
#Python 没有真正不可修改的常量，行业约定全大写表示不要随意修改：
#MAX_SCORE = 100


#5. 变量删除（释放内存）
#temp = 666
#del temp  # 彻底删除变量，之后再使用会报错


#6. 易错点：可变类型和不可变类型（解释你数字 / 字符串不会联动变化的原理）
#字符串、数字、布尔：不可变类型，重新赋值只会改变变量指向，旧变量不受影响（和你代码里 my_ex 案例一致）
#列表、字典：可变类型，两个变量指向同一个对象时，修改内容会一起变化，给你示例：
#list1 = [1,2,3]
#list2 = list1
#list1.append(4)
#print(list2)  # 输出 [1,2,3,4]，会跟着变，新手很容易踩坑


#7.f-string 嵌入变量（替代 + 拼接，更常用）
#不推荐一直用 + 拼接字符串，标准写法：
#name = "张三"
#print(f"你好，{name}")




greet="你好，吃了吗，"   #字符串变量赋值
greet_Chinese=greet    # 变量引用赋值，两个变量指向同一个字符串
greet_English="You what's up，"    
greet=greet_English      # 重新给变量绑定新值
print(greet+'张三')     #字符串用 + 拼接
print(greet_Chinese+"张三")      # 字符串用 + 拼接




my_love=1111
my_ex=my_love
my_love=2222    #数字变量、重新赋值不会影响旧引用变量
print(my_ex)
print(my_love)



a, b, c = 10, 20, "测试文本"   # 一行给多个变量赋值
x = y = z = 99    # 多个变量赋同一个值
print(a)
print(b)
print(x)
print(y)





















#顺序省略写法
text = "姓名：{}，年份：{}".format("小张","马")


#同一个参数多次复用
text = "{0}，{0}新年大吉".format("小张")


# :< 左对齐 :>右对齐 :^居中
print("{:^10}".format("新年快乐"))


#表达式直接嵌入 {} 内部
a = 5
b = 3
print(f"总和：{a + b}")


#数字格式化（和 format 通用）
score = 3.251
print(f"绩点：{score:.2f}") #保留2位小数
print(f"{score:.1f}") #保留1位小数


#千位分隔符（大数展示
num = 1234567
print(f"{num:,}") #输出 1,234,567


#字符串 + 变量：只适合简单拼接，大量文本麻烦，不支持格式控制
#"{}".format()：兼容性最强，老旧 Python 版本可用
#f""：语法简洁、可读性最高，日常开发首选


#如果文本里需要输出大括号 { }，f-string /format 需要写两层括号
print(f"{{name}}") #输出 {name}


#.items() 同时拿到 key 和 value（你已经在用）
#拓展：.keys() 只获取键，.values()只获取值


#f-string 大括号里面只能放变量 / 表达式，不能放完整语句
#小数格式化 :.2f 会自动四舍五入
#format 位置参数数量必须和传入变量数量匹配，否则报错


#%格式化（老式写法，很多旧代码能见到）
name = "小王"
print("你好 %s" % name)










contacts=["小林","小李","小王","小张"]
for name in contacts:      #搭配 for 循环遍历列表、字典items()批量生成文本
    message_contact=name + "：岁始之乐，点翠画柳喜开颜。\
云开雾散，良辰美景共团圆。祝福" + name + \
"及家人新年快乐，平安顺遂，虎年大吉！🧨"             #字符串直接拼接 +
    print(message_contact)



contacts=["小林","小李","小王","小张"]
year="马"
for name in contacts:
    message_contact="""
律回春渐，新元肇启。
新岁甫至，福气东来。
金""" + year + """贺岁，欢乐祥瑞。
金""" + year + """敲门，五福临门。
给""" + name + """及家人拜年啦！
新春快乐，""" + year + """年大吉！"""
    print(message_contact)



contacts=["小林","小李","小王","小张"]
year="马"
for name in contacts:
    message_contact="""        
律回春渐，新元肇启。
新岁甫至，福气东来。
金{0}贺岁，欢乐祥瑞。
金{0}敲门，五福临门。
给{1}及家人拜年啦！
新春快乐，{0}年大吉！     
""".format (year,name)      #.format() 格式化  位置参数 {0} {1}    位置参数 {0} {1}
    print(message_contact)





contacts=["小林","小李","小王","小张"]
year="马"
for name in contacts:
    message_contact="""
律回春渐，新元肇启。
新岁甫至，福气东来。
金{year}贺岁，欢乐祥瑞。
金{year}敲门，五福临门。
给{name}及家人拜年啦！
新春快乐，{year}年大吉！
""".format (year=year,name=name)
    print(message_contact)






contacts=["小林","小李","小王","小张"]
year="马"
for name in contacts:
    message_contact=f"""
律回春渐，新元肇启。
新岁甫至，福气东来。
金{year}贺岁，欢乐祥瑞。
金{year}敲门，五福临门。
给{name}及家人拜年啦！
新春快乐，{year}年大吉！     
"""
    print(message_contact)       #f-string（格式化字符串字面量）


    
gpa_dict={"小林":3.251,"小李":3.021,"小张":3.011,"小王":2.999}
for name,gpa in gpa_dict.items():
    message="{0}你好，你当前的绩点为:{1:.2f}".format(name,gpa)
    print(message)







gpa_dict={"小林":3.251,"小李":3.021,"小张":3.011,"小王":2.999}
for name,gpa in gpa_dict.items():
    message=f"{name}你好，你当前的绩点为:{gpa:.2f}"     #基础小数格式化 :.2f
    print(message)








    





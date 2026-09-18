print('你好')    #单引号 ' ' 包裹字符串


print("你好，"+"你还好吗，"+"对的，就是你！")   #字符串用 + 拼接，+ 只能拼接字符串


print("let's go")    #  单双引号转义


print('let\'s go')      #单引号内部带 ' 用转义符 \'


print('我是第一行\n我是第二行')    #\n 转义换行


print("""云绕青山远尘哗，
一窗风月伴清茶。
平生不逐浮华事，
静看庭前落晚霞""")      #三引号 """...""" 多行文本，自动换行


name="小明"
print("名字：",name,"年龄",18)   #逗号可以放任意类型：数字、变量都行


price=8
name="纸巾"
print(f"{name}的价格是：{price}元")   #f-string 格式化把变量直接嵌入文本


print(1, 2, 3, sep="---")   #多个内容之间的分隔符 sep


print("姓名\t年龄")              #\\：输出一个反斜杠
print("D:\\Desktop\\test.py")    #\t：制表缩进（相当于按 Tab）
                                 #\"：在双引号字符串里输出双引号


path = r"D:\Users\yuxue\Desktop\print.py"
print(path)   #原始字符串 r""，取消所有转义


print("第一段", end="")
print("紧挨着")    #控制末尾符号：end 参数























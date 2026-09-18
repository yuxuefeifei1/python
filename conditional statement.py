#1.三元表达式（简洁写法，if 简写）
#
#2.pass 占位语句（语法必备）,如果暂时不想写分支内部代码，防止程序报错
#if mood_index >=60:
#    pass # 暂时预留位置，后续补充代码
#else:
#   print("别打游戏")
#
#3.变量 = 满足条件的结果 if 条件 else 不满足条件的结果
#mood_index = 70
#res = "可以打游戏" if mood_index >= 60 else "别打了"
#print(res)











#条件语句
mood_index=float(input("对象今天的心情指数是："))
if mood_index>=60:
    print('恭喜，今晚应该可以打游戏,去吧皮卡丘')
else:  #mood_index<60
    print('为了自个儿小命，还是别打了')



#嵌套条件语句
mood_index=float(input("对象今天的心情指数是："))
is_at_home=input("是否在家（输入YES/NO）:")=="YES"
if mood_index<60:
    if is_at_home:
        print("为了自个儿小命，还是别打了")
    else:
        print("恭喜，今晚应该可以打游戏,去吧皮卡丘")
else:
    print('恭喜，今晚应该可以打游戏,去吧皮卡丘')




#多个条件判断语句
user_weight=float(input("请输入您的体重（单位：kg）:"))
user_height=float(input("请输入您的身高（单位：m）:"))
user_BMI=user_weight/(user_height)**2
print("您的BMI值为"+str(user_BMI))
if user_BMI<=18.5:
    print("此BMI值属于偏瘦范围")
elif 18.5<user_BMI<=25:
    print("此BMI值属于正常范围")
elif 25<user_BMI<=30:
    print("此BMI值属于偏胖范围")
else:
    print("此BMI值属于肥胖范围")


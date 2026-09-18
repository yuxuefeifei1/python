#1.input() 默认接收字符串，必须用 float() / int() 强制转为数字才能计算

#2.一行同时接收多个输入（高频用法）
#  weight, height = map(float, input("输入体重 身高，空格隔开：").split())





user_weight=float(input("请输入您的体重（单位：kg）:"))
user_height=float(input("请输入您的身高（单位：m）:"))
user_BMI=user_weight/(user_height)**2
print("您的BMI值为"+str(user_BMI))

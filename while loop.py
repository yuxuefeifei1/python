##1.无限循环 while True:无限循环必须设置退出条件，否则程序卡死。
##while True:
##    msg = input("输入quit结束：")
##    if msg == "quit":
##        break
##2.致命坑：continue前面一定要先更新计数器，否则死循环
### 错误示范！死循环
##i = 0
##while i < 5:
##    if i == 2:
##        continue
##    print(i)
##    i = i + 1
### 正确写法
##i = 0
##while i < 5:
##    i = i + 1
##    if i == 2:
##        continue
##    print(i)
##3.循环正常全部执行完毕，没有被 break 打断，才执行 else 代码；
##一旦触发break，else 部分不会运行。
##i = 0
##while i < 5:
##    if i == 10:
##        break
##    i += 1
##else:
##    print("循环完整跑完，没有触发break")
##4 ✅优先用 for 循环：
##  循环次数确定、遍历列表 / 字符串 / 字典 /range 序列
##  ✅优先用 while 循环：
##  循环次数不确定，依靠外部条件决定什么时候结束（你的平均值程序就是典型案例）





#for循环  和while循环
list1=["你","好","吗","兄","弟"]
for char in list1:
    print(char)

for i in range(len(list1)):
    print(list1[i])

i=0
while i<len(list1):
    print(list1[i])
    i=i+1







print("这是一个求平均值的小程序")
total=0
count=0
user_input=input("请输入数字（输入完成后请按q）:")
while user_input !="q":
    num=float(user_input)
    total=total+num
    count=count+1
    user_input=input("请输入数字（输入完成后请按q）:")
if count==0:
    result=0
else:    
    result=total/count
print("您输入的数字平均值为"+str(result))

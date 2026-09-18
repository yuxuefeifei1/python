#for 变量名 in 可迭代对象


#表格循环
temperature_list=[36.1,36.2,36.3,36.4,36.5,36.6,36.7,36.8,36.9,37.0]
for temperature in temperature_list:
    if temperature>=36.5:
        print(temperature)
        print("完球了")




#字典循环
#temperature_dict.keys()     #所有键
#temperature_dict.values()      #所有值
#temperature_dict.items()    #所有键值对

        
temperature_dict={
    "张三": 36.2,
    "李四": 36.8,
    "王五": 37.1,
    "赵六": 36.5,
    "钱七": 36.3,
    "孙八": 36.9,
    "周九": 36.4,
    "吴十": 37.2,
    "郑十一": 36.6,
    "冯十二": 36.7}        

for staff_id,temperature in temperature_dict.items():
    if temperature>=37.0:
        print(staff_id)

#等同于
#for temperature_tuple in temperature_dict.items():
#    staff_id = temperature_tuple[0]
#    temperature = temperature_tuple[1]
#    if temperature >= 38:
#       print(staff_id)


total=0
for i in range(1,101):
    total=total+i
    print(total)
print(total)


#    break：直接终止整个 for 循环
#    continue：跳过当前这一轮，直接进入下一次循环
temperature_list=[36.1,36.2,36.3,36.4,36.5,36.6]
for temperature in temperature_list:
    if temperature < 36.3:
        continue   # 低于36.3，跳过后面代码
    if temperature >= 36.6:
        break      # 遇到36.6直接结束循环
    print(temperature)



#    enumerate () 遍历列表，同时拿到下标 + 元素
#    你现在只能拿到数值，无法知道是第几个数据
temperature_list=[36.1,36.2,36.3]
for index,temp in enumerate(temperature_list):
    print(f"第{index+1}条体温：{temp}")


    
#    range 完整三种格式    
range(10)          # 0~9
range(1,10)        # 1~9
range(1,10,2)      # 1,3,5,7,9  第三个参数=步长



#    for ... else 结构（Python 独有）
#    循环正常跑完、没有被 break 打断，才执行 else；遇到 break 则不执行 else    
temperature_dict={
    "张三": 36.2,
    "李四": 36.3}
for name,temp in temperature_dict.items():
    if temp >= 37:
        print("发现发热人员")
        break
else:
    print("全部人员体温正常")













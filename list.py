##1..insert(下标, 内容)：在指定位置插入元素
##   shopping_list.insert(0,"鼠标") # 在最前面插入
##2..pop(索引)：根据下标删除元素，可以拿到被删掉的值
##   item = shopping_list.pop(2)
##   区分：remove() 按内容删；pop() 按下标删
##3..clear() 清空整个列表
##   shopping_list.clear()
##4..index(元素)：查找元素对应的下标，找不到会报错
##  .count(元素)：统计这个元素在列表出现多少次
##   nums = [1,1,2,3]
##   print(nums.count(1)) #输出2
##5.+ 拼接两个列表
##   a = [1,2]
##   b = [3,4]
##   c = a + b
##6.* 重复列表
##   print([0]*5) # [0,0,0,0,0]
##7.列表复制易错点（浅拷贝入门）
##   new_list = shopping_list.copy()
##8.成员判断 in
##   if "硬盘" in shopping_list:
##       print("存在")
##   if "耳机" not in shopping_list:
##       print("不存在")  
##9.(升序)
##  sorted(列表)：返回新列表，原列表不变
##  列表.sort()：直接修改原本列表，无返回值   
##   nums = [3,1,4,2]
##   a = sorted(nums)
##   print("sorted结果：", a)
##   print("原nums：", nums)
##
##   nums.sort()
##   print("sort之后nums：", nums)
##10.(降序)

##   列表.sort(reverse=True)
##   sorted(列表, reverse=True)
##   score = [88, 62, 95, 74, 88]
##
##   # 默认升序
##   score1=sorted(score)
##   print(score1)  # [62, 74, 88, 88, 95]
##
##   # 降序写法（你需要修改成这样）
##   score.sort(reverse=True)
##   print(score)   # [95, 88, 88, 74, 62]
















   
shopping_list=[]   #创建空列表 []
shopping_list.append("键盘")   #.append() 末尾新增元素
shopping_list.append("键帽")    
shopping_list.remove("键帽")    #.remove() 删除指定内容元素
shopping_list.append("音响")
shopping_list.append("电竞椅")
shopping_list[1]="硬盘"     #列表[下标] = 值 修改指定位置元素


print(shopping_list)
print(len(shopping_list))    #len(列表) 获取列表长度
print(shopping_list[0])    #列表[索引] 取出单个元素


price=[799,1024,200,800]
max_price=max(price)    #max() min() 求数字列表最大、最小值
min_price=min(price)
sorted_price=sorted(price)   #sorted() 对列表排序（生成新列表，不改动原列表）
print(max_price)
print(min_price)
print(sorted_price)


lst = [10,20,30]
print(lst[-1])  # 最后一个元素30
print(lst[-2])  # 倒数第二个20


lst = [1,2,3,4,5]
print(lst[1:3])
print(lst[::-1]) # 列表反转


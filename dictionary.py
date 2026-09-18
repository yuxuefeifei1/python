##关键易错知识点
##1.字典的键必须是不可变类型：字符串、数字可以；列表 list不能当做键
##2.执行 query in slang_dict，只会检索键，不会检索值
##3.字典无序（Python3.7 以后，会记住写入顺序，但不要当作有序容器使用）
##4.同一个字典内，键不能重复；重复书写后面的值覆盖前面


slang_dict={"韧性":"抗压能力，逆境反弹，作文万能高级词",
            "数字游民":"远程办公、不受地域束缚的自由年轻人",
            "具身智能":"实体人形机器人，人工智能新概念"}   #创建字典 {键:值, ...}
slang_dict["赛博对账"]="网上对比各国生活，跨文化交流"
slang_dict["活人感"]="讨厌流水线AI话术，偏爱真诚自然的性格"
slang_dict["预制XX"]="流水线标准化、没有个性的人或内容"
slang_dict["苏超"]="地方城市体育联赛，地域文化自信"
slang_dict[" 匆匆忙忙，连滚带爬"]="理想从容安逸，现实奔波辛苦"
slang_dict[" 邪修"]="不走正统、野路子但是效率极高的方法"
slang_dict[" 魔丸&灵珠"]="：魔丸=叛逆个性，灵珠=乖巧稳重，形容两种人格"

query=input("请输入您想要查询的流行语")     #input() 获取查询内容，简易字典查询器
if query in slang_dict:           #in 判断键是否存在字典中
    print("您查询的"+query+"含义如下")
    print(slang_dict[query])      #字典[键] 根据键获取对应值
else:
    print("您查询的流行语尚未收录")
    print("当前本词典收录词条数为："+str(len(slang_dict))+"条")       #len(字典) 统计字典里面键值对总数


del slang_dict["韧性"]   # 方式1：del 删除指定键
content = slang_dict.pop("苏超") # 方式2：pop(键) 删除，并且拿到被删除的值（和列表pop很像
 slang_dict.clear()     # 方式3：clear() 清空字典所有内容


 print(slang_dict.get("特种兵旅游"))   # 找不到键，默认返回None
 print(slang_dict.get("特种兵旅游","没有收录这个词"))   # 找不到键，自定义提示文字


 slang_dict.keys()    # 获取所有键
slang_dict.values()  # 获取所有值
slang_dict.items()   # 获取所有 (键,值) 配对


new_words = {"搭子":"结伴同行的伙伴","情绪价值":"提供情感安慰"}   # 字典合并 update ()
slang_dict.update(new_words)

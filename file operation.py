#read
f=open(r"D:\Users\yuxue\Desktop\format string.py","r",encoding="utf-8")
print(f.read())


f=open(r"D:\Users\yuxue\Desktop\format string.py","r",encoding="utf-8")
print(f.read(10))
print(f.read(10))


#readline
f=open(r"D:\Users\yuxue\Desktop\format string.py","r",encoding="utf-8")
print(f.readline())
print(f.readline())



f=open(r"D:\Users\yuxue\Desktop\format string.py","r",encoding="utf-8")
line=f.readline()
while line !="":
    print(line)
    line=f.readline()


#readlines
f=open(r"D:\Users\yuxue\Desktop\format string.py","r",encoding="utf-8")
print(f.readlines())



f=open(r"D:\Users\yuxue\Desktop\format string.py","r",encoding="utf-8")
lines=f.readlines()
for line in lines:
    print(line)

f.close()




with open(r"D:\Users\yuxue\Desktop\format string.py","r",encoding="utf-8") as f:
    print(f.read())




#write
with open(r"D:\Users\yuxue\Desktop\poem.txt","w",encoding="utf-8") as f:
    f.write("我欲乘风归去，\n")
    f.write("又恐琼楼玉宇，\n")
    f.write("高处不胜寒。\n")

with open(r"D:\Users\yuxue\Desktop\poem.txt","a",encoding="utf-8") as f:
    f.write("起舞弄清影，\n")
    f.write("何似在人间。")















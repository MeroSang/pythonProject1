# 1、请用代码实现如下进制的转换。
"""
#v1 = 675 二进制字符串类型
v1 = 675
v1= bin(675)  #是字符串类型
print(v1)

#v2 = "0b11000101"   转换十进制  整型
v2 = "0b11000101"
v2=int(v2,base=2)
print(v2)

#v3 = "1100101"    转换为十进制 整型
v3 = "1100101"
v3 = int(v3,base=2)
print(v3)
"""

# 2、现有v1=123 v2=456 ,请将这两个值转换为二进制，并将其二进制中的前缀去掉，将两个二进制数拼接起来，转换为整型（十进制）
"""
v1 = 123
v2 = 456
v1 = bin(v1)
v2 = bin(v2)
v1 = v1.replace("0b","")
v2 = v2.replace("0b","")
v3 = v1+v2
v3 = int(v3,base=2)
print(v3)
"""

# 3、现有v1=123 v2=456 ,请将这两个值转换为二进制，并将其二进制中的前缀去掉，再补足为2个字节（16位），将两个二进制数拼接起来，转换为整型（十进制）
"""
v1 = 123
v2 = 456
v1 = bin(v1)
v2 = bin(v2)
v1 = v1.replace("0b","")
v2 = v2.replace("0b","")
v1 = v1.zfill(16)
v2 = v2.zfill(16)
v3 = v1+v2
v3 = int(v3,base=2)
print(v3)
"""

# 4、列举你所知道的哪些数据类型的值是false
"""print(bool([]))
print(bool(""))
print(bool(0))
"""

# 5、  456   666  345

# 6、将赌博、黑钱替换位**，最后输出
"""char_list = ["赌博", "黑钱"]
msg = input("请输入您想传输的信息：")
for char in char_list:
    msg = msg.replace(char, "**")
print(msg)
"""

# 7、
# 移除变量的两边的空格
"""
name = " Mero leNB "
name = name.strip()
print(name)
"""

# 变量是否以"Me"开头，并输出结构；
"""name = "Mero leNB"
if name[0:2] == "Me":
    print(True)
else:
    print(False)

if name.startswith("Me"):
    print(True)
else:
    print(False)
"""

# 判断是否以“NB”结尾，并输出结果；
"""name = "Mero leNB"
if name[7:] == "NB":
    print(True)
else:
    print(False)

if name.endswith("NB"):
    print(True)
else:
    print(False)
"""

# 所有的“e”替换成“P”：
"""name = "Mero leNB"
name = name.replace("e","p")
print(name)
"""

# 根据所有的”e“进行切割，并输出结果
"""name = "Mero leNB"
name_list = name.split("e")
print(name_list)
"""

# 第一个”e“进行切割，输出结果
"""
name = "Mero leNB"
name_list = name.split("e",1)
print(name_list)
"""

# name 变量全大写 全小写
"""name = "Mero leNB"
name1 = name.upper()
print(name1)
name2 = name.lower()
print(name2)
"""

# 8、实现字符串翻转
"""name = "Mero leNB"
name = name[-1::-1]
print(name)
"""

# 9、有字符串s=”123a4b5c“
# 切片”123“
"""s="123a4b5c"
s1 = s[0:3]
print(s1)

#切片"a4b"
s2 = s[3:6]
print(s2)

#切片”c“
s3= s[-1:]
print(s3)

#切片”ba2“
s4 = s[-3::-2]
print(s4)
"""

# 10、while循环实现字符串message="伤情最是晚凉天，憔悴厮人不堪言"中每个字进行输出
"""
message="伤情最是晚凉天，憔悴厮人不堪言"
num = 0
while num < len(message):
    data = message[num]
    print(data)
    num+=1
"""

# 11、for循环实现字符串message="伤情最是晚凉天，憔悴厮人不堪言"中每个字进行输出
"""message="伤情最是晚凉天，憔悴厮人不堪言"
for char in message:
    print(char)
"""

# 12、for、rang实现字符串message="伤情最是晚凉天，憔悴厮人不堪言"中每个字进行  倒叙输出
"""
message="伤情最是晚凉天，憔悴厮人不堪言"
num = range(len(message) ,-1,-1)
for char in num:
    print(message[char])
"""

# 13、for循环实现输出倒计时效果， 输出内容一次是”倒计时3秒“。。。。
"""
num = range(3, 0, -1)
for char in num:
    data = "倒计时{0}秒".format(char)
    print(data)
"""

# 14、用户输入文本，计算”浪”出现的次数，并输入结果。
"""
data = input("请输入您想传递的信息：")
char_list= data.split("浪")
print(len(char_list)-1)
"""

# 15、获取用户的两组内容，并提取其中数字，然后实现数字的相加
data1 = input("请输入第一组内容：")
data2 = input("请输入第二组内容：")
num1 = ""
num2 = ""
for char1 in data1:
    if char1.isdecimal():
        num1 = num1 + char1
        continue
char2: str
for char2 in data2:
    if char2.isdecimal():
        num2 = num2 + char2
        continue
num1 = int(num1)
num2 = int(num2)
print(num1 + num2)

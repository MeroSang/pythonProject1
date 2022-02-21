# 1、写代码实现判断用户输入的值是否以“ai”开头，如果是则输出“是的” 否则 输出 “不是的”
"""
msg=input("请输入相应的值：")
if msg.startswith("ai"):
    print("是的")
else:
    print("不是的")
"""

# 2、判断用户输入的值是否以“Nb”结尾，如果是则输出“是的” 否则 输出 “不是的”
"""
msg=input("请输入相应的值：")
if msg.endswith("Nb"):
    print("是的")
else:
    print("不是的")
"""

# 3、将name变量的对应的值中的所有 “i” 替换成 “p”，并输出结果
"""
name = input("请输入你的名字：")
data = name.replace("i", "p")
print(data)
"""

# 4、对用户输入的值进行判断，是否为整数，如果是请转换为整型输出，否则输出“请输入数字”
"""
while True :
    msg = input("请输入数字：")
    if msg.isdecimal():
        data=int(msg)
        print(data)
        break
    else:
        print("请输入数字！！！")
"""

# 5、对输入的数据使用”+“切割，判断输入的值是否都是数字？提示：用户输入的格式必须是以下+连接的格式，如 5+9、alex+999
"""msg = input("请输入两组数字，且中间以”+“连接，如5+9：")
msg_list = msg.split("+")
data1 = msg_list[0]
data2 = msg_list[1]
if data1.isdecimal() == True and data2.isdecimal() == True:
    print("输入正确")
else:
    print("请按照格式输入数字")
"""

# 6、对输入的数据使用”+“切割，判断输入的值是否都是数字？将俩个数字相加并输出。提示：用户输入的格式必须是以下+连接的格式
"""
msg = input("请输入两组数字，且中间以”+“连接，如5+9：")
if "+" in msg :
    msg_list = msg.split("+")
    data1 = msg_list[0]
    data2 = msg_list[1]
    if data1.isdecimal() == True and data2.isdecimal() == True:
        answer = int(data1) + int(data2)
        print(answer)
    else:
        print("请按照格式输入数字")
else:
    print("请按照格式输入数字")
"""

#7、写一段代码实现两个数相加。（需去除空白）
"""
msg = input("请输入两组数字，且中间以”+“连接，如5+9：")
if "+" in msg :
    msg_list = msg.split("+")
    data1 = msg_list[0]
    data2 = msg_list[1]
    data1 = data1.strip()
    data2 = data2.strip()
    if data1.isdecimal() == True and data2.isdecimal() == True:
        answer = int(data1) + int(data2)
        print(answer)
    else:
        print("请按照格式输入数字")
else:
    print("请按照格式输入数字")
"""

#8、补充代码实现用户认证。需求：提示用户输入手机号、验证码，全部验证成功之后才算登录成功（验证码大小写不敏感）
"""
import random
code=random.randrange(1000,9999)
member=input("请输入你的手机号：")
msg = "欢迎登录Python系统，您的验证码为{0}，手机号为：{1}".format(code,member)
print(msg)
data1=input("请输入验证码：")
data2=data1.upper()
if int(data2) == code and member == "13260901296":
    print("登陆成功")
else:
    print("登录失败")
"""

#9、补充代码实现数据拼接
data_list = ["游泳","健身","高尔夫"]
while True:
    hobby = input("请输入你的爱好（Q/q退出）：")
    if hobby.upper() == "Q":
        break
    else:
        data_list.append(hobby)
        data_list_new = "、".join(data_list)
        print(data_list_new)
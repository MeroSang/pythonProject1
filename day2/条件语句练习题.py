# 1、练习题1  名字密码等于***，输入登陆成功
"""
name = input("请输入用户名：")
code = input("请输入密码：")
if name == "Mero" and code == "uuu":
    print("登陆成功")
else:
    print("登录失败")
"""

# # 2、练习题2:猜数字，判断大于10 猜错啦；否则输出猜对啦
"""
number=input("请输入猜测的数字：")
if int(number)>10:
    print("猜错啦")
else:
    print("猜对啦")
"""

# 3、练习题3：输入一个数字，判断是否为偶数；输出偶偶偶数，否则奇奇奇数
number=input("请输入一个数字：")
if int(number)%2==0:
    print("偶偶偶数")
else:
    print("奇奇奇数")
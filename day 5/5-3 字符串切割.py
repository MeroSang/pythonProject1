"""data="Mero|uuu|365314956@qq.com"
v1=data.split("|")
print(v1)     #['Mero', 'uuu', '365314956@qq.com']

v2=data.split("|",1)
print(v2)     #['Mero', 'uuu|365314956@qq.com']

v3=data.rsplit("|",1)
print(v3)     #['Mero|uuu', '365314956@qq.com']
"""

"""num=3
data="Mero,uuu"
user_list=data.split(",")
while num>=1:
    name = input("请输入用户名：")
    password = input("请输入密码：")
    if name == user_list[0] and password == user_list[1]:
        print("登录成功")
        break
    else:
        num -= 1
        print("请输入正确的用户名与密码,您还有{0}次机会".format(num))
"""

data_list = ["我的", "名字叫", "Mero"]
msg = "".join(data_list)
print(msg)

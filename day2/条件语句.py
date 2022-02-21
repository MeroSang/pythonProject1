# username=input("请输入用户名：")
# password=input("请输入密码：")
# if username =="Mero" and password == "666":
#     print("登陆成功")
# else:
#     print("登陆失败")

# number = input("请输入数字：")
# if int(number) % 2 == 1!=0:
#     print("数字为奇数")
# else:
#     print("数字为偶数")

number = input("请输入数字：")
data = int(number) % 2 == 1 != 0
if data:
    print("数字为奇数")
else:
    print("数字为偶数")

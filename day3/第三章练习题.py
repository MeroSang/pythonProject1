# 1、判断true or false
'''data=1 > 1 or 3 < 4 or 4 >5 and 2 > 1 and 9 > 8 or 7 < 6
     #true
print(data)
'''

'''data=not 2 > 1 and 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6
#false
print(data)
'''

# 2、求逻辑语句的值
'''data= 8 or 3 and 4 or 2 and 0 or 9 and 7
#     8
print(data)
'''

'''data=0 or 2 and 3 and 4 or 6 and 0 or 3
#    4       
print(data)
'''

# 3 输出结果
"""print(6 or 2 > 1) #6
print(3 or 2 > 1) #3
print(0 or 5 < 4) #False
print(5 < 4 or 3) #3
print(2 > 1 or 6) #True
print(3 and 2 > 1) #True
print(0 and 3 > 1) #0
print(2 > 1 and 3) #3
print(3 > 1 and 0) # 0
print(3 > 1 and 2 or 2 < 3 and 3 and 4 or 3 >2) #2
"""

# 4、实现用户登录系统，并且要支持连续三次输错之后直接退出，并且在每次输错误时显示剩余错误次数（提示：使用字符串格式化）
"""num = 3
while num > 0:
    name = input("请输入用户名：")
    password = input("请输入密码：")
    if name == "Mero" and password == "uuu":
        print("登陆成功，欢迎使用")
        break
    else:
        num -= 1
    print(f"输入错误，你还有{num}次机会")
"""

# 5、猜年龄游戏 ： 允许用户最多尝试3次，3次都没猜对的话，直接退出；如果猜对了，打印恭喜并推出
"""num = 3
while num > 0:
        age = input("请输入猜测的年龄：")
        if age == "18":
            print("恭喜，你猜对了")
            break
        else:
            num -= 1
        print(f"输入错误，你还有{num}次机会")
"""

# 6、猜年龄升级版：允许用户最多尝试3次，每尝试3次后，如果还没猜对，就问用户是否还想玩，如果回答Y，就继续让其猜3次，
# 以此往复，如果回答N，就退出程序，如果猜对了，就直接退出
num = 3
while num > 0:
    age = input("请输入猜测的年龄：")
    if age == "18":
        print("恭喜，你猜对了")
        break
    else:
        num -= 1
    print(f"输入错误，你还有{num}次机会")
    if num == 0:
        data = input("如果还想继续请输入Y，不想继续输入N:")
        if data == "Y":
            num=3
            continue
        else:
            break
# 1、猜数字66
"""
flag = True
while flag:
    num=input("请输入猜测的理想数字：")
    if num=="66":
        print("猜测结果正确")
        flag = False
    elif num > "66" :
        print("猜测的结果大了")
    else:
        print("猜测结果小了")

print("结束")

"""

# 2、使用循环输出1-100所有整数
"""
num = 1
while num <= 100:
    print(num)
    num = num + 1
"""

# 3、10以内整除7以外的整数
"""
num = 1
while num<=10:
    if num % 7 !=0:
        print(num)
    num=num+1
"""

# 4、输出1-100内所有奇数
"""
num=1
while num<=100:
    if num % 2==1:
        print(num)
    num=num+1
"""

# 5、输出1-100所有偶数
"""
num=1
while num<=100:
    if num % 2==0:
        print(num)
    num=num+1
"""

# 6、求1-100的所有整数的和
"""
num=1
total=0
while num<=100:
    total=total+num
    num = num + 1
print(total)
"""

# 7、输出10-1的所有整数
"""
num = 10
while num >= 1:
    print(num)
    num = num - 1
"""

# 8、思考题：求1~100以内所有整数这样的结果：1-2+3—4+5-6=？
num = 1
total = 0
while num <= 100:
    if num % 2 == 1:
        total = total + num
        num = num + 1
    else:
        total = total - num
        num = num + 1
print(total)

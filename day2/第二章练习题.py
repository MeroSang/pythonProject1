#-*- coding:UTF-8 -*-# 1、修改解释器默认编码

# 2、输出
"""
print("文能提笔安天下，")
print("武能上马定乾坤。")
print("心存谋略何人胜，")
print("古今英雄唯是君。")
"""

# text = """
# 文能提笔安天下，
# 武能上马定乾坤。
# 心存谋略何人胜，
# 古今英雄唯是君。
# """
# print(text)

# 3、变量名三个规范：
# 变量名只能由字母、数字、下划线组成
# 不能以数字开头
# 不能用python内置的关键字

# 4、设定一个理想数字：66，用户输入大于66，显示猜测结果多大；如果小于66，猜测结果小了；等于66，猜测结果正确
"""num = input("请输入猜测的理想数字：")
if num == "66":
    print("猜测正确")
elif num > "66":
    print("猜测结果大了")
else:
    print("猜测结果小了")
"""

# 5、根据输入的成绩，分为5个等级，与分数的对应关系如下，
# A:90-100 B:80-89 C:60-79 D:40-59 E:0-39
code = input("请输入你的分数：")
num = int(code)
if 89 < num < 101:
    print("你的等级为A")
elif 79 < num < 90:
    print("你的等级为B")
elif num > 59 and num < 80:
    print("你的等级为C")
elif num > 39 and num < 60:
    print("你的等级为D")
elif num > -1 and num < 40:
    print("你的等级为E")
else:
    print("输入的数字错误")

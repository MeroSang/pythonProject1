# 将用户随机输入的3位数字，按照从小到大排序，输出排序结果
"""
data1 = input("请输入数字1：")
data2 = input("请输入数字2：")
data3 = input("请输入数字3：")
if data1 <= data2 :
    if data2 <= data3:
        print(data1,data2,data3)
    elif data1 > data3:
        print(data3,data1,data3)
else:
    if data2 <= data3:
        print(data2, data3, data1)
    elif data3 > data1:
        print(data2, data1, data3)
"""

# 编写一个程序，计算a + aa + aaa + aaaa的值，a为用户输入的数字。
# 例如：假设为程序提供了以下输入：9 ，然后，计算9+99+999+9999，最后输出应该是： 11106
"""a = input("请输入一个值：")
a1 = a+a
a2 = a+a+a
a3 = a+a+a+a
print(int(a)+int(a1)+int(a2)+int(a3))
"""

# 给你一个字符串s，逐个翻转字符串中的所有单词 。
# 单词是由非空格字符组成的字符串。s中使用至少一个空格将字符串中的单词分隔开。
# 示例：
# 输入：s = "Alice does like Python course"
# 输出："course Python like does Alice"
s = input("请输入一个由非空格字符组成的字符串：")
s = s.split(" ")
reserve_s = s[::-1]
reserve_s = " ".join(reserve_s)
print(reserve_s)
result = ""
for char in s:
    result = char + " " + result
print(result)

"""
msg = "来做点dp交易"
print(len(msg))
num = 0
while num < len(msg):
    value = msg[num]
    print(value)
    num += 1
"""

msg = "来做点dp交易"
for i in msg:
    if i == "d":
        continue
    else:
        print(i)
ban_list=["艹","fuck","赌博"]
data=input("请输入你想传递的信息：")
for item in ban_list:
    data=data.replace(item,"**")
print(data)
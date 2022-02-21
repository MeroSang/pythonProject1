name = "我的名字叫Mero"
data = name.encode("utf-8")
# 打开一个文件
file_object = open("log.txt", mode="wb")
# 在文件中些内容
file_object.write(data)
# 关闭文件
file_object.close()

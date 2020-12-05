# 打开文件
# w模式,写入时文件不存在新建
# a模式,追加
# r模式,只读
# rb模式,二进制读
# file = open("../test.txt", "w")
# file.write("你好,世界!")


# 读取制定的字符,指针从头开始
file = open("../test.txt", "r")
content = file.read(4)
print(content)
file.close()

# 读取一行
file = open("../test.txt", "r")
content = file.readline()
print(content)
file.close()

# 读取n行
file = open("../test.txt", "r")
content = file.readlines()
print(content)
file.close()


import os
# 重命名 
os.rename("", "")

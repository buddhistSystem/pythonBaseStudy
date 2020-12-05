# 异常捕获
import time

try:
    file = open("../test.txt", "r")
    try:
        while True:
            content = file.readline()
            if len(content) == 0:
                break
            time.sleep(2)
            print(content)
    finally:
        file.close()
        print("文件关闭")
except Exception as result:
    print(result)
print("end")


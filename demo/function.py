# 函数

def printInfo(name):
    print("-------方法执行---------")
    print("     hello", name)
    print("-------执行结束---------")


# 带一个返回值
def getUserInput():
    inputStr = input("请苏入一个数字:")
    print("用户输入了:", inputStr)


# 多个返回值
def divid(a, b):
    shang = a // b
    yushu = a % b
    return shang, yushu


def printMyStr():
    print("*"*20)

def printMyNumStr(num):
    i = 0
    while i< num:
        printMyStr()
        i += 1

# 在函数中使用全局变量用global声明
name = "liqian"
def getName():
    global  name
    name = "张三"


if __name__ == '__main__':
    # printInfo("张三")
    # getUserInput()
    # shang, yushu = divid(10, 3)
    # print("商:%d,余数:%d" % (shang, yushu))
    # printMyNumStr(3)
    print(name)
    getName()
    print(name)





import random

nameList = ['张三', '李四', '王五']
# 遍历
for name in nameList:
    print(name, end='')

# 下标遍历
for i in range(len(nameList)):
    print(nameList[i], end='')

# 下标遍历
for i, name in enumerate(nameList):
    print(i, name)

# append 追加
nameList.append('赵六')
print(nameList)

nameList2 = ['马七', '法外']
nameList.append(nameList2)
print(nameList)

# insert 插入(下表,元素值)
a = [1, 2, 3]
a.insert(0, 5)
print(a)

# del[下标] 删除指定下表元素
videoList = ['加勒比海盗', '黑客帝国', '速度与激情', '指环王', '速度与激情']
del videoList[0]
print(videoList)

# pop 删除最后一个元素
videoList.pop()
print(videoList)

# remove[元素值] 直接删除指定内容,如果有相同内容,只删除第一个
videoList.remove('黑客帝国')
print(videoList)

# 清空列表
videoList.clear()
print(videoList)

# 修改
bookList = ['书本1', '书本2', '书本3']
bookList[1] = '修改书'
print(bookList)

# 查找 in  not in
inputStr = input('请输入你想查找的书本名称:')
if inputStr in bookList:
    print('找到了')
else:
    print('没找到')

# 查找index(查找值,开始下标,结束下标) 包含开始下标,不含结束下标
a = ['a', 'b', 'c', 'd', 'a']
print(a.index('b', 1, 4))

# 查找list中元素命中个数
print(a.count('a'))

# 反转
a = [1, 4, 2, 3]
a.reverse()
print(a)

# 排序 asc
a.sort()
print(a)

# 排序 desc
a.sort(reverse=True)
print(a)

# 8个老师随机分配3个房间
homes = [[], [], []]
names = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', ]

for name in names:
    index = random.randint(0, 2)
    homes[index].append(name)
print(homes)
for i in range(len(homes)):
    print('第%d个房间中的老师' % (i + 1))
    for j in range(len(homes[i])):
        print(homes[i][j], end='\t')
    print()

# 打印商品
products = [['iphone', 6888], ['MacPro', 14800], ['小米6', 2499], ['Nike', 399]]
cars = []
print('-----商品列表-----')
for i in range(len(products)):
    name = products[i][0]
    price = products[i][1]
    print(str(i + 1) + '\t' + name + '\t' + str(price))
for i in range(len(products)):
    productNo = input('请输入商品号:')
    if productNo != '':
        j = int(productNo) - 1
        cars.append(products[j])
print(cars)

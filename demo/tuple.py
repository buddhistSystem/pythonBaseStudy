# 元组
tup1 = (2000, 2001, 2002)
print(tup1)

# 增加 连接
tup2 = (2000, 2001, 2002)
tup3 = ('abc',)
tup4 = tup2 + tup3
print(tup4)

# 删除del 直接删除整个元组
tup5 = (1, 2, 3)
del tup5
# 删除后 tup5不存在,打印报错
# print(tup5)

# 不可修改

tup6 = (1, 2, 3, 1, 10)
# 最大值
print(max(tup6))
# 最小值
print(min(tup6))
# 元素1出现个数
print(tup6.count(1))
# 元组大小
print(len(tup6))

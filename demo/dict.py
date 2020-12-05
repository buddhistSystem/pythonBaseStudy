# 字典
people = {"name": "张三", "age": 26}

# 获取字典中的字段
print(people["name"])
print(people.get("name"))

# 若元组中不存在key,使用以下方式报错
# print(people["gender"])

# 访问key,若key不存在,赋予value默认值
print(people.get("gender", "男"))

# 判断key是否存在
print(people.__contains__("name"))

# 新增
people["gender"] = "男"

# 删除
del people["age"]
print(people)

# 修改
people["gender"] = "女"
print(people)

shengfen = {1: "北京", 2: "山西", 3: "山东", 4: "河南"}
# 遍历key
print(shengfen.keys())
# 遍历value
print(shengfen.values())
# 遍历entry 每一个entry是一个元组
print(shengfen.items())

# 遍历键值对
for key, value in shengfen.items():
    print("key=%d,value=%s" % (key, value))

# -*- codeing = utf-8 -*-
from bs4 import BeautifulSoup

file = open("./baidu.html", "rb")
html = file.read().decode("utf-8")
# 获取html解析器
bs = BeautifulSoup(html, "html.parser")

# 1.Tag 获取标签及内容,但是只能获取他找到的第一个内容
# print(bs.title)
# print(bs.a)
# print(bs.head)
# print(bs.div)

# 2.NavigableString 获取标签里面的内容
# print(bs.title.string)
# print(bs.a.string)

# 3.BeautifulSoup 文档对象
# print(bs)
# print(bs.name)

# 4.Comment 是一个特殊的NavigableString,输出的内容中不包含注释符号
# print(bs.a.string)
# print(type(bs.a.string))


# ---------------------分割线-----------------------
# 文档的遍历
# contents: 返回所有的Tag子节点
# print(bs.head.contents)
# print(bs.head.contents[1])


# 文档的搜索
# 字符串过滤:查找所有<a>
a_list = bs.find_all("a")
# print(a_list)

# 正则匹配搜索
import re

a_list_1 = bs.find_all(re.compile("<a"))


# print(a_list_1)

# 方法搜索,根据函数要求来搜索
def name_is_exists(tag):
    return tag.has_attr("name")


list = bs.find_all(name_is_exists)
# print(list)


# kwargs 参数搜索
list1 = bs.find_all(id="head")
# print(list1)
list2 = bs.find_all(class_="mnav")
# print(list2)
list3 = bs.find_all(href="http://news.baidu.com")
# print(list3)

# text参数
list4 = bs.find_all(text=["hao123", "地图"])
# print(list4)
# 通过正则作为条件,包含数字
list5 = bs.find_all(text=re.compile("\d"))
# print(list5)

# limit 参数
list6 = bs.find_all("a", limit=2)
# print(list6)

# css选择器
# 标签选择器
# print(bs.select("title"))
# 类选择器
# print(bs.select(".bri"))
# id选择器
# print(bs.select("#u1"))
# 属性选择器
# print(bs.select("a[class='bri']"))

print(bs.select("head > title"))

# -*- codeing = utf-8 -*-
# 正则

# .    表示任何单个字符
# []   表示字符集,[abc]b表示a,b,c,[a-z]表示a到z单个字符
# [^]  非字符集,[^abc]表示非a,非b,非c单个字符
# *    前一个字符0或无限次扩展
# +    前一个字符1或无限次扩展
# ?    前一个字符0或1次扩展
# |    左右表达式任意一个 abc|def,表示abc或者是def
# {m}  前一个字符出现m次,abc{2}表示abcc
# {m,n}前一个字符出现m至n次(含n)abc{1,2}表示abc或者abcc
# ^    匹配字符串开头,^ab,以ab开头
# $    匹配字符串结尾,ab$,以ab字符串结尾
# ()   分组标识,内部只能用 | 操作符 (abc),(abc|def)表示abc或者def
# \d   数字[0-9]
# \w   单词,[a-zA-Z0-9_]

import re

# 创建模式对象
s = "abccxxabcc"
pattern = re.compile("abc{2}")
# search()只匹配到第一个符合的段落
result = pattern.search(s)
print(result)
# findAll()匹配所有符合的段落
result1 = re.findall("abc{2}", s)
print(result1)
# sub("被替换的字符串","将要替换的字符串","操作字符串")
print(re.sub("a", "A", "abcd"))
# 建议在正则表达式中,被比较的字符串前面加上r,这样不用担心转义字符的问题
s1 = r"\aabc-'\'"
print(s1)


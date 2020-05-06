"""
正则表达式的使用过程
1、编译（re.compile）
2、匹配（match、find、search）
3、匹配结果（匹配到的字符串、文本以及索引）
"""
import re

p = re.compile(r"abc")
print(type(p))

m = p.match("abcedf")
print(type(m))
print(m.group())
print(m)

m = p.match("acbedf")
print(type(m))
# print(m.group())



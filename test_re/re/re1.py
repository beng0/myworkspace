"""
元字符

.    除换行符的任意字符
\    转义字符
[…]  字符集合
\d   数字：[0-9]
\D   非数字：[^0-9]
\s   空白字符[<空格>\t\r\n\f\n]
\S   非空白字符[^\s]
\w   单词字符[A-Za-z0-9_]
\W   非单词字符[^\w]
"""
import re

# p = re.compile(".")

# m = p.match("abc")
# print(m.group())

# m = p.match("\n")
# print(m.group())

# p = re.compile('\.')
# m = p.match("abc.ef")
# print(m.group())

# m = p.match(".")
# print(m.group())
#
# m = p.findall("abc.ef.gh")
# print(type(m))
# print(m)

p = re.compile("[abc]")
m = p.findall("abcdef")
print(m)

m = p.match("abcdef")
print(m.group())



"""
逻辑、分组

| 左右表达式任意匹配一个，先匹配左边一旦成功则跳过匹配右边，如果|没有包含在（）中，匹配整个正则表达式
(…) 分组匹配，从左到右，每遇到一个（编号+1分组后面可加数量词）
(?P<name>…) 除了分组序号外，制定一个name的别名
(?P=name) 引用别名为<name>的分组匹配到的串
\<number> 引用编号为<number>的分组匹配到的字符串
"""
import re

p = re.compile("(a)(b)(c)")
m = p.match("abcdef")
print(m.groups())

p = re.compile("(a)b(c)")
m = p.match("abcdef")
print(m.groups())

# m = p.match("adcdef")
# print(m.groups())

p = re.compile("(?P<name>a)b(c)")
m = p.match("abcdef")
print(m.groups())
print(m.groupdict())

p = re.compile("(?P<name>a)b(c)(?P=name)")
print(p.findall("abcd"))
print(p.findall("abca"))

p = re.compile(r"(?P<name>a)b(c)(?P=name)\1")
print(p.findall("abcaa"))
print(p.findall("abcac"))

p = re.compile(r"(?P<name>a)b(c)(?P=name)\2")
print(p.findall("abcac"))

m = p.match("abcac")
print(m.group())
print(m.groups())
print(m.groupdict())
print(m.group(1))
print(m.group(2))
print(m.group(3))
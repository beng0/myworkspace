"""
边界

^ 匹配字符串开头，多行匹配每一行开头
$ 匹配字符串末尾，多行匹配每一行末尾
\A 仅匹配字符串开头
\Z 仅匹配字符串末尾
\b 匹配\w 和 \W 之间
"""
import re

# p = re.compile("^[abc]*")
# print(p.findall("abcdef"))
# print(p.findall("bcdef"))
# print(p.findall("def"))
# print(p.findall("defabc"))

# p = re.compile("[abc]*")
# print(p.findall("defabc"))

# p = re.compile("[^abc]*")
# print(p.findall("abcdef"))

p = re.compile("^[abc]*e$")
print(p.findall("abcd"))
print(p.findall("abcde"))
print(p.findall("abce"))
print(p.findall("bce"))
print(p.findall("ce"))


import re

p = re.compile("a")

# print(type(p))

# m = re.match("a","adb")
# print(m)
# print(type(m))
# print(m.group())

# n = p.match('aadb')
# print(n)
# print(type(n))
# print(n.group())

l = p.findall("abca")
print(l)
print(type(l))
# print(l.group())

# 总结：re.compile(),re.match().group(),re.findall()方法
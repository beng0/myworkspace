"""
re.compile(strPattern[, flag])
pattern
match
search
split
findall
finditer
sub
"""
import re

p = re.compile(r"abc", re.I)
# m = p.match("cbabcaa")
# print(m.group())
m = p.search("cbabcaa")
print(m.group())

p = re.compile(r"-")
print(p.split("a-bc-ddd-aaa-sss"))

p = re.compile("a")
m = p.finditer("abcdddaaass")
print(type(m))

p = re.compile(r"(\w+) (\w+)")
s = "hey you , good boy"
print(p.sub(r"\2 \1", s))
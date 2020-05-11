"""
特殊构造

(?:…) (…)不分组版本，用于使用 | 或者后接数量词
(?#...) #号后的内容将作为注释
(?=…) 之后的字符串内容需要匹配正则表达式才能成功匹配
(?!...) 之后的字符串不匹配表达式才能成功
(?<=…) 之前的字符串需要匹配表达式才能成功
(?<!...) 之前的字符串需要不匹配表达式才能成功
(?(id/name) yes |no) 如果编号为id/名字为name的组匹配到字符串，则需要匹配yes，否则匹配no，no可以省略
"""
import re

# p = re.compile(r"(?:abc){2}")
# print(p.findall("abc"))
# print(p.findall("abcabc"))
# print(p.findall("abcabcabc"))
# print(p.findall("abcabcabcabc"))
# m = p.match("abcabcabcabc")
# print(m.groups())

# p = re.compile(r"a(?=\d)")
# print(p.findall("a1a2a3"))
# p = re.compile(r"\w(?=\d)")
# print(p.findall("word1 wor2 wo3"))
# p = re.compile(r"\w+(?=\d)")
# print(p.findall("word1 wor2 wo3"))
# p = re.compile(r"a(?!\d)")
# print(p.findall("word1 wor2 oa3"))
# print(p.findall("word1 wor2 ao3"))

# p = re.compile(r"(?<=\d)a")
# print(p.findall("word1 wora2 awo3a"))
# p = re.compile(r"(?<!\d)a")
# print(p.findall("word1 wora2 awo3a"))

p = re.compile(r"(\d)?abc(?(1)\d|abc)")
print(p.findall("1abc4"))
m = p.match("1abc4")
print(m.group())
# m = p.match("1abcabc")
# # print(m.group())
m = p.match("abcabc")
print(m.group())
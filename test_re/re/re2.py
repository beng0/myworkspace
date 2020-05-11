"""
数量词

* 匹配前一个字符0或者多次
+ 匹配前一个字符1或者多次
? 匹配前一个字符0次或者1次
{m} 匹配前一个字符m次
{m,n} 匹配前一个字符m次n次
数量词? 变成非贪婪模式
"""
import re

# p = re.compile("[abc]*")
# print(p.findall("abcdef"))
#
# p = re.compile("[abc]+")
# print(p.findall("abcdef"))

# p = re.compile("[abc]*?")
# print(p.findall("abcdef"))

# p = re.compile("[abc]+?")
# print(p.findall("abcdef"))

p = re.compile("[abc]{2}")
print(p.findall("abcdef"))
print(p.findall("abcabc"))

p = re.compile("[abc]{2,3}")
print(p.findall("abcabc"))

p = re.compile("[abc]{2,3}?")
print(p.findall("abcabc"))


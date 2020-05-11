"""
iLmsux
(?iLmsux) iLmsux的每个字符代表一个匹配模式，只能用在正则表达式的开头，可选多个

I re.I 忽略大小写
L re.L 使用预定字符类 \w \W \b \B \s \S 取决当前区域设定
m re.M 多行模式改变^ 和 $ 的行为
s re.S . 任意匹配模式
u re.U 使用预定字符类 \w \W \b \B \s \S \d \D 取决unicode定义的字符属性
x re.X 详细模式，可以多行，忽略空白字符，并且可以加入注释
"""
import re
p = re.compile(r"(?i)abc")
print(p.findall("abc"))
print(p.findall("Abc"))
print(p.findall("ABc"))

p = re.compile(r"abc", re.I)
print(p.findall("abc"))
print(p.findall("Abc"))
print(p.findall("ABc"))


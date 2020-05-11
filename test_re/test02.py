# 元字符
import re
a = re.compile("a")
print(re.match("a","adbaa").group())

# .

print(re.match(".","kkf%").group())

# \
print(re.match("\(","(kkk)").group())

# \d
print(re.match("\d","4er5").group())
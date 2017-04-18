import re

# .* 匹配 0 到多个字符
# .+ 匹配 1 到多个字符
# 

li = re.findall(" liao ", "liaomixi is good liaomixixxxx liao ")
print(li, type(li))

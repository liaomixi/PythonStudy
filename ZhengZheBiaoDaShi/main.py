import re

# .* 匹配 0 到多个字符
# .+ 匹配 1 到多个字符
# .? 匹配 0 或 1 个字符
# .{1,5} 匹配 1 到 5 个字符
# .{4} 匹配 4 个字符
# . 匹配任意 1 个字符

li = re.findall(" liao ", "liaomixi is good liaomixixxxx liao ")
print(li, type(li))

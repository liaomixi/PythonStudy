# 集合的并集
a = set([1, 2, 3])
b = set([3, 4])
d = a.union(b) # d为a、b两个集合的并集，也可写为 a | b，重复元素只保留1个
print(d)

# 集合的交集
a = set([1, 2, 3])
b = set([3, 4])
d = a.intersection(b) # d为a、b两个集合的交集，即a和b之间相同元素组成的集合。也可写为 a & b
print(d)

# 集合的差集
a = set([1, 2, 3])
b = set([3, 4])
d = a.difference(b)   # d为a中去掉与b重复的元素后，a中还剩余的元素。---- b.difference(a) 就是b中去掉与a重复的元素后，b中还剩余的元素。
print(d)

# 集合的对称差集
a = set([1, 2, 3, 4])
b = set([3, 4])
d = a.symmetric_difference(b) # d为a和b合在一起后去掉重复元素后剩余的部分
print(d)

#test

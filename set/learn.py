#set 适合用于查重，集合操作，判断元素是否存在
#create set
nums={1,2,3}
#对于可迭代对象创建
letters=set("hello")#字符串会拆解成字符
print(letters)#顺序不能保证但是会去重
#设置空集合
empty_set=set()
#{}这是空字典，空集合必须用set()
scores={87,99,104,118,75,104}
print(scores)
"""
set的特点：
1，无序，不可下标索引
2.元素不重复,但是不同类型可以混编
3.元素必须是可哈希的（不可变对象，元组是可哈希的
4.访问很快O(1)
"""

#add
fruits={"banana","apple"}
fruits.add("banana")
fruits.add("orange")
print(fruits)

#update 添加多个元素
fruits.update(("orange", "pear"))#list add列表元组和集合都可以满足批量化
fruits.update("wiki")
print(fruits)

#delete
nums.remove(2)#没有会报keyerror，discard不会
nums.discard(99)
print(nums)

#pop随机弹出元素,claer清空
s={'a','b','c'}
item=s.pop()
print(s)
print(item)
print('b' in s)
print(len(s))#返回集合长度，即元素个数
languages = {"Python", "Java", "C++"}
for l in languages:#无序的
    print(l)
for l in sorted(languages):#实际上sorted将languages转化为list输出，但是可以实现排序后的固定顺序
    print(l)
print(type(sorted(languages)))

#集合操作
a={1,2,3,4}
b={3,4,5,6}
#并集
print(a|b)
print(a.union(b))
#交集
print(a&b)
print(a.intersection(b))
#差集
print(a-b)
print(a.difference(b))
#对称差集
print(a^b)
print(a.symmetric_difference(b))

#判断
a = {1, 2}
b = {1, 2, 3, 4}
c = {5, 6}
print(a<=b)
print(a.issubset(b))
print(b>=a)
print(b.issuperset(a))
#不含共同元素
print(a.isdisjoint(c))

#集合推导式，适合去重
l1={x**2 for x in range(1,11) if x%2==0}
print(l1)#1-256小整数自身是哈希值，不需要哈希盐，因此每次结果几乎相同
names={'bob','alice','kat','cow','butty'}
name_lens={len(name) for name in names}
print(name_lens)

#字典的键和几何元素必须是可哈希的，frozenset可以将元素均为可哈希的list或者set转换为不可变的SET
fs=frozenset([1,2,3])
group1 = frozenset({"Alice", "Bob"})
group2 = frozenset({"Cathy", "David"})
groups={group1,group2}#frozenset转化后可以作为set元素，但会标注frozenset
print(groups)
#列表去重
numbers = [1, 2, 2, 3, 1, 4]
unique_numbers = list(set(numbers))
print(unique_numbers)#丢失顺序,小数排列时另说
#不丢失
unique_numbers2=list(dict.fromkeys(numbers))#传入可迭代对象，转化为keys,value默认NOne,但是传入可变对象
# ，所有键地址相同，共同修改，如果想要修改：d={key:[]for key in[list]}
print(unique_numbers2)

#找两个列表共同元素
class_a = ["Alice", "Bob", "Cathy"]
class_b = ["Bob", "David", "Cathy"]
common=set(class_a)&set(class_b)
print(common)

#检查列表是否存在重复
items=[1,2,3,2]
r=len(items)!=len(set(items))
print(r)




mix=["banana",2.3,3,True]
print(mix[::-1])
lst=[1,2,3,4]
print(lst[2:0:-1])
#增删改操作
lst.append(5)
lst.insert(5,6)
lst.extend([7,8])
del lst[7]
lst.pop(-1)
lst.remove(6)
#lst.clear()
print(len(lst))
print(lst.index(3))
print(2 in lst)
#增删改操作
print(lst)
#sort
nums=[1,2,2,9,6,5]
new_nums=sorted(nums)
print(new_nums)
nums.sort(reverse=True)
print(nums)
nums.reverse()
print(nums)
#列表推导式
nums=[x**2 for x in range(10) if x%2==0]
print(nums)
a=nums.copy()
b=a[:]
c=list(a)
print(a)
print(b)
print(c)

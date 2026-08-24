#去重与成员判断
raw = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
new_list=[]
for i in raw:
    if not i in new_list:
        new_list.append(i)
print(new_list)
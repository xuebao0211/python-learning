scores = {"Math": 95, "English": 88, "CS": 100}
for key in scores:
    print(key)
for value in scores.values():
    print(value)
for key,value in scores.items():
    print(f"lesson {key} score is {value}")
#字典推导式
nums=[1,2,3,4]
dict1={x:x**2 for x in nums}
dict2={x:x**2 for x in range(10) if x%2==0}
print(dict1,dict2)
d={'a':1,'b':2}
data_view=d.keys()
data_view1=d.items()
print(data_view,data_view1)
d['c']=3
print(data_view,data_view1)
snap=list(d.items())
snap1=list(d.values())
print(snap,snap1)
score_dict = {"Alice": 85, "Bob": 92, "Charlie": 78}
dict_sort=dict(sorted(score_dict.items(),key=lambda x:x[0],reverse=True))
dict_sort1=dict(sorted(score_dict.items(),key=lambda x:x[1]))
print(dict_sort,dict_sort1)
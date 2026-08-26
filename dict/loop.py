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
snap1=list(d.values())#返回的是视图
print(snap,snap1)
score_dict = {"Alice": 85, "Bob": 92, "Charlie": 78}
dict_sort=dict(sorted(score_dict.items(),key=lambda x:x[0],reverse=True))
dict_sort1=dict(sorted(score_dict.items(),key=lambda x:x[1]))
print(dict_sort,dict_sort1)
for key in list(d.keys()):
    if key=='b':
        del d[key]
print(d)
#users = {"user1": {"age": 20, "city": "NY"}, "user2": {"age": 25}}
#让你安全地获取 user2 的 city，如果不存在就返回 "Unknown"，该怎么写？
users = {"user1": {"age": 20, "city": "NY"}, "user2": {"age": 25}}
city=users.get("user2",{}).get("city","Unknown")
print(city)
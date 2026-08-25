#查
info={"name":"Bob","score":90}
print(info.get("age"))
print(info.get("age",0))
print(info.get("name"))
print(info["score"])
#add and change
data={"city":"beijing"}
data["city"]="shanghai"
data["country"]="china"
print(data)
#批量更新
extra={"city":"suzhou","zipcode":100000}
data.update(extra)
print(data)
#删
stock= {"apple": 5, "banana": 3, "cherry": 10}
item1=stock.pop("banana",None)
item2=stock.pop("year",None)
print(item1,item2)
del stock["apple"]
print(stock)
disc=stock.popitem()
print(disc)
print(stock)
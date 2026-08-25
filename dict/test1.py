"""你有一家小卖部的库存字典 inventory = {"可乐": 10, "雪碧": 5, "矿泉水": 20}。
请编写程序，依次执行以下操作，并在每次操作后打印当前库存：
上架新品：新增一种商品 "红牛"，库存为 8 瓶。
卖出商品：用户购买 3 瓶 "雪碧"，请减少对应库存。
补货：给 "矿泉水" 补货 10 瓶。
安全查询：用户想查 "橙汁" 的库存，请使用 .get() 方法查询，如果不存在，则打印 "橙汁 暂时缺货"。
下架滞销品：如果 "可乐" 的库存小于 5，则将它从字典中删除；否则，不做任何操作。
考察点：增、改、安全取值 (get)、条件删除 (del 或 pop)。"""
inventory = {"cola": 10, "xue": 5, "water": 20}
inventory["red"]=8
print(inventory)
inventory["xue"]=2
print(inventory)
inventory["water"]=30
print(inventory)
search=inventory.get("juice","sold out")#get是取值操作
print(search)
if inventory.get("cola")<5:
    del inventory["cola"]
print(inventory)
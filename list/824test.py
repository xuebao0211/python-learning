n=int(input("please input:"))
total=0
for i in range(n):
    if i%3==0 and i%5!=0:
         total+=i
print(f"the total is:{total}")
x=100
print(x,type(x))
x='100'
print(x,type(x))#type()表示类型
a=3
b=5
a,b=b,a
print(a,b)

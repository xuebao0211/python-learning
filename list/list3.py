#嵌套列表逻辑处理
intervals = [[1, 3], [2, 9], [8, 10], [15, 18]]
intervals.sort(key=lambda x:x[0])
merged=[]
for interval in intervals:
    if not merged or merged[-1][1]<interval[0]:#空列表或者两者不连贯时直接加入，需要通过sort保证intervals是升序的
        merged.append(interval)
    else:
        merged[-1][1]=interval[1]
print(merged)

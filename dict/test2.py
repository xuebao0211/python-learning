"""给定一个包含多个学生成绩记录的列表（每门课一条记录），数据如下：

records = [
    {"name": "Alice", "subject": "Math", "score": 88},
    {"name": "Bob", "subject": "Math", "score": 92},
    {"name": "Alice", "subject": "English", "score": 95},
    {"name": "Charlie", "subject": "Math", "score": 78},
    {"name": "Bob", "subject": "English", "score": 85},
    {"name": "Charlie", "subject": "English", "score": 90},
]
需求：
请编写程序，将上述数据转换成一个按科目分组的嵌套字典，结构如下：
{
    "Math": {
        "avg_score": 86.0,          # 该科目平均分
        "students": ["Bob", "Alice", "Charlie"], # 按分数从高到低排序的学生名字
        "top_student": "Bob"         # 该科目最高分学生
    },
    "English": {
        "avg_score": 90.0,
        "students": ["Alice", "Charlie", "Bob"],
        "top_student": "Alice"
    }
}"""
records = [
    {"name": "Alice", "subject": "Math", "score": 88},
    {"name": "Bob", "subject": "Math", "score": 92},
    {"name": "Alice", "subject": "English", "score": 95},
    {"name": "Charlie", "subject": "Math", "score": 78},
    {"name": "Bob", "subject": "English", "score": 85},
    {"name": "Charlie", "subject": "English", "score": 90},
]
temp={}#先构造一个非排序的分学科字典
for item in records:
    subject=item["subject"]
    name=item["name"]
    score=item["score"]
    if subject not in temp:
        temp[subject]={"scores":[],"names":[]}#字典的增加操作，等号后面是value
    temp[subject]['scores'].append(score)
    temp[subject]['names'].append(name)
result={}#我要的结果
for subject,data in temp.items():#同时取出key and value
    scores=data["scores"]
    names=data['names']
    sorted_pairs=sorted(zip(scores,names),key=lambda x:x[0],reverse=True)#元组列表
    avg=sum(scores)/len(scores)
    sort_name=[name for score,name in sorted_pairs]
    result[subject]={
        "avg_score":round(avg,1),#round函数保留精度
        "students":sort_name,
        "top_student":sort_name[0]
    }
print(result)

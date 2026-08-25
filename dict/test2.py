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
}
考察点：

分组逻辑：遍历列表，将数据按 subject 归类到字典中。
列表与字典嵌套操作：动态维护每个科目的分数列表和学生列表。
内置函数与排序：使用 sum() / len() 计算平均分，使用 sorted 配合 lambda 按分数排序学生名字。
字典取值：熟练使用 .get() 或 setdefault 避免 KeyError。"""
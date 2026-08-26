scores = [88, 92, 88, 76, 100, 92, 85]
rank=sorted(set(scores),reverse=True)
print(rank)
python_students = {"小明", "小红", "小李", "小张"}
java_students = {"小红", "小张", "小王", "小陈"}
print(python_students&java_students)
print(python_students-java_students)
print(python_students|java_students)
usernames = ["alice", "bob", "cathy", "alice", "david"]
if len(usernames)!=len(set(usernames)):
    print("exist")
else:
    print("None")

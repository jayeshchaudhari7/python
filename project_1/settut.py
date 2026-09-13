n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
print(student_marks)
for name, scores in student_marks.items():
    total = sum(scores)     
    max_total = len(scores) * 100   
    percentage = (total / max_total) * 100
    print(f"{name}: {percentage:.2f}%")

n=int(input("enter the no of students records to store"))
student_records={}
for _ in range(n):
    name,*line=input().split()

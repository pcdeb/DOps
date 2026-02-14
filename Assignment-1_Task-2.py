#Student Grades (Assignment-1_Task-2.py)

Student_Grades = {"A":20, "B":30, "C":40}

print(type(Student_Grades))
print(Student_Grades)

#adding a new key
Student_Grades.update({"D":90})

#updating an existing key
Student_Grades.update({"C":90})

print(Student_Grades)

#getting input from user to add/modify key
stu_name=input("Enter name: ")
stu_marks=float(input("Enter marks: "))

Student_Grades.update({stu_name:stu_marks})

print(Student_Grades)

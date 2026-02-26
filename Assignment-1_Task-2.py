#Student Grades (Assignment-1_Task-2)

Student_Marks = {"Alice":20, "Brittany":30, "Chloe":40}

print(type(Student_Marks))
print(Student_Marks)

#adding a new key
Student_Marks.update({"Demi":90})

#updating an existing key
Student_Marks.update({"Chloe":90})

print(Student_Marks)

#getting input from user to add/modify key
stu_name=input("Enter name: ")
stu_marks=float(input("Enter marks: "))

Student_Marks.update({stu_name:stu_marks})

print(Student_Marks)

#function to check grades of the students
def grades(dict):
    
        for i in dict:
            if dict[i]>=90:
                print(f"{i}'s grade is A")
            elif dict[i]>=80:
                print(f"{i}'s grade is B")                
            elif dict[i]>=70:
                print(f"{i}'s grade is C")                
            elif dict[i]>=60:
                print(f"{i}'s grade is D")     
            else:
                print(f"{i}'s grade is F")

        return 0
    

#calling the function
grades(Student_Marks)

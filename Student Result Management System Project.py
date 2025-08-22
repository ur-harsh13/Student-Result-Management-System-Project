students_data = []
for i in range(1 , 11):
        while True:
            name = input(f"Enter name of student {i}: ")
            if all(part.isalpha() for part in name.split()):
                 break
            else:
                print("Invalid! Name should in A to Z Characters")
        Subjects = ["Maths", "Science", "English", "Hindi", "Computer"]
        subject_marks = {}
        for subject in Subjects: 
            while True:
                marks = int(input(f"Enter marks for {subject} (0-100):"))
                if 0 <= marks <= 100:
                    subject_marks[subject] = marks
                    break
                else:
                    print("Invalid! Marks should be between 0 to 100.")
                 
    
        total_marks = sum(subject_marks.values())
        Percentage = (total_marks / (len(Subjects) * 100)) * 100
    
        if Percentage >= 90:
            Grade = "A+"
        elif Percentage >= 80:
            Grade = "A"
        elif Percentage >= 70:
            Grade = "B+"
        elif Percentage >= 60:
            Grade = "B"
        elif Percentage >= 50:
            Grade = "C"
        elif Percentage >= 40:
            Grade = "D"

    
        stud_data = {
            "name" : name , 
            "marks": subject_marks , 
            "total_marks" : total_marks , 
            "Percentage" : round(Percentage, 3),
            "Grade": Grade
        }
    
        students_data.append(stud_data)
    
print ("\n...Students Result...")
for student in students_data:
    print(f"Name: {student['name']}")
    print(f"marks: {student['marks']}")
    print(f"Total: {student['total_marks']}")
    print(f"Percentage: {student['Percentage']}%")
    print(f"Grade: {student['Grade']}")
    print(".." * 20)
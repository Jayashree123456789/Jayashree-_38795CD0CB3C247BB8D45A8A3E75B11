class students:
def __init__(self,name,roll_number, cgpa):
   self.name=name 
   self.roll_number=roll_number 
   self.cgpa=cgpa
def sort_student(students_list): 
  sorted_students=sorted(student_list, key=lambda students:students,cgpa,reverse=True)
return sorted_students
students=[student("hari","A123","7.8"),student("srikanth","A124","8.9"),student("saumya","A125","9.1"),student("mahidhar","A126","9.9")]
sorted_students=sort_students(students)
for students in sorted_students:
  print("name:{},roll_number:{},cpga:{}".format (student.name,student,roll_number,student,cgpa)
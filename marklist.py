f_name= input("Enter your first name: ")
s_name= input("Enter your second name: ")
roll_no= input("Enter your roll no: ")
standard= input("Enter your class: ")
sub1= float(input("Enter mark for english: "))
sub2= float(input("Enter mark for mathematics: "))
sub3= float(input("Enter mark for science: "))
sub4= float(input("Enter mark for malayalam: "))
sub5= float(input("Enter mark for IT: "))
sub6= float(input("Enter mark for social science: "))
Total= sub1 + sub2 + sub3 + sub4 + sub5 + sub6
average= Total / 6
if average >= 90:
  grade = "A" 
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
else:
    grade = "F"
    
    
if ((sub1>=40) and (sub2>=40) and (sub3>=40) and (sub4>=40) and (sub5>=40) and (sub6>=40)):
    is_pass = "Pass"
else:
    is_pass = "Fail"



print("\n" + "*" * 30)
print("      STUDENT REPORT")
print("*" * 30)
print(f"First Name:     {f_name}")
print(f"Second Name:    {s_name}")    
print(f"Roll No:        {roll_no}")
print(f"Class:          {standard}")
print("-" * 30)
print(f"English:        {sub1}")
print(f"Mathematics:    {sub2}")
print(f"Science:        {sub3}")
print(f"Malayalam:      {sub4}")
print(f"IT:             {sub5}")
print(f"Social Science: {sub6}")
print("-" * 30)
print(f"Total:          {Total}")
print(f"Average:        {average}")
print(f"Grade:          {grade}")
print(f"Result:  {is_pass}")
print("*" * 30)
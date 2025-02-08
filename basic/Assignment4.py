#Grades: 

# A = 90-100,B=80-89,C=70-79,D=60-69,F=less than 60

# Create an integer variable , grade, holding a value between 0 and 100

# Add if, elif and else statements to print the letter grade of the grade value.


grade = int(input("Enter your grade: "))

if grade >= 90 :
    print("A")
elif grade >= 80 and grade <= 89:
    print("B")
elif grade >= 70 and grade <= 79:
    print("C")
elif grade >= 60 and grade <= 69:
    print("D")
else:
    print("F")
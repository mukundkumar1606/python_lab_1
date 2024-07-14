# MarkeSheet
# Created by Mukund vaghasiya  on 11/07/24.

name = input("Enter the student's name: ")

math = float(input("Enter marks for Math: "))
science = float(input("Enter marks for Science: "))
english = float(input("Enter marks for English: "))
history = float(input("Enter marks for History: "))
geography = float(input("Enter marks for Geography: "))

total = math + science + english + history + geography

average = total / 5

if average >= 90:
    grade = 'A'
elif average >= 80:
    grade = 'B'
elif average >= 70:
    grade = 'C'
elif average >= 60:
    grade = 'D'
else:
    grade = 'F'

print("\nMarksheet for {}".format(name))
print("-" * 30)
print("Math: {}".format(math))
print("Science: {}".format(science))
print("English: {}".format(english))
print("History: {}".format(history))
print("Geography: {}".format(geography))
print("-" * 30)
print("Total Marks: {}".format(total))
print("Average Marks: {}".format(average))
print("-" * 30)
print("Grade: {}".format(grade))
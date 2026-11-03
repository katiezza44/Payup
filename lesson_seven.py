# Comparison Operators
age = 22
if_adult = age >= 18
print(if_adult)

hour = 9
if_morning = hour <= 12
print(if_morning)
# Comparing alphabetically
print("banana" > "mango")
# If-else statement
number = 11
if number > 20:
    print("number is greater")
else:
    print("number is less")

age = 15
if age < 18:
    print("not an adult")
else:
    print("is an adult")

# Challenge: Quiz Pass or fail
# Youre building the results screen for an online course quiz. A student
# needs at least 60 points to pass.
# 1. Ask the student for their score and convert it to an int.
# 2. It thetr score is 60 or higher, print that they passed.
# 3. Otherwise, print that they didn't pass this time.

student_score = int(input("what is your score? "))

if student_score >= 60:
    print("you have passed!")
else:
    print("you have not passed.")

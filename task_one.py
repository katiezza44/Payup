# Tasks

# Challenge 2: Build a student result display
# 1. Create variables for: student name, course name, assignment score, test score, exam score, and total score.
# 2. Use made-up scores for now.
# 3. Calculate the total score using the three scores.
# 4. Display the result line by line using print() and f-strings.
# 5. Add a blank line between the student's information and their scores.
# 6. Run the program and check the output.

student_name = "mitya"
course_name = "chemistry"
assignment_score = 89
test_score = 94
exam_score = 98
total_score = assignment_score + test_score + exam_score

print(f"mitya is doing a {course_name} course. For his assignment score he achieved {assignment_score}, for his test score he achieved {test_score} and he achieved a {exam_score} for his exam score. In total, Mitya achieved a grand score of {total_score}.")

# Challenge 3: Create a simple shopping receipt
# 1. Create variables for: product name, product price, quantity, discount, and delivery fee.
# 2. Calculate the subtotal.
# 3. Calculate the final total after applying the discount and delivery fee.
# 4. Display the receipt using print() and f-strings.
# 5. Make the output look like an actual receipt.
# 6. Run it with at least two different sets of values.
 

# Challenge 4: Build a salary calculator
# 1. Create variables for: employee name, basic salary, transport allowance, housing allowance, tax, and pension.
# 2. Calculate the total allowances.
# 3. Calculate the gross salary.
# 4. Calculate the total deductions.
# 5. Calculate the net salary.
# 6. Display the salary breakdown line by line using print() and f-strings.
# 7. Make the output look like a simple payslip.

# Challenge 5: Build a ticket booking calculator
# 1. Create variables for: event name, ticket price, number of tickets, service charge, and discount.
# 2. Calculate the ticket subtotal.

# 3. Calculate the final amount after the discount and service charge.

# 4. Calculate the amount each person pays if the tickets are shared among a group.

# 5. Display everything using print() and f-strings.
# 6. Make sure the final output is easy to read.


event_name = "vodyanitsa's opera show"
ticket_price = 20
service_charge = 9
number_of_tickets = 4
discount = 10/100
group_size = 4

subtotal = ticket_price * number_of_tickets

discount_amount = discount * subtotal


final_amount = (subtotal) + service_charge + discount_amount

total_amount = (subtotal + service_charge) - discount_amount

amount_per_person = total_amount / group_size

print(final_amount)
print(amount_per_person)

print(f"Each person will pay a total fee of ${amount_per_person}")






# cost = float("50")
# service_charge = int("30")

# print(cost + service_charge)
# print(type(cost))
# print(cost)
# budget = float(input("what is your budget for the project? "))
# print(budget)
# print(type(budget))
# print(budget + 100)


# Challenge: Build a simple paycheck calculator
# 1, Instead of hard coded values, prompt the user for their hourly rate and hours_worked
# 2. Convert hourly_rate to a float and hours_worked to an integer.
# 3. Type check both variables.
# Multiply them together and print the total pay



# hourly_rate = input("What is your hourly rate? ")

# hours_worked = input("How many hours do you work for? ")

# print(type(hourly_rate))
# print(type(hours_worked))

# total_pay = int(hours_worked) * int(hourly_rate)

# print(total_pay)

# Now, we apply this type checking and conversion knowledge in lesson.py

event_name = input("What event are you attending? ")

drinks = int(input("How much did you spend on drinks? "))

pizza = int(input("How much did you spend on Pizza? "))

food_cost = drinks + pizza


service_charges = int(input("What was the percentage charge? For example 20 or 20% ").strip("%"))

group_size = int(input("How big is your group?"))


service_charges_total = (service_charges / 100) * food_cost 


grand_total = food_cost + service_charges_total

each_person_must_payup = grand_total / group_size

print(grand_total) 

print("Welcome to PayUp")
print()
print(f"Here's the breakdown for lunch at {event_name}")
print(f"Drinks: ${drinks}")
print(f"Pizza: ${pizza}")
print(f"Service Charges: ${service_charges_total}")
print(f"Group size: {group_size}")
print()
print(f"Grand Total: ${grand_total}")
print()
print(f"Each person must PayUp: ${each_person_must_payup:.2f}")
# We more on the expense split. We are about to get a percentage on the cost for the service charge
# Add cost and service charge to get grand_total 
# Then split the bills to the group size
# use fstring to tell the groupsize their amount. If their ammount have alot of decimals format to 2 decimal places


# Strings
# child_age = input("How old are you? ")
# father_age = input("How old are you? ")

# total_age = int(child_age) + int(father_age)

# print(total_age)
# print(type(total_age))


# age_number = int(age)

# print(age)
# print(age_number)

# print(type(age))
# print(type(age_number))
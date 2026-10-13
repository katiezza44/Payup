#  1. Learnt how to run our code using the print() function
#  2. We install python extensions
print("welocme to python")
name="kadijah tholley"
print(name)


# 3. We talked about Variables. Variable is a named container or place that stores a value.
# 4. We talked about Strings. Strings is simply text stored inside a program. There
#    are two types Strings and the Fstrings (a convenient way to put a variable in a string).

# 5. We did an example or how variable, strings, and fstrings are used using a Payup app.

age = 14
school = "Sydenham"

print(age)
# print(school)

exercise_number = 16
print(exercise_number)

pen = 12
pencil = 18
total_materials = pen + pencil
print(total_materials)


morning = "ate a sandwich"

afternoon = "had a good lunch"

evening = "did some revision"

print(f"in the morning i {morning}, in the afternoon i {afternoon}, and in the evening i {evening}")

event_name = "Domino's Pizza"
drinks = 200
pizza = 500
service_charges = 20
group_size = 4

grand_total = 720

each_person_must_payup = 130

price_per_person = grand_total / group_size

print(grand_total) 
print(f"${price_per_person}")

print("Welcome to PayUp")
print()
print(f"Here's the breakdown for lunch at {event_name}")
print(f"Drinks: ${drinks}")
print(f"Pizza: ${pizza}")
print(f"Service Charges: ${service_charges}")
print(f"Group size: {group_size}")
print()
print(f"Grand Total: ${grand_total}")
print()
print(f"Each person must PayUp: ${price_per_person}")

import random

# Challenge 1: Create a program that:
# - Randomizes the queue.
# - Selects one person for a VIP upgrade.
# - Creates a scrambled version of that person's name as their temporary VIP code.

queue = ["Ada", "Michael", "Grace", "Daniel", "Sarah"]
random.shuffle(queue)
print(queue)
random_person = random.choice(queue)
print(random_person)
person = list(random_person)

random.shuffle(person)
print(person)
scrambled_version = "".join(person)
print(scrambled_version)

# Challenge 2: You're helping a bank build a small security-training program.

# Every morning, the bank has these customers waiting:

customers = ["Ada", "Michael", "Grace", "Daniel", "Sarah"]

# The bank wants to randomly select one customer for a security check.

# However, before selecting the customer, the system should mix the queue so that nobody always gets selected based on their original position.

# After selecting the person, the bank wants a security code made from their name.

random.shuffle(customers)
print(customers)
selected_customer = random.choice(customers)
print(selected_customer)
customer = list(selected_customer)
print(customer)
random.shuffle(customer)
print(customer)
scrambled_code = "".join(customer)
print(scrambled_code)


# Challenge 3: You're making a music app for you and your friends.

# You have these songs:
songs = ["Perfect", "Flowers", "Havana", "Calm Down", "As It Was"]

# Your app should:
# - Mix the songs into a new order.
# - Pick one song to play first.
# - Create a funny scrambled version of that song's name as a secret code.
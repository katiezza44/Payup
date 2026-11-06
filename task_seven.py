# Challenge 1: Shopping Discount 🛒
# You're shopping online and the store offers free delivery for orders above $20,000.
# wallet = 25000cart_total = 18000delivery_fee = 2000

# Check:
# 1. Can you afford everything in your cart?
# 2. Do you qualify for free delivery? ($20,000 or more)
# 3. Is your wallet balance greater than $10,000?
# 4. Will you have money left after buying everything and paying delivery?

wallet = 25000
cart_total = 18000
delivery_fee = 2000
free_delivery = 20000

remaining_cash = wallet - (cart_total + delivery_fee)
print(f"cash left over: ${remaining_cash}")
total = cart_total + delivery_fee
print(f"total: ${total}")

print("Can you afford everything in your cart?")

if remaining_cash < wallet:
    print("Yes")
else:
    print("No")



print("Are you elegible for free delivery?")

if total >= free_delivery:
    print("Yes")
else:
    print("No")



print("Is your wallet balance greater than $10,000?")

if remaining_cash > 10000:
    print("Yes")
else:
    print("No")



print("Do you have money left after buying everything and paying delivery?")

if remaining_cash > 0:
    print("Yes")
else:
    print("No")


# Challenge 2: School Examination 📚
# A student has just received her examination results.
# math_score = 75english_score = 45science_score = 82


# The school considers 50 the passing mark.

# Check:
# 1. Did she pass Mathematics?
# 2. Did she pass English?
# 3. Did she score above 80 in Science?
# 4. Did she get exactly 50 in any subject? (For this exercise, check English.)
# 5. Is her Mathematics score higher than her English score?


# Challenge 3: Movie Night 🎬
# You're planning a movie night with your friends.
# your_age = 14movie_age_limit = 16ticket_price = 5000your_money = 7000


# Check:
# 1. Are you old enough for the movie?
# 2. Can you afford the ticket?
# 3. Is your age below 18?
# 4. Is the ticket price exactly ₦5,000?
# 5. Do you have more money than the ticket costs?
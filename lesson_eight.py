# ELIF STATEMENT


test_score = 60


if test_score >= 70:
    print("A")
elif test_score >= 60:
    print("B")
elif test_score >= 50:
    print("C")
elif test_score >= 40:
    print("D")
else:
    print("F")



# An amusement park has different ticket prices depending on a visitor's age. You're building a program that automatically determines how much each visitor should pay.

# Ticket pricing:
# Age	Ticket price
# Below 5	Free
# 5–12	₦2,000
# 13–17	₦3,500
# 18–59	₦5,000
# 60 and above	₦3,000

# Your tasks:
# 1. Ask the visitor for their name and age.
# 2. Convert their age to an integer.
# 3. Use an if / elif / else chain to determine their ticket price.
# 4. Print their name and ticket price.
# 5. If the age is negative, display an invalid age message.


# You're building a feature for a coffee shop that has unreliable Wi-Fi. The shop wants to reward customers with discounts depending on how many Wi-Fi signal bars they receive.

# Write a Python program using an if / elif / else chain to determine the customer's discount.

# Discount rules:
# Wi-Fi signal bars	Discount / message
# 0 bars	50% off — "Sorry about the Wi-Fi!"
# 1–2 bars	25% off
# 3–4 bars	10% off
# 5 bars	No discount — "Full bars, no discount today!"

# Your tasks:
# 1. Ask the customer how many signal bars they have.
# 2. Convert their answer to an integer.
# 3. Use if, elif and else to check their signal strength.
# 4. Print the appropriate discount message.
# 5. If they enter a number below 0 or above 5, print an invalid signal message.
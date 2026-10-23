# Basic Arithmetic Operations

# Use of Multiplication, addition, substraction, division 


print(20/4)

# Challenge: Practice arithmetic operators
# 1. You have 200 songs in your library. You delete 47. Print how many are left.

total_songs = 200
deleted_songs = 47

remaining = total_songs - deleted_songs


print(remaining)
# 2. A movie ticket costs $12. You"re buying for yourself and 2 friends. print the total cost.

ticket_cost = 12

number_of_people = 3

total_cost = ticket_cost * number_of_people

print(f"${total_cost}")


# 3. You have 48 stickers to share equally among 6 friends. print how sony each person gets.

stickers = 48

number_of_friends = 6

sticker_per_person = 48 / 6

print(sticker_per_person)

# 4. You have $4200 in your wallet as your total revenue. You paid 3 staffs $50. You restocked goods of $1000 .Print how much I have left.

total_revenue = 4200
staff_payment = 3 * 50
goods_restock = 1000

balance = total_revenue - (staff_payment + goods_restock)
print(f"${balance}")

# Type Checking and Conversion

name = "Emmanuel"      # string (str)
age = 20               # integer (int)
price = 2500.50        # decimal (float)
is_student = True     # boolean (bool)

# cost = "300"

# cost = int(cost)

print(type(name))
print(type(age))
print(type(price))
print(type(is_student))


age = input("How old are you? ")


number_of_book = "14"

number_of_book_c = float(number_of_book)

number_of_pen = "12"

number_of_pen_c = float(number_of_pen)

total_x = number_of_book + number_of_pen

total_c = number_of_book_c + number_of_pen_c


print(total_x)
print(total_c)

print(type(age))


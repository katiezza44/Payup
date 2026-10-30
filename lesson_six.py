import random

# Challenge: Scramble word
# 1. Create a new file named lesson_six.py
# 2. Create a list of at least 3 words and save to a variable called "words"
# 3. Use random.choice() to pick a word from the list
# 4. use list(), random.shuffle(), and "".join() to scramble the word
# 5. Print the scrambled word

name = ["Emmanuel", "David", "Kelvin"]

random_name = random.choice(name)

print(random_name)


wrd = list(random_name)

random.shuffle(wrd)


print(wrd)
scrambled_wrd = "".join(wrd)

print(scrambled_wrd)



words = ["flower", "rei", "yuki"]
random_word = random.choice(words)
print(random_word)

word = list(random_word)
random.shuffle(word)
print(word)

scrambled_word = "".join(word)
print(scrambled_word)


# Equality Operator

password = "EMMANUEL"

user_password = input("What is your password? ")

print(password == user_password)


print(password != user_password)
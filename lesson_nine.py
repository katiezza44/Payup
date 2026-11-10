
import random
# get_name = input("What is my name? ").upper().strip()

# print(get_name)

# emmanuel oguntolu

# String methods

# .join()
# lower()
# upper()
# strip()
# title()

# design
# DESIGN
# desiGN
# Design

# Variable Original value Expected result
# promo_code "summer?25" "SUMMER?25"
# full_name "ada lovelace" "Ada Lovelace"
# email "  Ada@GMAIL.COM  " "ada@gmail.com"
# display_name "  the QUEEN  " "The Queen"
# country "nIGERIA" "Nigeria"

# promo_code = input("Please enter promo code. ").upper()
# print(promo_code)

# full_name = input("What is your name? ").title()
# print(full_name)

# email = input("What is your email? ").lower().strip()
# print(email)

# display_name = input("Please enter a display name. ").title().strip()
# print(display_name)

# country = input("Please enter a country. ").title()
# print(country)





words = ["rin","kaito", "luka", "len"]
random_word = random.choice(words)
print(random_word)
word = list(random_word)
random.shuffle(word)
print(word)
scrambled_word = "".join(word)
print(scrambled_word)

guess = input("Guess the word or type 'Skip' to skip. ").lower().strip()
if guess == "skip":
    print(f"Skip: The word is {random_word}. ")
elif guess == random_word:
    print("Correct!")
else:
    print("Game over.")
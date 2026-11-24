
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





# words = ["rin","kaito", "luka", "len"]

word_bank = [
    ("adventure", "Our trip to the mountains was an exciting ________"),
    ("whisper", "She had to ________ so she wouldn't wake the baby."),
    ("fall", "If he wasn't careful, he'd ______ off his bike.")    
]

word, hint = random.choice(word_bank)

letters = list(word)

# print(word)

random.shuffle(letters)

# print(word)

scrambled_word = "".join(letters)


print(scrambled_word)



guess = input("Guess the word choose 'hint' or 'skip' to skip. ").lower().strip()

if guess == "hint":
    print(f"Hint: {hint}")
    guess = input("Guess the word choose 'skip' to skip. ").lower().strip()

if guess == "skip":
    print(f"Skip: The word is {word}. ")
elif guess == word:
    print("Correct!")
else:
    print("Game over.")

# Tuples are immutable, meaning they cannot be changed after they are created. They are defined using parentheses () and can contain elements of different data types.


# about_me = ("Emmanuel", 22, "Nigeria", "Python Developer")

# about_me[0] # Accessing the first element of the tuple


# word_bank = [
    ("adventure", "Our trip to the mountains was an exciting ________"),
    ("whisper", "She had to ________ so she wouldn't wake the baby."),
    

# education , I love -------

# education , I love -------
print(20/4)
print(int(7.9))
number = int("12.5")
print(number)
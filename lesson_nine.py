
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
    ("algorithm", "A step-by-step set of instructions used to solve a problem."),
    ("database", "A place where an application stores and organises information."),
    ("password", "A secret combination used to protect your account."),
    ("notification", "A message that alerts you when something happens."),
    ("download", "To receive a file from the internet onto your device."),
    ("browser", "An application used to visit websites."),
    ("function", "A reusable block of code that performs a particular task."),
    ("variable", "A named location used to store information in a program."),
    ("firewall", "A security system that helps block unwanted network traffic."),
    ("interface", "The part of an application that users interact with."),
    ("adventure", "Our trip to the mountains was an exciting ________"),
    ("whisper", "She had to ________ so she wouldn't wake the baby."),
    ("fall", "If he wasn't careful, he'd ______ off his bike.")    
]


rounds = 5
round_number = 1
used = []
score = 0 

while round_number <= rounds:

    word, hint = random.choice(word_bank)

    while (word, hint) in used:
        word, hint = random.choice(word_bank)
    used.append((word, hint))


    letters = list(word)


    random.shuffle(letters)

    scrambled_word = "".join(letters)


    print(scrambled_word)

    guess = input("Guess the word choose 'hint', 'quit' or 'skip'").lower().strip()

    if guess == "hint":
        print(f"Hint: {hint}")
        guess = input("Guess the word choose 'skip' or 'quit'").lower().strip()

    if guess == "quit":
        print("Game over.")
        break

    if guess == "skip":
        print(f"Skip: The word is {word}. ")
    elif guess == word:
        score += 1
        print("Correct!")
    else:
        print("Game over.")

    round_number += 1
print("Thanks for playing!")

print(f"Your final score is {score} out of {rounds}")

# Tuples are immutable, meaning they cannot be changed after they are created. They are defined using parentheses () and can contain elements of different data types.


# about_me = ("Emmanuel", 22, "Nigeria", "Python Developer")

# about_me[0] # Accessing the first element of the tuple

# education , I love -------

# password = "Emmanuel"
# attempts = 4

# while attempts < 4:
#     guess = input("Please enter your password: ")
#     attempts += 1

#     if guess == password:
#         print("Phone Unlocked!")
#         break
#     else:
#         print("Incorect password")

# if attempts >= 4:
#     print("Phone locked!")
# education , I love -------
print(20/4)
print(int(7.9))
number = int("12.5")
print(number)



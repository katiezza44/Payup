import random

# Lists          → characters = [...]
archon = ["venti", "zhongli", "raiden", "nahida", "focalors" "mavuika", "tsaritsa"]


# Indexing       → characters[0]
first_word = archon[0]
second_word = archon[1]
third_word = archon[2]


# Negative index → characters[-1]
last_word = archon[-1]
second_last_word = archon[-2]

# Strings        → "design"
word = "design"
print(word)


# String indexing → "design"[2]

third_letter = "design"[2]
first_letter = "design"[0]


# list()         → list("design")
eula = list("eula")
# shuffle()      → random.shuffle(...)
random.shuffle(eula)

print(eula)

# join()         → "".join(...)
# Date Format  30/10/2026

todays_date = "/".join(["30", "10", "2026"])

print(todays_date)


# f-strings      → f"Hello {name}"

name = "Kadi"
(f"hello {name}")

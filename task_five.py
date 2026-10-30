import random

# Lists          → characters = [...]
archon = ["venti", "zhongli", "raiden", "nahida", "focalors" "mavuika", "tsaritsa"]
cities = ["london", "tokyo", "washinton DC"]


# Indexing       → characters[0]
first_word = archon[0]
second_word = archon[1]
third_word = archon[2]

first_city = cities[0]
second_city = cities[1]
third_city = cities[2]



# Negative index → characters[-1]
last_word = archon[-1]
second_last_word = archon[-2]

last_city = cities[-1]
second_last_city = cities[-2]

# Strings        → "design"
word = "design"
print(word)

city = "conakry"
print(city)

# String indexing → "design"[2]

third_letter = "design"[2]
first_letter = "design"[0]

second_letter = "design"[1]
fourth_letter = "design"[3]


# list()         → list("design")
eula = list("eula")
lisa = list("lisa")
# shuffle()      → random.shuffle(...)
random.shuffle(eula)

print(eula)

random.shuffle(lisa)
print(lisa)

# join()         → "".join(...)
# Date Format  30/10/2026

todays_date = "/".join(["30", "10", "2026"])

print(todays_date)

tomorrows_date = "/".join(["31","10","2026"])

print(tomorrows_date)


# f-strings      → f"Hello {name}"

name = "Kadi"
print(f"hello {name}")

nickname = "katie"
print(f"hello, {nickname}")

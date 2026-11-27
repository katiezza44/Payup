

cart = []


cart.append("Apple")
cart.append("Banana")
cart.append("Mango")
cart.append("Pear")

print(cart)

# playlist = []

# song = input("Add a song (or 'done)")

# while song != "done":
#     playlist.append(song)
#     song = input("Add a song (or 'done')")

# print(f"Your playlist: {playlist}")

# print(playlist)  # Accessing the first song in the playlist


print ("a" in "banana")
print ("n" in "mango")
print ("k" in "mango")


# while + in + append
import random

students = ["Emmanuel", "Tolu", "Ayo", "Bola", "Sade"]

past_class_captains = ["Tolu", "Ayo"]   

captain = random.choice(students)

while captain in past_class_captains:
    captain = random.choice(students)

print(f"The class captain is: {captain}")

past_class_captains.append(captain)

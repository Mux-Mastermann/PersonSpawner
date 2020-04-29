#! python

import requests
import time

# ask user for positive integer input
while True:
    n = input("Who many persons do you want to spawn? ")
    try:
        n = int(n)
    except Exception:
        print("You have to provide a positive integer!")
        continue
    else:
        if n in range(1, 51):
            break
        else:
            print("Choose an integer between 1 and 50")
            continue

print("Spawning Persons...")
for i in range(n):
    # get picture from https://thispersondoesnotexist.com/
    r = requests.get("https://thispersondoesnotexist.com/image", headers={
                     "User-Agent": "My User Agent 1.0"}).content
    # save image to a .png file
    with open(f"person{i + 1}.png", "wb") as f:
        f.write(r)
    # user indicating how many persons already there
    print(f"Hello Person {i + 1}!")
    # wait a moment, because otherwise the same persons will come from website
    time.sleep(2)

# SUCCESS MESSAGE
print(f"Successfully spawned {n} persons.")
time.sleep(3)

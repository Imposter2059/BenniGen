import requests
import random
import string
import time

print("""Benni Gen Forked Edition 1.0""")
time.sleep(0.2)
print("Credit goes to Benni (@bigbotboi on replit). Forked by @One9D on Discord.")
print("He was the dude who made this, I just forked it, and edited the code to say different stuff.")
print("Please tell him how awesome he is.")
time.sleep(1)
print("This is how to setup. Firstly, create a new folder, and place this file into that folder.")
print("Next, Create two text files; name the first one: 'Nitro Codes.txt', and the second one: 'Valid Codes.txt'.")
print("Have fun, and start digging! (Side note, if you leave this running on your pc and leave it, it will auto-close.)")
time.sleep(0.2)
print("(I almost forgot while finishing.)Also, it takes 12 hours to run 1,000,000 checks. A cool trick it learned was")
print("if you run two instances in this same folder, and make them both run 500,000 checks, then you run for only 6 hours!")
print("If you have a beefy pc you can keep making instances and cut the checks in half until its something short, like 3 hours.")
print("Anywho, have fun :D!")
time.sleep(0.2)
print("NITRO.CODES.txt/valid")
time.sleep(0.1)
print("Benni Nitro Gen Checker")
time.sleep(0.1)

num = int(input('Input How Many Codes to Generate and Check: '))

with open("Nitro Codes.txt", "w", encoding='utf-8') as file:
    print("Your nitro codes are being generated, be patient if you entered the high number!")

    start = time.time()

    for i in range(num):
        code = "".join(random.choices(
            string.ascii_uppercase + string.digits + string.ascii_lowercase,
            k = 16
        ))

        file.write(f"https://discord.gift/{code}\n")

    print(f"Generated {num} codes | Time taken: {time.time() - start}\n")

with open("Nitro Codes.txt") as file:
    for line in file.readlines():
        nitro = line.strip("\n")

        url = "https://discordapp.com/api/v6/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"

        r = requests.get(url)

        if r.status_code == 200:
            print(f" Valid | {nitro} ")
            break
        else:
            print(f" Invalid | {nitro} ")

input("\nYou have generated, Now press enter to close this, you'll get valid codes in Valid Codes.txt if you see its empty then you got no luck, generate 20 million codes for luck or else.")

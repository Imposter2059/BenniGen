import requests
import random
import string
import time

print("""Benni Gen Forked Edition 1.0""")
time.sleep(0.2)

print("Enter: 'A' to go to the credits.")
print("Enter: 'B' to go to the tutorial")
print("Enter: 'C' to go to the tips.")
print("Enter anything else to access the Primary Functions.")
print("    Please fullscreen for the best experience.")
print("")

user_input = input()

# Flag to track whether a special option was selected
special_option_selected = False

if user_input == "A":
    print("")
    print("Credit goes to Benni (@bigbotboi on replit). Forked by @One9D on Discord.")
    print("He was the dude who made the engine, I just forked it into software, and edited the code to say different stuff.")
    print("Please tell him how awesome he is.")
    special_option_selected = True
    print("This window will automatically close in 40 seconds.")
    time.sleep(40)

elif user_input == "B":
    print("")
    print("This is how to set up. Firstly, create a new folder, and place this file into that folder.")
    print("Next, create a file in that folder. Name it 'Valid Codes.txt', or in simpler terms, create a text file in that folder, name it Valid Codes.")
    print("Close this window and re-open it. After that, access the Primary Functions. Once it starts generating after you enter the details, it will create another text file containing invalid codes.")
    time.sleep(1)
    special_option_selected = True
    print("This window will automatically close in 40 seconds.")
    time.sleep(40)

elif user_input == "C":
    print("")
    print("(I almost forgot while finishing.) Also, it takes 12 hours to run 1,000,000 checks. A cool trick it learned was")
    print("if you run two instances in this same folder, and make them both run 500,000 checks, then you run for only 6 hours!")
    print("If you have a beefy pc you can keep making instances and cut the checks in half until it's something short, like 3 hours.")
    print("Have fun, and start digging! (Side note, if you leave this running on your pc and leave it, it will auto-close probably idk man.)")
    time.sleep(1)
    special_option_selected = True
    print("This window will automatically close in 40 seconds.")
    time.sleep(40)


# Move on to the primary functions if no special option was selected
if not special_option_selected:
    print("You chose the Primary Functions.")
    time.sleep(0.2)
    print("NITRO.CODES.txt/valid")
    time.sleep(0.1)
    print("Benni Nitro Gen Checker")
    time.sleep(0.1)

    num = int(input('Input How Many Codes to Generate and Check: ').strip())

    with open("Nitro Codes.txt", "w", encoding='utf-8') as file:
        print("Your nitro codes are being generated, be patient if you entered a high number!")

        start = time.time()

        for i in range(num):
            code = "".join(random.choices(
                string.ascii_uppercase + string.digits + string.ascii_lowercase,
                k=16
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

    input("\nYou have generated. Press enter to close this. Valid codes will be in Valid Codes.txt. If it's empty, you got no luck; generate more codes for better chances.")

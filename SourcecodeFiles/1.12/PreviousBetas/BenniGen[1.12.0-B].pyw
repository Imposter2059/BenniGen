import tkinter as tk
from tkinter import messagebox, scrolledtext, simpledialog
import random
import string
import requests
import time

class NitroGenApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Benni Gen Forked Edition v1.11")
        self.root.geometry("400x300")

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Please fullscreen for the best experience.").pack(pady=10)

        options_frame = tk.Frame(self.root)
        options_frame.pack(pady=10)

        tk.Button(options_frame, text="Credits", command=self.show_credits).grid(row=0, column=0, padx=5)
        tk.Button(options_frame, text="Tutorial", command=self.show_tutorial).grid(row=0, column=1, padx=5)
        tk.Button(options_frame, text="Tips", command=self.show_tips).grid(row=0, column=2, padx=5)
        tk.Button(options_frame, text="Changelog", command=self.show_changelog).grid(row=1, column=0, padx=5)
        tk.Button(options_frame, text="Version Display", command=self.show_version).grid(row=1, column=1, padx=5)
        tk.Button(options_frame, text="Primary Functions", command=self.show_primary_functions).grid(row=1, column=2, padx=5)

        tk.Label(self.root, text="NOTE: SUPPORT ON PLATFORMS OTHER THAN WINDOWS IS NOT GUARANTEED").pack(pady=10)

        # Frame for Primary Functions
        self.primary_frame = tk.Frame(self.root)

    def show_credits(self):
        messagebox.showinfo("Credits", "Credit goes to Benni (@bigbotboi on replit). Forked by @One9D on Discord.\n"
                                        "He was the dude who made the engine, I just forked it into software, "
                                        "and edited the code to say different stuff.\nPlease tell him how awesome he is.")

    def show_tutorial(self):
        messagebox.showinfo("Tutorial", "This is how to set up. Firstly, create a new folder, and place this file into that folder.\n"
                                         "Next, create a file in that folder. Name it 'Valid Codes.txt', or in simpler terms, "
                                         "create a text file in that folder, name it Valid Codes.\n"
                                         "Close this window and re-open it. After that, access the Primary Functions. "
                                         "Once it starts generating after you enter the details, it will create another text file containing invalid codes.")

    def show_tips(self):
        messagebox.showinfo("Tips", "(I almost forgot while finishing.) Also, it takes 12 hours to run 1,000,000 checks. "
                                     "A cool trick it learned was if you run two instances in this same folder, "
                                     "and make them both run 500,000 checks, then you run for only 6 hours!\n"
                                     "If you have a beefy pc you can keep making instances and cut the checks in half "
                                     "until it's something short, like 3 hours.\n"
                                     "Have fun, and start digging! (Side note, if you leave this running on your pc and leave it, "
                                     "it will auto-close probably idk man.)")

    def show_changelog(self):
        messagebox.showinfo("Changelog", "- Update v1.11 -\n"
                                         "- Moderate Patches -\n\n"
                                         "- Added Changelog\n"
                                         "- Added Version display\n"
                                         "- Added auto-fullscreen\n"
                                         "- Added depression towards the dev\n"
                                         "- Cleaned up internal code\n"
                                         "- Fixed Version number")

    def show_version(self):
        messagebox.showinfo("Version Display", "Model Version -:- v1.11(.0)\n"
                                              "- Standard Edition\n"
                                              "Advanced Version ID -:- v1.11.0-Stable")

    def show_primary_functions(self):
        # Clear previous widgets in primary frame
        for widget in self.primary_frame.winfo_children():
            widget.destroy()

        tk.Label(self.primary_frame, text="Primary Functions").pack(pady=10)

        num = simpledialog.askinteger("Primary Functions", "Input How Many Codes to Generate and Check:")

        generated_codes = []
        for _ in range(num):
            code = "".join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=16))
            generated_codes.append(f"https://discord.gift/{code}")

        valid_codes = self.check_codes(generated_codes)

        # Display results in a scrolled text widget
        result_text = scrolledtext.ScrolledText(self.primary_frame, width=40, height=10)
        result_text.pack(pady=10)

        result_text.insert(tk.END, f"Generated {num} codes | Valid codes: {len(valid_codes)}\n\n")
        result_text.insert(tk.END, "\n".join([f"{'Valid' if code in valid_codes else 'Invalid'} | {code}" for code in generated_codes]))

        self.primary_frame.pack(pady=10)

    def check_codes(self, codes):
        valid_codes = []
        for code in codes:
            url = f"https://discordapp.com/api/v6/entitlements/gift-codes/{code[19:]}?with_application=false&with_subscription_plan=true"
            r = requests.get(url)
            if r.status_code == 200:
                valid_codes.append(code)
        return valid_codes


if __name__ == "__main__":
    root = tk.Tk()
    app = NitroGenApp(root)
    root.mainloop()

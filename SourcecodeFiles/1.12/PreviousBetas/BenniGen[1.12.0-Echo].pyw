import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext, simpledialog
import random
import string
import requests
import time
import threading

class NitroGenApp:
    def __init__(self, root):
        self.root = root
        self.root.title("BenniGen Echo v1.12")
        self.root.geometry("432x500")
        self.root.resizable(False, False)

        self.create_widgets()
        self.log_text = scrolledtext.ScrolledText(self.root, width=40, height=10, fg="white", bg="black")
        self.log_text.pack(pady=10)

        # Default render speed
        self.render_speed = 0.01

    def create_widgets(self):
        tk.Label(self.root, text="Please fullscreen for the best experience.", fg="white", bg="black").pack(pady=10)

        options_frame = tk.Frame(self.root)
        options_frame.pack(pady=10)

        ttk.Button(options_frame, text="Credits", command=self.show_credits).grid(row=0, column=0, padx=5)
        ttk.Button(options_frame, text="Tutorial", command=self.show_tutorial).grid(row=0, column=1, padx=5)
        ttk.Button(options_frame, text="Tips", command=self.show_tips).grid(row=0, column=2, padx=5)
        ttk.Button(options_frame, text="Changelog", command=self.show_changelog).grid(row=1, column=0, padx=5)
        ttk.Button(options_frame, text="Version Display", command=self.show_version).grid(row=1, column=2, padx=5)
        ttk.Button(options_frame, text="Primary Functions", command=self.show_primary_functions).grid(row=2, column=1, padx=15)

        tk.Label(self.root, text="NOTE: SUPPORT ON PLATFORMS OTHER THAN WINDOWS IS NOT GUARANTEED", fg="white", bg="black").pack(pady=10)

        # Frame for Primary Functions
        self.primary_frame = tk.Frame(self.root)

        # Render Speed Label and Scale
        render_speed_label = ttk.Label(self.root, text="Render Speed:")
        render_speed_label.pack(pady=5)
        
        self.render_speed_scale = ttk.Scale(self.root, from_=0.00001, to=0.5, length=200, orient="horizontal", command=self.update_render_speed)
        self.render_speed_scale.set(0.01)  # Default render speed
        self.render_speed_scale.pack(pady=5)

    def update_render_speed(self, value):
        self.render_speed = float(value)

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
        messagebox.showinfo("Changelog", "- Update v1.12 -\n"
                                         "- UI Overhaul -\n\n"
                                         "- Added GUI\n"
                                         "- Updated System\n"
                                         "- Disabled Fullscreen\n"
                                         "- Updated depression towards the dev\n"
                                         "- Cleaned up internal code\n"
                                         "- Optimized Processes\n")

    def show_version(self):
        messagebox.showinfo("Version Display", "Model Version -:- v1.12(.0)\n"
                                              "- Standard Edition\n"
                                              "Advanced Version ID -:- v1.12.0-EchoCore")

    def show_primary_functions(self):
        # Clear previous widgets in primary frame
        for widget in self.primary_frame.winfo_children():
            widget.destroy()

        tk.Label(self.primary_frame, text="Primary Functions", fg="grey", bg="black").pack(pady=15)

        num = simpledialog.askinteger("Primary Functions", "Input How Many Codes to Generate and Check:")

        generated_codes = []
        for _ in range(num):
            code = "".join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=16))
            generated_codes.append(f"https://discord.gift/{code}")

        self.log_text.delete(1.0, tk.END)  # Clear the log

        # Run code checking in a separate thread to avoid freezing the GUI
        threading.Thread(target=self.check_codes, args=(generated_codes,), daemon=True).start()

        self.primary_frame.pack(pady=10)

    def check_codes(self, codes):
        valid_codes = []

        for code in codes:
            url = f"https://discordapp.com/api/v6/entitlements/gift-codes/{code[19:]}?with_application=false&with_subscription_plan=true"
            r = requests.get(url)

            if r.status_code == 200:
                valid_codes.append(code)

            time.sleep(self.render_speed)

            # Update the log
            self.log_text.insert(tk.END, f"Checking: {code}\n")
            self.log_text.yview(tk.END)  # Automatically scroll to the bottom of the log

        # Display the results in a messagebox
        messagebox.showinfo("Code Check Complete", f"Generated {len(codes)} codes\nValid Codes: {len(valid_codes)}\nInvalid Codes: {len(codes) - len(valid_codes)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = NitroGenApp(root)
    root.mainloop()

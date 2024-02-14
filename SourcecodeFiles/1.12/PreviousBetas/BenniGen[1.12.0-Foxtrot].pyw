import tkinter as tk
from tkinter import messagebox, scrolledtext, simpledialog
import random
import string
import requests
import time
import threading

class NitroGenApp:
    def __init__(self, root):
        self.root = root
        self.root.title("BenniGen Foxtrot v1.12")
        self.root.geometry("430x500")
        self.root.resizable(False, False)  # Disable window resizing

        self.render_speed = 0.0001  # Default render speed

        self.create_widgets()
        self.log_text = scrolledtext.ScrolledText(self.root, width=40, height=10, fg="white", bg="black")
        self.log_text.pack(pady=10)

    def create_widgets(self):
        tk.Label(self.root, text="Please fullscreen for the best experience.", fg="white", bg="black").pack(pady=10)

        tk.Button(self.root, text="Credits", command=self.show_credits).pack(pady=5)
        tk.Button(self.root, text="Tutorial", command=self.show_tutorial).pack(pady=5)
        tk.Button(self.root, text="Tips", command=self.show_tips).pack(pady=5)
        tk.Button(self.root, text="Changelog", command=self.show_changelog).pack(pady=5)
        tk.Button(self.root, text="Version Display", command=self.show_version).pack(pady=5)

        # Swap positions of "Render Speed" and "Primary Functions" buttons
        tk.Button(self.root, text="Render Speed", command=self.change_render_speed).pack(pady=5)
        
        # Increase font size for "Primary Functions" button
        primary_functions_button = tk.Button(self.root, text="Primary Functions", command=self.show_primary_functions, font=("Helvetica", 12, "bold"))
        primary_functions_button.pack(pady=10)

        tk.Label(self.root, text="NOTE: SUPPORT ON PLATFORMS OTHER THAN WINDOWS IS NOT GUARANTEED", fg="white", bg="black").pack(pady=10)

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
        messagebox.showinfo("Changelog", "- Update v1.12 -\n"
                                         "-  UI Overhaul -\n\n"
                                         "- Added GUI\n"
                                         "- Updated System\n"
                                         "- Disabled Fullscreen\n"
                                         "- Updated depression towards the dev\n"
                                         "- Cleaned up internal code\n"
                                         "- Optimized Processes\n")

    def show_version(self):
        messagebox.showinfo("Version Display", "Model Version -:- v1.12(.0)\n"
                                              "- Standard Edition\n"
                                              "Advanced Version ID -:- v1.12.0-FoxtrotCore")

    def show_primary_functions(self):
        for widget in self.primary_frame.winfo_children():
            widget.destroy()

        tk.Label(self.primary_frame, text="Primary Functions", fg="white", bg="black").pack(pady=10)

        num = simpledialog.askinteger("Primary Functions", "Input How Many Codes to Generate and Check:")

        generated_codes = [f"https://discord.gift/{''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=16))}" for _ in range(num)]

        self.log_text.delete(1.0, tk.END)

        threading.Thread(target=self.check_codes, args=(generated_codes,), daemon=True).start()

        self.primary_frame.pack(pady=10)

    def change_render_speed(self):
        render_speed = simpledialog.askfloat("Render Speed", "Enter Render Speed (0.000001 to 0.5)", minvalue=0.000001, maxvalue=0.5)
        if render_speed is not None:
            self.render_speed = render_speed

    def check_codes(self, codes):
        valid_codes = []

        for code in codes:
            url = f"https://discordapp.com/api/v6/entitlements/gift-codes/{code[19:]}?with_application=false&with_subscription_plan=true"
            r = requests.get(url)

            if r.status_code == 200:
                valid_codes.append(code)

            time.sleep(self.render_speed)

            self.log_text.insert(tk.END, f"Checking: {code}\n")
            self.log_text.yview(tk.END)

        messagebox.showinfo("Code Check Complete", f"Generated {len(codes)} codes\nValid Codes: {len(valid_codes)}\nInvalid Codes: {len(codes) - len(valid_codes)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = NitroGenApp(root)
    root.mainloop()

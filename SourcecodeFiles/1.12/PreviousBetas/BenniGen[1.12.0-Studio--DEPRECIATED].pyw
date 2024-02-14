import tkinter as tk
from tkinter import messagebox, simpledialog, scrolledtext
import random
import string
import requests
import threading
import time
import ctypes
import sys

class NitroGenApp:
    def __init__(self, root):
        self.root = root
        self.root.title("BenniGen Studio v1.12")
        self.root.geometry("500x800")
        self.root.resizable(False, False)

        self.render_speed = 0.0001  # Default render speed
        self.clutter_mode = False
        self.primary_functions_running = False

        self.create_widgets()
        self.log_text = scrolledtext.ScrolledText(self.root, width=50, height=15, fg="white", bg="black")
        self.log_text.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        self.primary_frame = tk.Frame(self.root)

    def create_widgets(self):
        tk.Label(self.root, text="Please close other windows for the best experience.", fg="white", bg="black").pack(pady=10)

        buttons = [
            ("Credits", self.show_credits),
            ("Tutorial", self.show_tutorial),
            ("Tips", self.show_tips),
            ("Changelog", self.show_changelog),
            ("Version Display", self.show_version),
            ("Render Speed", self.change_render_speed),
            ("Clutter Mode", self.toggle_clutter_mode),
            ("Primary Functions", self.show_primary_functions),
            ("Abort", self.abort),
            ("Admin Panel", self.show_admin_panel),
        ]

        for text, command in buttons:
            button = tk.Button(self.root, text=text, command=command, height=2, width=20)
            button.pack(pady=5)

            if "Primary Functions" in text:
                button.config(width=25, font=("Arial", 12, "bold"), fg="black")

        tk.Label(self.root, text="NOTE: SUPPORT ON PLATFORMS OTHER THAN WINDOWS IS NOT GUARANTEED", fg="white", bg="black").pack(pady=10)

    def show_credits(self):
        messagebox.showinfo("Credits", "Credit goes to Benni (@bigbotboi on replit). Forked by @One9D on Discord.\n"
                                        "He was the dude who made the engine, I just forked it into software, "
                                        "and edited the code to say different stuff.\nPlease tell him how awesome he is."
                                        "He is the one to Credit for the some of the Frame by Frame software and the main Algorithm. "
                                        "Um, credits to me? I guess I made the cluttered rendering system?")

    def show_tutorial(self):
        messagebox.showinfo("Tutorial", "I made it mostly automatic, this is straight forward. "
                            "You really do not need a tutorial bro. Are you dumb!?")

    def show_tips(self):
        messagebox.showinfo("Tips", "(I almost forgot while finishing.) Also, it takes 12 hours to run 1,000,000 checks. "
                                     "A cool trick it learned was if you run two instances in this same folder, "
                                     "and make them both run 500,000 checks, then you run for only 6 hours!\n"
                                     "If you have a beefy pc you can keep making instances and cut the checks in half "
                                     "until it's something short, like 3 hours.\n"
                                     "Have fun, and start digging! (Side note, if you leave this running on your pc and leave it, "
                                     "it will auto-close probably idk man.)")

    def show_changelog(self):
        messagebox.showinfo("Changelog", "- Update v1.12 Studio -\n"
                                         "- UI Overhaul -\n\n"
                                         "- Added GUI\n"
                                         "- Updated System\n"
                                         "- Disabled Fullscreen\n"
                                         "- Updated depression towards the dev\n"
                                         "- Cleaned up internal code\n"
                                         "- Optimized Processes\n"
                                         "- Added Cluttered Rendering System\n"
                                         "- Broke Frame by Frame System. (didnt have time to fix must release)")

    def show_version(self):
        messagebox.showinfo("Version Display", "Model Version -:- v1.12(.0)\n"
                                              "- Studio Edition\n"
                                              "Advanced Version ID -:- v1.12.0-Studio")

    def show_primary_functions(self):
        if not self.primary_functions_running:
            for widget in self.primary_frame.winfo_children():
                widget.destroy()

            tk.Label(self.primary_frame, text="Primary Functions", fg="white", bg="black").pack(pady=10)

            num = simpledialog.askinteger("Primary Functions", "Input How Many Codes to Generate and Check:")

            generated_codes = [f"https://discord.gift/{''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=16))}" for _ in range(num)]

            self.log_text.delete(1.0, tk.END)

            threading.Thread(target=self.check_all_codes, args=(generated_codes,), daemon=True).start()

            self.primary_frame.pack(pady=10)

    def change_render_speed(self):
        if not self.primary_functions_running:
            render_speed = simpledialog.askfloat("Render Speed", "Enter Render Speed (0.000001 to 0.5)", minvalue=0.000001, maxvalue=0.5)
            if render_speed is not None:
                self.render_speed = render_speed

    def toggle_clutter_mode(self):
        if not self.primary_functions_running:
            self.clutter_mode = not self.clutter_mode
            mode_text = "On" if self.clutter_mode else "Off"
            messagebox.showinfo("Clutter Mode", f"Clutter Mode: {mode_text}")
            if self.clutter_mode:
                self.disable_render_speed_button()
            else:
                self.enable_render_speed_button()

    def check_all_codes(self, codes):
        results = {"valid_codes": []}

        threads = []

        for code in codes:
            thread = threading.Thread(target=self.check_code, args=(code, results))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        self.primary_functions_running = False

        messagebox.showinfo("Code Check Complete", f"Generated {len(codes)} codes\nValid Codes: {len(results['valid_codes'])}\nInvalid Codes: {len(codes) - len(results['valid_codes'])}")

    def check_code(self, code, results):
        url = f"https://discordapp.com/api/v6/entitlements/gift-codes/{code[19:]}?with_application=false&with_subscription_plan=true"
        r = requests.get(url)

        if r.status_code == 200:
            results["valid_codes"].append(code)

        self.log_text.insert(tk.END, f"Checking: {code}\n")
        self.log_text.yview(tk.END)

    def disable_render_speed_button(self):
        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Button) and "Render Speed" in widget.cget("text"):
                widget.config(state=tk.DISABLED)

    def enable_render_speed_button(self):
        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Button) and "Render Speed" in widget.cget("text"):
                widget.config(state=tk.NORMAL)

    def abort(self):
        self.root.destroy()

    def show_admin_panel(self):
        answer = messagebox.askyesno("Admin Panel", "Do you want to run this file as administrator?")
        if answer:
            self.show_prioritize_button()

    def show_prioritize_button(self):
        tk.Label(self.root, text="Admin Panel", fg="white", bg="black").pack(pady=10)
        tk.Button(self.root, text="Prioritize Program", command=self.prioritize_program).pack(pady=5)

    def prioritize_program(self):
        # The following command attempts to run the script as an administrator
        try:
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to prioritize program: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = NitroGenApp(root)
    root.mainloop()

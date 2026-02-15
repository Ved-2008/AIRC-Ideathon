import tkinter as tk
import random

students = {}
trash_types = ["Paper", "Plastic", "Organic"]

total_items = 0  # campus recycling counter

window = tk.Tk()
window.title("Smart Trash Bin Reward System")
window.geometry("400x550")

def clear_screen():
    for widget in window.winfo_children():
        widget.destroy()

# HOME SCREEN 
def home_screen():
    clear_screen()
    tk.Label(window, text="Smart Recycling System",
             font=("Helvetica", 16, "bold")).pack(pady=40)

    tk.Label(window, text="Is this your first time?").pack(pady=10)

    tk.Button(window, text="Yes - Sign Up", width=20,
              command=signup_screen).pack(pady=10)

    tk.Button(window, text="No - Deposit Trash", width=20,
              command=deposit_screen).pack(pady=10)

# SIGNUP SCREEN 
def signup_screen():
    clear_screen()

    tk.Label(window, text="Sign Up",
             font=("Helvetica", 14, "bold")).pack(pady=10)

    tk.Label(window, text="Name").pack()
    name_entry = tk.Entry(window)
    name_entry.pack(pady=5)

    tk.Label(window, text="UID").pack()
    uid_entry = tk.Entry(window)
    uid_entry.pack(pady=5)

    feedback = tk.Label(window, text="")
    feedback.pack()

    def register():
        name = name_entry.get().strip()
        uid = uid_entry.get().strip()

        if name == "" or uid == "":
            feedback.config(text="Fill all fields", fg="red")
            return

        if uid in students:
            feedback.config(text="UID already exists", fg="red")
            return

        students[uid] = {"name": name, "score": 0}
        feedback.config(text="Registration successful!", fg="green")

    tk.Button(window, text="Register", command=register).pack(pady=10)
    tk.Button(window, text="Back to Home", command=home_screen).pack(pady=5)

# DEPOSIT SCREEN
def deposit_screen():
    clear_screen()

    tk.Label(window, text="Deposit Trash",
             font=("Helvetica", 14, "bold")).pack(pady=10)

    tk.Label(window, text="Enter UID").pack()
    uid_entry = tk.Entry(window)
    uid_entry.pack(pady=5)

    feedback = tk.Label(window, text="")
    feedback.pack()

    score_label = tk.Label(window, text="")
    score_label.pack(pady=5)

    total_label = tk.Label(window, text="")
    total_label.pack(pady=5)

    leaderboard = tk.Listbox(window)
    leaderboard.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

    def update_leaderboard():
        leaderboard.delete(0, tk.END)
        sorted_students = sorted(
            students.items(),
            key=lambda x: x[1]["score"],
            reverse=True
        )
        for uid, data in sorted_students:
            leaderboard.insert(tk.END, f"{data['name']} : {data['score']}")

    def process_deposit():
        global total_items

        uid = uid_entry.get().strip()

        if uid not in students:
            feedback.config(text="UID not found. Please sign up.", fg="red")
            return

        feedback.config(text="Processing classification...", fg="blue")

        window.after(1500, lambda: complete_deposit(uid))

    def complete_deposit(uid):
        global total_items

        total_items += 1
        students[uid]["score"] += 10

        feedback.config(text="Trash Classified Successfully! +10 points",
                        fg="green")

        score_label.config(text=f"Your Score: {students[uid]['score']}")
        total_label.config(text=f"Total Items Recycled (Campus): {total_items}")

        update_leaderboard()

    tk.Button(window, text="Deposit Trash",
              command=process_deposit).pack(pady=10)

    tk.Button(window, text="Back to Home",
              command=home_screen).pack(pady=5)

# Start app
home_screen()
window.mainloop()
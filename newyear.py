import tkinter as tk
from tkinter import messagebox

# Function to generate wishes
def generate_wish():
    name = name_entry.get()
    wish_type = wish_var.get()
    
    if not name:
        messagebox.showwarning("Input Error", "Please enter the recipient's name.")
        return
    
    if wish_type == "Heartfelt":
        wish = f"Happy New Year, {name}! 🌟 May 2024 bring you endless joy, success, and beautiful moments. You're truly special, and I wish you all the happiness in the world!"
    elif wish_type == "Flirty":
        wish = f"Happy New Year, {name}! 😉 Just a little wish from me to you—may your 2024 be as amazing as your smile. Here's to a year full of surprises (hopefully including me)!"
    elif wish_type == "Funny":
        wish = f"Hey {name}, Happy New Year! 🎉 Here's to a 2024 where your resolutions last longer than your Wi-Fi signal. 😉 Stay awesome!"
    else:
        wish = f"Happy New Year, {name}! 🎆 Wishing you all the best for an amazing year ahead!"
    
    result_label.config(text=wish)

# Function to save the wish
def save_wish():
    wish_text = result_label.cget("text")
    if not wish_text:
        messagebox.showwarning("Save Error", "No wish to save! Generate a wish first.")
        return
    
    with open("new_year_wish.txt", "w") as file:
        file.write(wish_text)
    messagebox.showinfo("Success", "Wish saved to new_year_wish.txt!")

# GUI Setup
root = tk.Tk()
root.title("New Year Wishes Generator")
root.geometry("400x400")

# Input fields
tk.Label(root, text="Enter Recipient's Name:", font=("Arial", 12)).pack(pady=10)
name_entry = tk.Entry(root, width=30, font=("Arial", 12))
name_entry.pack(pady=5)

tk.Label(root, text="Choose Wish Type:", font=("Arial", 12)).pack(pady=10)
wish_var = tk.StringVar(value="Heartfelt")
tk.Radiobutton(root, text="Heartfelt", variable=wish_var, value="Heartfelt", font=("Arial", 10)).pack()
tk.Radiobutton(root, text="Flirty", variable=wish_var, value="Flirty", font=("Arial", 10)).pack()
tk.Radiobutton(root, text="Funny", variable=wish_var, value="Funny", font=("Arial", 10)).pack()

# Buttons
tk.Button(root, text="Generate Wish", command=generate_wish, font=("Arial", 12), bg="lightblue").pack(pady=10)
tk.Button(root, text="Save Wish to File", command=save_wish, font=("Arial", 12), bg="lightgreen").pack(pady=5)

# Result display
result_label = tk.Label(root, text="", wraplength=350, font=("Arial", 12), fg="darkblue")
result_label.pack(pady=20)

# Run the application
root.mainloop()

import tkinter as tk
from tkinter import messagebox


def open_igbo_dictionary():
    # Dickson Igbo code
    print("Igbo Dictionary: [Add your code here]")
    messagebox.showinfo("Igbo Dictionary", "Displaying Igbo dictionary...")

def open_hausa_dictionary():
    # Daniel Hausa code
    print("Hausa Dictionary: [Add your code here]")
    messagebox.showinfo("Hausa Dictionary", "Displaying Hausa dictionary...")

def open_yoruba_dictionary():
    # Toby Yoruba code
    print("Yoruba Dictionary: [Add your code here]")
    messagebox.showinfo("Yoruba Dictionary", "Displaying Yoruba dictionary...")

def open_igala_dictionary():
    # David Igala code
    print("Ijala Dictionary: [Add your code here]")
    messagebox.showinfo("Ijala Dictionary", "Displaying Igala dictionary...")

def open_tiv_dictionary():
    # David Tiv code (mine)
    print("Tiv Dictionary: [Add your code here]")
    messagebox.showinfo("Tiv Dictionary", "Displaying Tiv dictionary...")

# Create the main window
root = tk.Tk()
root.title("Nigerian Languages Dictionary")
root.geometry("600x250")

# Add a label
label = tk.Label(root, text="DICTIONARY\nNIGERIAN LANGUAGES\nClick Preferred Language", font=("Arial", 12), justify="center")
label.pack(pady=20)

# Add buttons for each language
languages = {
    "Igbo Language": open_igbo_dictionary,
    "Hausa Language": open_hausa_dictionary,
    "Yoruba Language": open_yoruba_dictionary,
    "Igala Language": open_igala_dictionary,
    "Tiv Language": open_tiv_dictionary,
}

for language, command in languages.items():
    button = tk.Button(root, text=language, font=("Times New Roman", 10), width=20, command=command)
    button.pack(pady=5)

# Run the GUI
root.mainloop()
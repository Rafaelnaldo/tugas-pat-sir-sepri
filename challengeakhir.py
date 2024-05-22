import tkinter as tk
import ttkbootstrap as tb
import random

man_names = ["Udin", "Asep", "Joko", "Anwar", "Pardede","Arif","Budi","Deni","Candra","Eko"]
woman_names = ["Siti", "Lina", "Dewi", "Nurul", "Rina","Ayu","Bela","Eka","Gita","Indah"]
chances = 3
chosen_gender = None

def pick_gender(gender):
    global chosen_gender, chances
    chosen_gender = gender
    chances = 3
    button.config(state=tk.NORMAL)
    if gender == "man":
        label.config(text="Man's name")
        woman_button.config(state=tk.DISABLED)
    else:
        label.config(text="Woman's name")
        man_button.config(state=tk.DISABLED)
    chance_label.config(text=f"Chances Left: {chances}")

def pick_name():
    global chances, chosen_gender
    if chosen_gender == "man" and man_names and chances > 0:
        selected_name = random.choice(man_names)
        man_names.remove(selected_name)
    elif chosen_gender == "woman" and woman_names and chances > 0:
        selected_name = random.choice(woman_names)
        woman_names.remove(selected_name)
    else:
        label.config(text="No more names left.")
        button.config(state=tk.DISABLED)
        return

    label.config(text=f"Selected {chosen_gender}'s Name: {selected_name}")
    chances -= 1
    chance_label.config(text=f"Chances to draw: {chances}")

root = tb.Window(themename="cosmo")
root.title("Name Picker")
root.geometry("800x500")

label = tb.Label(root, text="Choose Your Gender", font=("Arial", 14))
label.pack(pady=20)

man_button = tb.Button(root, text="Man", command=lambda: pick_gender("man"), bootstyle="primary")
man_button.pack(pady=10)

woman_button = tb.Button(root, text="Woman", command=lambda: pick_gender("woman"), bootstyle="danger")
woman_button.pack(pady=10)

chance_label = tb.Label(root, text=f"Chances Left: {chances}", font=("Arial", 12))
chance_label.pack()

button = tb.Button(root, text="Pick a Name", command=pick_name, bootstyle="primary", state=tk.DISABLED)
button.pack(pady=20)

root.mainloop()

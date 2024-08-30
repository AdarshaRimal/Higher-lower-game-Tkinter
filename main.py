import random
import tkinter as tk
from game_data import data

# Function to pick a random item from the data list
def random_data():
    return random.choice(data)

# Function to compare follower counts
def compare_follower(choice):
    if choice == "A":
        return first_data["follower_count"] > second_data["follower_count"]
    elif choice == "B":
        return second_data["follower_count"] > first_data["follower_count"]

# Function to update the GUI with new data
def update_data():
    global first_data, second_data
    first_data = second_data
    second_data = random_data()
    while first_data == second_data:
        second_data = random_data()
    update_labels()

# Function to update the labels and buttons in the GUI
def update_labels():
    label_a.config(text=f"Compare A: {first_data['name']}, a {first_data['description']} from {first_data['country']}")
    label_b.config(text=f"Compare B: {second_data['name']}, a {second_data['description']} from {second_data['country']}")
    button_a.config(text=first_data['name'])
    button_b.config(text=second_data['name'])

# Function to handle the user's choice
def on_choice(choice):
    global score, game_over
    if compare_follower(choice):
        score += 1
        result_label.config(text=f"You are right! Score: {score}")
        update_data()
    else:
        result_label.config(text=f"You are wrong. Final Score: {score}")
        game_over = True
        disable_buttons()

# Function to disable buttons when the game is over
def disable_buttons():
    button_a.config(state="disabled")
    button_b.config(state="disabled")

# Initialize the game
first_data = random_data()
second_data = random_data()
while first_data == second_data:
    second_data = random_data()
score = 0
game_over = False

# Setup the Tkinter window
root = tk.Tk()
root.title("Higher or Lower Game")
root.geometry("500x300")

# Labels for displaying the data
label_a = tk.Label(root, text="", wraplength=400)
label_a.pack(pady=20)
label_b = tk.Label(root, text="", wraplength=400)
label_b.pack(pady=20)

# Buttons for choosing A or B
button_a = tk.Button(root, text="", command=lambda: on_choice("A"))
button_a.pack(side="left", padx=50, pady=20)

button_b = tk.Button(root, text="", command=lambda: on_choice("B"))
button_b.pack(side="right", padx=50, pady=20)

# Label for displaying the result
result_label = tk.Label(root, text="")
result_label.pack(pady=20)

# Initial update to show data
update_labels()

# Start the Tkinter main loop
root.mainloop()

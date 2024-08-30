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
    label_b.config(
        text=f"Compare B: {second_data['name']}, a {second_data['description']} from {second_data['country']}")
    button_a.config(text=first_data['name'])
    button_b.config(text=second_data['name'])


# Function to handle the user's choice
def on_choice(choice):
    global score, game_over
    if compare_follower(choice):
        score += 1
        result_label.config(text=f"You are right! Score: {score}")
    else:
        result_label.config(text=f"You are wrong. Final Score: {score}")
        game_over = True
        disable_buttons()

    # Adjust label size based on text length
    adjust_label_size()
    update_data()


# Function to disable buttons when the game is over
def disable_buttons():
    button_a.config(state="disabled")
    button_b.config(state="disabled")


# Function to adjust the result label size
def adjust_label_size():
    text_length = len(result_label.cget("text"))
    if text_length > 50:  # Arbitrary threshold for longer text
        result_label.config(height=4)  # Increase height for longer text
    else:
        result_label.config(height=2)  # Default height for shorter text


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
root.geometry("500x400")

# Labels for displaying the data
label_a = tk.Label(root, text="", wraplength=400)
label_a.grid(row=0, column=0, columnspan=2, pady=10, padx=10)

# "VS" Label in a larger font
vs_label = tk.Label(root, text="VS", font=("Helvetica", 24, "bold"))
vs_label.grid(row=1, column=0, columnspan=2)

label_b = tk.Label(root, text="", wraplength=400)
label_b.grid(row=2, column=0, columnspan=2, pady=10, padx=10)

# Buttons for choosing A or B
button_a = tk.Button(root, text="", command=lambda: on_choice("A"))
button_a.grid(row=3, column=0, pady=20, padx=50)

button_b = tk.Button(root, text="", command=lambda: on_choice("B"))
button_b.grid(row=3, column=1, pady=20, padx=50)

# Label for displaying the result
result_label = tk.Label(root, text="", wraplength=400, height=2)
result_label.grid(row=4, column=0, columnspan=2, pady=20, sticky="ew")

# Initial update to show data
update_labels()

# Start the Tkinter main loop
root.mainloop()

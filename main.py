import tkinter as tk
from tkinter import messagebox
import pyjokes

# Function to generate a joke
def tell_joke():
    joke = pyjokes.get_joke()
    joke_label.config(text=joke)

# Create main window
root = tk.Tk()
root.title("Offline Joke Generator")
root.geometry("500x300")
root.resizable(False, False)

# Heading
heading = tk.Label(root, text="😂 Offline Joke Generator", font=("Helvetica", 18, "bold"))
heading.pack(pady=20)

# Joke display
joke_label = tk.Label(root, text="Click 'Get Joke' to start!", wraplength=400, justify="center", font=("Helvetica", 14))
joke_label.pack(pady=20)

# Button to generate joke
joke_button = tk.Button(root, text="Get Joke", command=tell_joke, font=("Helvetica", 14), bg="#4CAF50", fg="white")
joke_button.pack(pady=10)

# Exit button
exit_button = tk.Button(root, text="Exit", command=root.destroy, font=("Helvetica", 12))
exit_button.pack(pady=5)

# Run the app
root.mainloop()

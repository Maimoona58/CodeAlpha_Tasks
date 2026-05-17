import tkinter as tk
import random

quotes = [
    {"text": "The best way to get started is to quit talking and begin doing.", "author": "Walt Disney"},
    {"text": "Success is not in what you have, but who you are.", "author": "Bo Bennett"},
    {"text": "Don’t let yesterday take up too much of today.", "author": "Will Rogers"},
    {"text": "It always seems impossible until it’s done.", "author": "Nelson Mandela"},
    {"text": "Push yourself, because no one else is going to do it for you.", "author": "Unknown"}
]

def show_quote():
    quote = random.choice(quotes)
    quote_label.config(text=f'"{quote["text"]}"')
    author_label.config(text=f'- {quote["author"]}')

     # UI
root = tk.Tk()
root.title("Random Quote Generator")
root.geometry("400x300")

quote_label = tk.Label(root, text="", wraplength=350, font=("Arial", 12), justify="center")
quote_label.pack(pady=30)

author_label = tk.Label(root, text="", font=("Arial", 10, "italic"))
author_label.pack(pady=10)

btn = tk.Button(root, text="New Quote", command=show_quote)
btn.pack(pady=20)

      # Show first quote
show_quote()

root.mainloop()
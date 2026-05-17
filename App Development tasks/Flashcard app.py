import tkinter as tk
from tkinter import messagebox

# Flashcard data
flashcards = []
current_index = 0
show_answer = False

# Functions
def update_card():
    global show_answer
    if not flashcards:
        card_label.config(text="No flashcards available")
        return
    
    card = flashcards[current_index]
    if show_answer:
        card_label.config(text=card["answer"])
    else:
        card_label.config(text=card["question"])

def toggle_answer():
    global show_answer
    show_answer = not show_answer
    update_card()

def next_card():
    global current_index, show_answer
    if current_index < len(flashcards) - 1:
        current_index += 1
        show_answer = False
        update_card()

def prev_card():
    global current_index, show_answer
    if current_index > 0:
        current_index -= 1
        show_answer = False
        update_card()

def add_card():
    q = question_entry.get()
    a = answer_entry.get()
    
    if q == "" or a == "":
        messagebox.showwarning("Input Error", "Please enter both question and answer")
        return
    
    flashcards.append({"question": q, "answer": a})
    question_entry.delete(0, tk.END)
    answer_entry.delete(0, tk.END)
    update_card()

def delete_card():
    global current_index
    if not flashcards:
        return
    
    flashcards.pop(current_index)
    
    if current_index >= len(flashcards):
        current_index = max(0, len(flashcards) - 1)
    
    update_card()

def edit_card():
    if not flashcards:
        return
    
    q = question_entry.get()
    a = answer_entry.get()
    
    if q == "" or a == "":
        messagebox.showwarning("Input Error", "Please enter both question and answer")
        return
    
    flashcards[current_index] = {"question": q, "answer": a}
    update_card()

# UI Setup
root = tk.Tk()
root.title("Flashcard Quiz App")
root.geometry("400x400")

card_label = tk.Label(root, text="No flashcards available", wraplength=300, font=("Arial", 14), height=6)
card_label.pack(pady=20)

show_btn = tk.Button(root, text="Show Answer", command=toggle_answer)
show_btn.pack()

nav_frame = tk.Frame(root)
nav_frame.pack(pady=10)

prev_btn = tk.Button(nav_frame, text="Previous", command=prev_card)
prev_btn.grid(row=0, column=0, padx=10)

next_btn = tk.Button(nav_frame, text="Next", command=next_card)
next_btn.grid(row=0, column=1, padx=10)

# Entry fields
question_entry = tk.Entry(root, width=40)
question_entry.pack(pady=5)
question_entry.insert(0, "Enter question")

answer_entry = tk.Entry(root, width=40)
answer_entry.pack(pady=5)
answer_entry.insert(0, "Enter answer")

# Action buttons
btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

add_btn = tk.Button(btn_frame, text="Add", command=add_card)
add_btn.grid(row=0, column=0, padx=5)

edit_btn = tk.Button(btn_frame, text="Edit", command=edit_card)
edit_btn.grid(row=0, column=1, padx=5)

delete_btn = tk.Button(btn_frame, text="Delete", command=delete_card)
delete_btn.grid(row=0, column=2, padx=5)

root.mainloop()

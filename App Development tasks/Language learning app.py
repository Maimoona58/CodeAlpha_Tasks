import tkinter as tk
from tkinter import messagebox
import random


# Language Learning Data
# -----------------------------
lessons = {
    "Vocabulary": [
        {"english": "Hello", "translation": "Hola"},
        {"english": "Thank You", "translation": "Shukria"},
        {"english": "Good Morning", "translation": "Suba bakhair"},
    ],
    
    "Grammar": [
        {"english": "I am a student", "translation": "M student hn"},
        {"english": "She is happy", "translation": "M khush hn"},
        {"english": "We are friends", "translation": "Ham dost han"},
    ]
}

current_category = "Vocabulary"
current_index = 0
show_translation = False

# -----------------------------
# Functions
# -----------------------------
def update_card():
    global show_translation

    data = lessons[current_category]

    if not data:
        card_label.config(text="No lessons available")
        return

    lesson = data[current_index]

    if show_translation:
        card_label.config(
            text=f"{lesson['translation']}\n\nPronunciation:\n{lesson['translation']}"
        )
    else:
        card_label.config(text=lesson["english"])

    progress_label.config(
        text=f"{current_index + 1} / {len(data)}"
    )


def show_answer():
    global show_translation
    show_translation = True
    update_card()


def next_card():
    global current_index, show_translation

    data = lessons[current_category]

    if current_index < len(data) - 1:
        current_index += 1
        show_translation = False
        update_card()


def previous_card():
    global current_index, show_translation

    if current_index > 0:
        current_index -= 1
        show_translation = False
        update_card()


def change_category(category):
    global current_category, current_index, show_translation

    current_category = category
    current_index = 0
    show_translation = False

    update_card()


def add_word():
    english = english_entry.get()
    translation = translation_entry.get()

    if english == "" or translation == "":
        messagebox.showwarning(
            "Input Error",
            "Please fill both fields"
        )
        return

    lessons[current_category].append({
        "english": english,
        "translation": translation
    })

    english_entry.delete(0, tk.END)
    translation_entry.delete(0, tk.END)

    messagebox.showinfo(
        "Success",
        "Word added successfully!"
    )

    update_card()


def start_quiz():
    data = lessons[current_category]

    if not data:
        return

    question = random.choice(data)

    answer = tk.simpledialog.askstring(
        "Quiz",
        f"What is the translation of:\n\n{question['english']}?"
    )

    if answer is None:
        return

    if answer.lower() == question["translation"].lower():
        messagebox.showinfo(
            "Correct",
            "Correct Answer!"
        )
    else:
        messagebox.showerror(
            "Wrong",
            f"Correct answer is:\n{question['translation']}"
        )


# -----------------------------
# Main Window
# -----------------------------
root = tk.Tk()
root.title("Language Learning App")
root.geometry("550x550")
root.config(bg="#f0f4f7")

# -----------------------------
# Title
# -----------------------------
title = tk.Label(
    root,
    text="Language Learning App",
    font=("Arial", 20, "bold"),
    bg="#f0f4f7",
    fg="#333"
)
title.pack(pady=15)

# -----------------------------
# Category Buttons
# -----------------------------
category_frame = tk.Frame(root, bg="#f0f4f7")
category_frame.pack()

vocab_btn = tk.Button(
    category_frame,
    text="Vocabulary",
    width=15,
    command=lambda: change_category("Vocabulary")
)
vocab_btn.grid(row=0, column=0, padx=10)

grammar_btn = tk.Button(
    category_frame,
    text="Grammar",
    width=15,
    command=lambda: change_category("Grammar")
)
grammar_btn.grid(row=0, column=1, padx=10)

# -----------------------------
# Flashcard Area
# -----------------------------
card_label = tk.Label(
    root,
    text="",
    font=("Arial", 16),
    bg="white",
    width=30,
    height=8,
    relief="solid",
    wraplength=400
)
card_label.pack(pady=20)

progress_label = tk.Label(
    root,
    text="",
    font=("Arial", 12),
    bg="#f0f4f7"
)
progress_label.pack()

# -----------------------------
# Navigation Buttons
# -----------------------------
nav_frame = tk.Frame(root, bg="#f0f4f7")
nav_frame.pack(pady=15)

prev_btn = tk.Button(
    nav_frame,
    text="Previous",
    width=12,
    command=previous_card
)
prev_btn.grid(row=0, column=0, padx=10)

show_btn = tk.Button(
    nav_frame,
    text="Show Translation",
    width=15,
    command=show_answer
)
show_btn.grid(row=0, column=1, padx=10)

next_btn = tk.Button(
    nav_frame,
    text="Next",
    width=12,
    command=next_card
)
next_btn.grid(row=0, column=2, padx=10)

# -----------------------------
# Add New Words
# -----------------------------
form_frame = tk.Frame(root, bg="#f0f4f7")
form_frame.pack(pady=20)

tk.Label(
    form_frame,
    text="English Word:",
    bg="#f0f4f7"
).grid(row=0, column=0, padx=5, pady=5)

english_entry = tk.Entry(form_frame, width=30)
english_entry.grid(row=0, column=1)

tk.Label(
    form_frame,
    text="Translation:",
    bg="#f0f4f7"
).grid(row=1, column=0, padx=5, pady=5)

translation_entry = tk.Entry(form_frame, width=30)
translation_entry.grid(row=1, column=1)

add_btn = tk.Button(
    root,
    text="Add Lesson",
    width=20,
    command=add_word
)
add_btn.pack(pady=10)

# Quiz Button

quiz_btn = tk.Button(
    root,
    text="Start Quiz",
    width=20,
    bg="#4CAF50",
    fg="white",
    command=start_quiz
)
quiz_btn.pack(pady=15)

# Start App

update_card()

root.mainloop()
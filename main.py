from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
learn_words = {}
words = {}

try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    words = original_data.to_dict(orient="records")
else:
    words = data.to_dict(orient="records")

def button_click():
    global learn_words, flip_timer
    window.after_cancel(flip_timer)
    learn_words = random.choice(words)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=learn_words["French"], fill="black")
    canvas.itemconfig(card_image, image=card_front)
    flip_timer = window.after(3000, func=flip)

def flip():
    canvas.itemconfig(card_image, image=card_back)
    canvas.itemconfig(card_title, text="English", fill = "white")
    canvas.itemconfig(card_word, text=learn_words["English"], fill = "white")

def is_known():
    words.remove(learn_words)
    words_to_learn = pd.DataFrame(words)
    words_to_learn.to_csv("data/words_to_learn", index=False)
    
    
    button_click()



window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip)
 
canvas = Canvas(width=800, height=526)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
card_image = canvas.create_image(400, 263, image=card_front)
card_title = canvas.create_text(400, 150, text="title", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Arial", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button=Button(image=wrong_image, highlightthickness=0, command=button_click)
wrong_button.grid(column=0, row=1)

right_image = PhotoImage(file="images/right.png")
right_button=Button(image=right_image, highlightthickness=0, command=is_known)
right_button.grid(column=1, row=1)


button_click()


window.mainloop()
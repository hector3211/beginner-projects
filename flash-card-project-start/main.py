from tkinter import *
from tkinter import messagebox
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
current_question = {}
new_df = {}
try:
    # Pandas read_csv ----------------------------------------------------------------
    df = pd.read_csv("/Users/hectororopesa/Documents/GUI/flash-card-project-start/data/questions to learn.csv")
except FileNotFoundError:
    # If the file doesn't exist --------------------------------'
    original_data = pd.read_csv("/Users/hectororopesa/Documents/GUI/flash-card-project-start/data/Moms citizens test questions - Sheet1.csv")
    new_df= original_data.to_dict(orient="records")
else:
    new_df = df.to_dict(orient="records")



# Generate French words ------------------------------------------------
def gen_word_french():
    global current_question, flip_card_timer
    window.after_cancel(flip_card_timer)
    current_question = random.choice(new_df)
    canvas.itemconfig(word_title, text = "Question", fill = "black")
    canvas.itemconfig(word_label, text = current_question['Questions'], fill = "black")
    canvas.itemconfig(canvas_background, image=card_front_img)
    flip_card_timer = window.after(3000, func= flip_card)


# change card function -----------------------------------------------------------
def flip_card():
    canvas.itemconfig(word_title,text = "Answer", fill = "white")
    canvas.itemconfig(word_label,text = current_question['Answers'], fill = "white")
    canvas.itemconfig(canvas_background,image=card_back_img)



def known():
    new_df.remove(current_question)
    data = pd.DataFrame(new_df)
    data.to_csv("/Users/hectororopesa/Documents/GUI/flash-card-project-start/data/questions to learn.csv", index=False)
    gen_word_french()


# window ----------------------------------------------------------------
window = Tk()
window.title("FlashCard App")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

flip_card_timer = window.after(3000, func= flip_card)

# canvas ----------------------------------------------------------------
canvas = Canvas(width=800,height=526)
card_front_img = PhotoImage(file="/Users/hectororopesa/Documents/GUI/flash-card-project-start/images/card_front.png")
card_back_img = PhotoImage(file="/Users/hectororopesa/Documents/GUI/flash-card-project-start/images/card_back.png")
canvas_background = canvas.create_image(400,263, image= card_front_img)
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
word_title = canvas.create_text(400,150, text="",font=("Ariel",40,"italic"))
word_label = canvas.create_text(400,263, text="",font=("Ariel",20,"bold"))
canvas.grid(column=0,row=0,columnspan=2)


# Button Images----------------------------------------------------------------
wrong_image = PhotoImage(file="/Users/hectororopesa/Documents/GUI/flash-card-project-start/images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0,command=gen_word_french)
wrong_button.grid(column=0,row=1)

right_image = PhotoImage(file="/Users/hectororopesa/Documents/GUI/flash-card-project-start/images/right.png")
right_button = Button(image=right_image, highlightthicknes =0,command=known)
right_button.grid(column=1,row=1)





gen_word_french()





window.mainloop()
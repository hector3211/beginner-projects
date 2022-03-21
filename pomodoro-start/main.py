from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
BLACK = "#222831"
GREY = "#393E46"
BLUE = "#00ADB5"
WHITE = "#EEEEEE"
FONT_NAME = "Courier"
WORK_MIN = 1 # 25
SHORT_BREAK_MIN = 2 # 5
LONG_BREAK_MIN = 20  # 20 min
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    # timer reset 00:00
    canvas.itemconfig(timer_text, text="00:00")
    # title_label "Timer"
    timer_label.config(text="Timer")
    # reset our check marks
    check_mark_label.config(text="")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps +=1
    work_time = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        count_down(long_break)
        timer_label.config(text="Break", fg=BLUE)
    elif reps % 2 == 0:
        count_down(short_break)
        timer_label.config(text="Break", fg=BLUE)
    else:
        count_down(work_time)
        timer_label.config(text="Work", fg=BLUE)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer= window.after(1000,count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_session = math.floor(reps/2)
        for i in range(work_session):
            marks += "✓"
        check_mark_label.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Break Timer")
window.config(padx=40,pady= 50,bg=WHITE)



canvas = Canvas(width=200,height=224,bg=WHITE,highlightthickness=0)
photo = PhotoImage(file="/Users/hectororopesa/Documents/GUI/pomodoro-start/tomato.png")
canvas.create_image(100,112, image= photo)
timer_text = canvas.create_text(100,130, text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)


# timer label
timer_label = Label(text="Timer",fg = BLUE,bg=WHITE,font=(FONT_NAME,24,"bold"))
timer_label.grid(column=1,row=0)

# start button
start_button = Button(text="Start",highlightthickness=0,fg=BLUE,bg=GREY,font=(FONT_NAME),command=start_timer)
start_button.grid(column=0,row=2)

# check marks
check_mark_label= Label(fg=BLUE,bg=WHITE,font=(FONT_NAME,30))
check_mark_label.grid(column=1,row=3)


# reset_button
reset_button = Button(text="Reset",highlightthickness=0,fg=BLUE,bg=WHITE,font=(FONT_NAME),command=reset_timer)
reset_button.grid(column=2,row=2)


window.mainloop()
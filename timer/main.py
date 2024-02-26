
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
num = ""
time = None
# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(time)
    global reps
    global num
    reps = 0
    num = ""
    label["text"]="Timer"
    canva.itemconfig(timer_text,text="00:00")
    check["text"] = num
# ---------------------------- TIMER MECHANISM ------------------------------- #
def set_timer():
    global reps
    global num
    reps +=1
    if reps%6==0:
        start_time(LONG_BREAK_MIN*60)
        label["text"]="break"
        label["fg"]=RED
        num = num[::] + "✓"
        check["text"] = num
    elif reps%2 == 0:
        start_time(SHORT_BREAK_MIN*60)
        label["text"]="break"
        label["fg"]=RED
        num = num[::] + "✓"
        check["text"] = num
    else:
        start_time(WORK_MIN*60)
        label["text"]="work"
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
import math


def start_time(count):
    minutes = math.floor(count / 60)
    sec = count % 60
    if sec<10:
        sec = f"0{sec}"
    canva.itemconfig(timer_text,text=f"{minutes}:{sec}")
    if count>0:
        global time
        time = window.after(1000,start_time,count-1)
    elif count == 0:
        set_timer()




# ---------------------------- UI SETUP ------------------------------- #
from tkinter import *

window = Tk()
window.title("Timer")
window.minsize(height=150,width=250)
window.config(padx=50,pady=100,bg=YELLOW)

canva = Canvas(width=200,height=250, bg=YELLOW,highlightthickness=0)
pic = PhotoImage(file = "tomato.png")
canva.create_image(100,135,image=pic)
timer_text = canva.create_text(110,145,text="00:00",fill="white",font=(FONT_NAME,30,"bold"))
canva.grid(column=1,row=1)


label = Label(text="Timer",fg=GREEN,bg=YELLOW,font=(FONT_NAME,35,"bold"))
label.grid(column=1,row=0)

check = Label(text=num,fg=GREEN,highlightthickness=0,bg=YELLOW,font=(FONT_NAME,35,"bold"))
check.grid(column=1,row=3)


start = Button(text="START",command=set_timer)
start.grid(column=0,row=2)
reset = Button(text="RESET",command=reset_timer)
reset.grid(column=2,row=2)


window.mainloop()

from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25 
SHORT_BREAK_MIN = 5 
LONG_BREAK_MIN = 20 
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer.config(text ="Timer")
    check_mark.config(text=" ")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    
    reps+=1
    
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    
    
    #if it's the 8th rep:
    if reps % 8 == 0:
        count_down(long_break_sec)
        timer.config(text="Long Break",fg=RED ,font=(FONT_NAME, 40))
     
    #if it's 2nd/4th/6th rep:     
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer.config(text="Short Break",fg=PINK ,font=(FONT_NAME, 40))
    
    #if its 1st/3rd/5th/7th rep:
    else:
        count_down(work_sec)
        timer.config(text="Work", fg = GREEN ,font=(FONT_NAME, 40))
        mark = ""
        work_sessions = math.floor(reps/2)
        for i in range(work_sessions):
            mark += "✓"
        
   
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    
    count_min = math.floor(count/60)
    count_sec = count % 60
    
    if count_sec == 0:
        count_sec = "00"
        
    elif count_sec < 10:
        count_sec = f"0{count_sec}"
    
    canvas.itemconfig(timer_text, text = f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        window.after(1000, count_down, count - 1)
        
    else:
        start_timer()
        
            
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")#Tomato in italian
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 111, image = tomato_img)# half of the width and half of the height
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)
# count_down(5)

timer = Label()
timer.config(text="Timer", foreground=GREEN, font=(FONT_NAME, 40), bg=YELLOW)
timer.grid(column=1, row=0)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

Reset_button = Button(text="Reset", highlightthickness=0, command = reset_timer)
Reset_button.grid(column=2, row=2)

check_mark = Label()
check_mark.config(foreground=GREEN, bg=YELLOW)
check_mark.grid(column=1, row=3)


window.mainloop()
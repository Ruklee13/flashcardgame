BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import random
import pandas
import csv
shower = 0
Lang_list = pandas.read_csv("data\\french_words.csv")
words = pandas.DataFrame.to_dict(Lang_list)

# ------------------------card mechanic--------------------------#
def randomizer():
    global shower
    global words
    global Lang_list
    shower = random.randint(0,100)
    main_canv = canvas.create_image(400, 263, image = my_front)
    canvas.itemconfig(L_word, text = words["French"][shower])
    canvas.itemconfig(L_LAN, text = "French")
    canvas.tag_raise(L_LAN)
    canvas.tag_raise(L_word)
    window.after(3000, changer)  

def changer():
    global shower
    global words
    global Lang_list
    main_canv = canvas.create_image(400, 263, image = my_back)
    canvas.itemconfig(L_word ,text = words["English"][shower])
    canvas.itemconfig(L_LAN, text="English")
    canvas.tag_raise(L_LAN)
    canvas.tag_raise(L_word)

# ------------------------interface------------------------------#
def remover():
    global shower
    global words
    global Lang_list
    try:
        WH_lo = pandas.read_csv("data\\words_learned.csv")
        WH_LL = pandas.DataFrame.to_dict(WH_lo, orient="records")
        newl = { "French": [Lang_list["French"][shower]], "English": [Lang_list["English"][shower]]}
        new = pandas.DataFrame.from_dict(newl)
        lol = pandas.DataFrame.from_dict(WH_LL)
        j = lol.append(new)
        j.to_csv("data\words_learned.csv", index=False)
        randomizer()
    except FileNotFoundError:
        with open("data\\words_learned.csv", "w") as filer_l:
            newl = { "French": ["Filler"], "English": ["Filling"]}
            new = pandas.DataFrame.from_dict(newl)
            new.to_csv("data\words_learned.csv", index=False)
    
    


    




# ------------------------interface------------------------------#

window = Tk()
window.title("Flash Card")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
canvas = Canvas(height=546, width=800, highlightthickness=0, bg=BACKGROUND_COLOR)

#LABEL
#canvas
my_back = PhotoImage(file="images\\card_back.png")
my_front = PhotoImage(file="images\\card_front.png")
main_canv = canvas.create_image(400, 263, image = my_front) 
L_LAN =canvas.create_text(400,150,text="Language", font=("Arial", 40, "italic"))
L_word = canvas.create_text(400,263,text= "Word", font=("Arial", 50, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

#Button
right = PhotoImage(file="images\\right.png")
right_button = Button(height= 100, width=100, image = right, bg= BACKGROUND_COLOR, relief="flat", command=remover)
right_button.grid(column=1, row=1)

wrong = PhotoImage(file="images\\wrong.png")
wrong_button = Button(height= 100, width=100, image = wrong, bg=BACKGROUND_COLOR, relief="flat", command=randomizer)
wrong_button.grid(column=0, row=1)

window.mainloop()
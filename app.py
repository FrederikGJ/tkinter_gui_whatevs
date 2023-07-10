from tkinter import *

def submit():
    question = entry.get()
    print("DIt spørgsmål er:"+question)

def delete():
    entry.delete(0, END)

window = Tk()
window.geometry("300x100")

entry = Entry(window,
              font=("Arial", 25)
            )
entry.pack(side=TOP)

submit_button = Button(window, text="spørg", command=submit)
submit_button.pack(side=TOP)

submit_button = Button(window, text="slet", command=delete)
submit_button.pack(side=TOP)

window.mainloop()
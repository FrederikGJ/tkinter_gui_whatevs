from tkinter import *
from tkinter import font

def submit():
    question = text.get("1.0", END)  # Getting the text input
    question = question.rstrip()  # Removing trailing newlines
    output_text.set("Dit spørgsmål er: " + question + " \nSvaret er: NEJ!")  

def delete():
    text.delete("1.0", END)  # Deleting the text input

window = Tk()
window.geometry("800x600")

output_text = StringVar()  # Variable to hold output text

customFont = font.Font(family="Arial", size=20)  

text = Text(window, height=2, width=30, font=customFont)  
text.pack()

submit_button = Button(window, text="spørg", command=submit, font=customFont)
submit_button.pack(side=TOP)

delete_button = Button(window, text="slet", command=delete, font=customFont)
delete_button.pack(side=TOP)

output_label = Label(window, textvariable=output_text, font=customFont)  
output_label.pack(side=TOP)

window.mainloop()

from tkinter import simpledialog, Tk, messagebox

window = Tk()
window.withdraw()


answer = simpledialog.askstring('Title', "What is your birthday? (month and day)")

if answer == "04/30":
    messagebox.showinfo('Title', "Happy Birthday")
else:
    messagebox.showinfo('Title', "Happy Unbirthday")







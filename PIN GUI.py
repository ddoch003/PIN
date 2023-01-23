#PIN new
from tkinter import *
from tkinter import messagebox
import winsound

root=Tk()

root.config(bg="#80ff63")
root.geometry("1080x560+30+30")
root.resizable(False,False)
root.title("Python bank")

counter=0
limit=3
pin_code="1234"
balance=20000

#Functions
def delete(event):
    e.delete(0,END)

def backspace():
    e.delete(len(e.get())-1,END)

def submit(event):
    global counter
    global limit
    global pin_code
    global pin_entry
    if counter==2:
        if e.get()!=pin_code:
            messagebox.showerror(message="Card blocked! Please contact 0800 111 222")
            root.quit()
        else:correct_pin()
    elif counter<limit:
        if e.get()!=pin_code:
            incorrect_pin()
        else:
            correct_pin()
    else:
        messagebox.showerror(message="Card blocked! Please contact 0800 111 222")
        root.quit()

def quit():
    answer=messagebox.askyesno(message="Are you sure you want to quit?")
    if answer:
        messagebox.showinfo(message="Thank you for choosing Python Bank!\nGoodbye!")
        root.quit()

def incorrect_pin():
    winsound.Beep(432, 500)
    global counter
    counter = counter + 1
    messagebox.showwarning(message="Incorrect PIN! " + str(limit - counter) + " tries left.\n")
    global pin_entry
    pin_entry=""
    e.delete(0,END)

def correct_pin():
    winsound.Beep(600, 500)
    messagebox.showinfo(message="Correct PIN!")
    root.destroy()

    menu_root=Tk()
    menu_root.title("Python Bank")
    menu_root.resizable(False,False)

    global bg
    bg=PhotoImage(file="atm_background.png")

    menu_canvas = Canvas(menu_root, width=1080, height=560)
    menu_canvas.pack(fill="both", expand=True)
    menu_canvas.create_image(0, 0, image=bg, anchor="nw")

    menu_canvas.create_text(370, 100, text="Main Menu", font=("Calibry", 50, "bold"), fill="white", anchor="nw")

    global button_balance
    button_balance=Button(menu_root,font=("Helvetica", 20),text="Balance",width=20,pady=10,command=balance_function).place(x=200,y=250)
    global button_withdraw
    button_withdraw=Button(menu_root,font=("Helvetica", 20),text="Withdraw",width=20,pady=10,command=withdraw_function).place(x=550,y=250)
    global button_deposit
    button_deposit=Button(menu_root,font=("Helvetica", 20),text="Deposit",width=20,pady=10,command=deposit_function).place(x=200,y=350)
    global button_cancel
    button_cancel=Button(menu_root,font=("Helvetica", 20),text="Cancel",width=20,pady=10,command=quit).place(x=550,y=350)

def balance_function():
    global balance
    messagebox.showinfo(message=f"Your current balance is ${balance}")

def withdraw_submit(event):
    global balance
    global e
    if int(e.get())>balance:
        messagebox.showwarning(message="Exceeded withdraw limit")
        withdraw_root.destroy()
        withdraw_function()
    elif int(e.get())%10!=0:
        messagebox.showwarning(message="Please enter a sum dividable by 10")
        withdraw_root.destroy()
        withdraw_function()
    else:
        if int(e.get())>500:
            messagebox.showwarning(message="Exceeded withdraw limit")
            withdraw_root.destroy()
            withdraw_function()
        else:
            balance=balance-int(e.get())
            messagebox.showinfo(message=f"You have successfully withdrawn ${e.get()}.\nYour balance is now ${balance}.")
            withdraw_root.destroy()

def withdraw_function():
    global withdraw_root
    withdraw_root=Toplevel()
    withdraw_root.title("Python Bank")
    global bg
    withdraw_canvas=Canvas(withdraw_root,width=1080,height=560)
    withdraw_canvas.pack(fill="both",expand=True)
    withdraw_canvas.create_image(0, 0, image=bg,
                            anchor="nw")

    withdraw_canvas.create_text(540, 160, text="Enter the amount\nyou want to withdraw", font=("Calibry", 50, "bold"), fill="white", justify="center")

    withdraw_root.bind("<Return>", withdraw_submit)

    global e
    e=Entry(withdraw_root,width=6, font=("Helvetica", 40))
    e.place(x=455, y=280)
    withdraw_root.bind("<x>",delete)
    withdraw_root.bind("<X>", delete)

    button_OK = Button(withdraw_canvas, text="OK", fg="green", width=10, activeforeground="green", font=("Helvetica", 20),
                       command=withdraw_submit)
    button_OK.place(x=660, y=400)

    button_X = Button(withdraw_canvas, text="X", fg="red", width=10, activeforeground="red", font=("Helvetica", 20),
                      command=delete)
    button_X.place(x=460, y=400)

    button_back = Button(withdraw_canvas, text="<-", fg="orange", width=10, activeforeground="orange",
                         font=("Helvetica", 20), command=backspace)
    button_back.place(x=260, y=400)

def deposit_submit(event):
    global balance
    while int(e.get())%10!=0:
        messagebox.showwarning(message="Please enter a sum divisible by 10!")
        deposit_root.destroy()
        deposit_function()
    else:
        balance = balance + int(e.get())
        messagebox.showinfo(message=f"You have successfully deposited ${e.get()}.\nYour balance is now ${balance}.")
        deposit_root.destroy()

def deposit_function():
    global deposit_root
    deposit_root=Toplevel()
    deposit_root.title("Python Bank")
    global bg
    deposit_canvas=Canvas(deposit_root,width=1080,height=560)
    deposit_canvas.pack(fill="both",expand=True)
    deposit_canvas.create_image(0, 0, image=bg,
                            anchor="nw")

    deposit_canvas.create_text(540, 140, text="Enter the amount\nyou want to deposit", font=("Calibry", 50, "bold"), fill="white", justify="center")

    deposit_root.bind("<Return>",deposit_submit)

    global e
    e=Entry(deposit_canvas,width=6, font=("Helvetica", 40))
    e.place(relx=0.50, y=300,anchor=CENTER)
    deposit_root.bind("<x>", delete)
    deposit_root.bind("<X>", delete)

    button_OK = Button(deposit_canvas, text="OK", fg="green", width=10, activeforeground="green", font=("Helvetica", 20),
                       command=deposit_submit)
    button_OK.place(x=660, y=400)

    button_X = Button(deposit_canvas, text="X", fg="red", width=10, activeforeground="red", font=("Helvetica", 20),
                      command=delete)
    button_X.place(x=460, y=400)

    button_back = Button(deposit_canvas, text="<-", fg="orange", width=10, activeforeground="orange",
                         font=("Helvetica", 20), command=backspace)
    button_back.place(x=260, y=400)


#Add image
bg = PhotoImage(file="atm_background.png")

#Create canvas
PIN_canvas=Canvas(root, width=1080, height=560)
PIN_canvas.pack(fill="both", expand=True)

#Display Canvas
PIN_canvas.create_image(0, 0, image=bg,
                        anchor="nw")

#Add text to canvas:
PIN_canvas.create_text(130, 80, text="Welcome to Python Bank!\n   Please enter your PIN:", font=("Calibry", 50, "bold"), fill="white", anchor="nw")

#Add entry
pin_entry=StringVar()
e=Entry(PIN_canvas, width=4, font=("Helvetica", 40), textvariable=pin_entry)
e.place(x=475,y=280)

#Add buttons
button_OK=Button(PIN_canvas, text="OK", fg="green", width=10, activeforeground="green", font=("Helvetica", 20), command=submit)
button_OK.place(x=650,y=400)

button_X=Button(PIN_canvas, text="X", fg="red", width=10, activeforeground="red", font=("Helvetica", 20), command=delete)
button_X.place(x=450,y=400)

button_back=Button(PIN_canvas, text="<-", fg="orange", width=10, activeforeground="orange", font=("Helvetica", 20), command=backspace)
button_back.place(x=250,y=400)

winsound.Beep(600, 500)

root.bind("<Return>",submit)
root.bind("<x>",delete)
root.bind("<X>",delete)

root.mainloop()
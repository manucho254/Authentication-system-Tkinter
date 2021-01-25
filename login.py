from tkinter import *


class Login:
    def __init__(self, master):
        self.master = master
        self.master.configure(bg="#B0C4DE")
        master.geometry("400x570")
        master.resizable(width=0, height=0)
        master.title("REGISTER")
        master.img = PhotoImage(file="login2.png")
        master.label = Label(master, bg="black", height=180)
        master.label.grid(row=0, column=2)
        master.label.place(x=80, y=65)
        master.label["compound"] = LEFT
        master.label["image"] = master.img

        # main label
        master.login_label = Label(
            master, text="Registration Form", font="Helvetica, 30",
            fg="#4682B4", bg="black", width=18)
        master.login_label.place(x=0, y=0)

        # Firstname
        master.login_label2 = Label(
            master, text="Firstname", bd=5, fg="#4682B4", bg="black", width=8)
        master.login_label2.place(x=55, y=270)

        master.entry1 = Entry(
            master, bd=5, fg="black", bg="#4682B4",  width=25, font="Helvetica, 10")
        master.entry1.place(x=150, y=270)

        # Lastname
        master.login_label3 = Label(
            master, text="Lastname", bd=5, fg="#4682B4", bg="black", width=8)
        master.login_label3.place(x=55, y=310)

        master.entry2 = Entry(
            master, bd=5, fg="black", bg="#4682B4", width=25, font="Helvetica, 10")
        master.entry2.place(x=150, y=310)

        # Username
        master.login_label4 = Label(
            master, text="Username", bd=5, fg="#4682B4", bg="black", width=8)
        master.login_label4.place(x=55, y=350)

        master.entry3 = Entry(
            master, bd=5, fg="black", bg="#4682B4", width=25, font="Helvetica, 10")
        master.entry3.place(x=150, y=350)

        # Email
        master.login_label5 = Label(
            master, text="Email", bd=5, fg="#4682B4", bg="black",  width=8)
        master.login_label5.place(x=55, y=390)

        master.entry4 = Entry(
            master, bd=5, fg="black", bg="#4682B4", width=25, font="Helvetica, 10")
        master.entry4.place(x=150, y=390)

        # Password
        master.login_label6 = Label(
            master, text="Password", bd=5, fg="#4682B4", bg="black", width=8)
        master.login_label6.place(x=55, y=430)

        master.entry5 = Entry(
            master, bd=5, fg="black", bg="#4682B4", width=25, font="Helvetica, 10")
        master.entry5.place(x=150, y=430)

        # Confirm password
        master.login_label7 = Label(
            master, text="Confirm \n Password", bd=5, fg="#4682B4", bg="black", width=8)
        master.login_label7.place(x=55, y=470)

        master.entry6 = Entry(
            master, bd=5, fg="black", bg="#4682B4", width=25, font="Helvetica, 10")
        master.entry6.place(x=150, y=470)

        def open_login():

            top = Toplevel()
            top.title('SIGN IN')
            top.geometry("400x300")
            top.configure(bg="#B0C4DE")
            top.resizable(width=0, height=0)

            my_label = Label(top, text="SIGN IN", bd=10, width=21,
                             font="helvetica, 25", fg="#4682B4", bg="black")
            my_label.place(x=0, y=0)

            login_label8 = Label(
                top, text="Email", bd=5, fg="#4682B4", bg="black", width=8)
            login_label8.place(x=55, y=120)

            entry7 = Entry(
                top, bd=5, fg="black", bg="#4682B4", width=25, font="Helvetica, 10")
            entry7.place(x=150, y=120)

            login_label9 = Label(
                top, text="Password", bd=5, fg="#4682B4", bg="black", width=8)
            login_label9.place(x=55, y=170)

            entry8 = Entry(
                top, bd=5, fg="black", bg="#4682B4", width=25, font="Helvetica, 10")
            entry8.place(x=150, y=170)

            checkv = IntVar()
            check = Checkbutton(top, text="Remember password", highlightcolor="black", width=36,
                                justify=RIGHT, variable=checkv, bg="#4682B4", fg="black", onvalue=1, offvalue=0)
            check.place(x=55, y=210)

            def welcome():
    
                new = Toplevel()
                new.title("cool")
                new.geometry("1000x600")
                new.configure(bg="orange")
                new.resizable(width=0, height=0)
                label = Label(new, text="WELCOME", font="helvetica, 40")
                label.pack(side=TOP)

            def exiter():
                top.destroy()

            button = Button(
                top, text="Sign In", bd=10, fg="#4682B4", bg="black", width=10, command=lambda:[exiter(), welcome()])
            button.place(x=180, y=250)

        # Register button

        def exit():
            master.destroy()
        master.button = Button(
            master, text="Register", bd=10, fg="#4682B4", bg="black", width=10, command=lambda: [exit(), open_login()])
        master.button.place(x=230, y=520)

        # Login button
        master.button = Button(
            master, text="Login", bd=10, fg="#4682B4", bg="black", width=10, command=lambda: [exit(), open_login()])
        master.button.place(x=100, y=520)

if __name__ == "__main__":
    root = Tk()
    Logon = Login(root)
    root.mainloop()

from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip

# ---------------------------- CONSTANTS ------------------------------- #
WHITE = 'white'
BLACK = 'black'

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def gen_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
               'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
               'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_pass():
    website = website_entry.get()
    email = email_entry.get()
    user_password = password_entry.get()

    if len(website) == 0 or len(user_password) == 0:
        messagebox.showinfo(title="Error", message="Please enter all values")
    else:
        user_resp = messagebox.askokcancel(title=website, message=f"Email: {email}\nPassword: {user_password}\n\n"
                                                                  f"Click Ok to continue or Cancel to amend")

        if user_resp:
            with open('data.txt', 'a') as pass_saved:
                pass_saved.write(f"{website} | {email} | {user_password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(pady=40, padx=40)

canvas = Canvas(width=200, height=200)
photo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=photo_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username")
email_label.grid(column=0, row=2)

password_label = Label(text="Password")
password_label.grid(column=0, row=3)

gen_btn_label = Button(text="Generate Password", command=gen_password)
gen_btn_label.grid(column=2, row=3)

add_btn_label = Button(text="add", width=35, command=save_pass)
add_btn_label.grid(column=1, row=4, columnspan=2)

# ------------------ Inputs ----------------- #

website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, 'example@test.com')

password_entry = Entry(width=20)
password_entry.grid(column=1, row=3)


window.mainloop()

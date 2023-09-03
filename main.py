from tkinter import *
from tkinter import messagebox
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generatepassword():

    #Password Generator Project
    import random
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for char in range(nr_letters) ]
    password_symbols = [random.choice(symbols) for char in range(nr_symbols) ]
    password_numbers = [random.choice(numbers) for char in range(nr_numbers) ]
    password_list = password_numbers+password_letters+password_symbols
    random.shuffle(password_list)

    password ="".join(password_list)
    pyperclip.copy(password)
    print(f"Your password is: {password}")
    password_entry.insert(0,password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_name=website_entry.get()
    password_name=password_entry.get()
    email_name=email_name_entry.get()
    new_data={
        website_name : {
            "email":email_name,
            "password": password_name,
        }
    }

    if len(website_name)==0 or len(password_name)==0:
        messagebox.askokcancel(title="Oops",message="Please dont leave any field empty")
    else:
        try:
            with open("data.json","r") as data_file:
                # reading the new_data
                data=json.load(data_file)
                # updating the new_data to old data
                data.update(new_data)

            with open("data.json","w") as data_file:
                # saving the updated_data
                json.dump(data,data_file,indent=4)
                website_entry.delete(0,END)
                password_entry.delete(0,END)
        except FileNotFoundError:
            with open("data.json","w") as data_file:
                json.dump(new_data,data_file,indent=4)
#---------------------------search set_up------------------------#
def search():
    search_key = website_entry.get()
    try:
        with open("data.json","r") as data_file:
            contents = json.load(data_file)
            dictionary = contents[search_key]
            emaill = dictionary["email"]
            password = dictionary["password"]


            messagebox.askokcancel(title=f"{search_key}",message=f"email: {emaill} \npassword: {password}")
    except FileNotFoundError:
        messagebox.askokcancel(title="error",message="No Data File Found")
    except KeyError:
        messagebox.askokcancel(title="error", message="No Data File Found")








# ---------------------------- UI SETUP ------------------------------- #
#creating a Window
window = Tk()
window.title("Password Manager")
window.config(padx=65,pady=55)


# creating the canvas of image

canvas = Canvas(width=200, height=200)
canvas_img = PhotoImage(file="logo.png")
canvas.create_image(110, 110, image=canvas_img)
canvas.grid(row=0, column=1)



#  creating the labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

# website_label.config(padx=40)

email_name_label = Label(text="Email/username:")
email_name_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)


# creating the website,email/username/ password entries

website_entry = Entry(width=48)
website_entry.grid(row=1, column=1,columnspan=2 )
website_entry.focus()

email_name_entry = Entry(width=48)
email_name_entry.grid(row=2, column=1,columnspan=2)
email_name_entry.insert(0,"lokeskalli@gmail.com")

password_entry = Entry(width=48)
password_entry.grid(row=3, column=1,columnspan=2)

# generation of buttons ADD,GENERATE PASSWORD,search

generate_password_button = Button(text="Generate password",height=1,command=generatepassword)
generate_password_button.grid(row=3, column=3)
add_button = Button(text="Add", width=41,command=save)
add_button.grid(row=4, column=1, columnspan=2)
search_button = Button(text="Search",width=15,command=search)
search_button.grid(row=1, column=3)





window.mainloop()
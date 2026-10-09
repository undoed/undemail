# Imports
import hashlib
import tkinter as tk
 
# Definitions
logged_in = False
syntax_check_bool = True
you_have_mail = False
duplicate = False
email_syntax_check = None

# Tkinter functions
def email_field():
    global signup_email
    signup_email = email_entry.get()
    print(signup_email)

    wn_signup.destroy()
    
    global wn_signup_password
    wn_signup_password = tk.Tk()

    wn_signup_password.geometry("650x500")
    wn_signup_password.title("Undemail Signup")
    wn_signup_password.config(background="#ffffff")

    email_label = tk.Label(text="Please enter password:")
    email_label.place(x=257, y=150)


    global password_entry
    password_entry = tk.Entry(show="*")
    password_entry.place(x=250, y=250)

    password_entry_button = tk.Button(text="Done")
    password_entry_button.place(x=303, y=300)
    password_entry_button.config(command=password_field)

    # Checks for corrext xxx@xxx.xxx email format
    email_format_check_len = len(signup_email)
    email_format_check_at = signup_email.find("@")
    email_format_check_dot = signup_email.find(".")

    global email_syntax_check

    if email_format_check_at > 0 and email_format_check_at < email_format_check_dot and email_format_check_len > email_format_check_dot:
        email_syntax_check = True
    else:
        email_syntax_check = False

    # Checks if the account email is duplicate
    global duplicate
    with open("accounts.txt", "r", encoding="utf-8") as account:
        for line in account:
            line = line.strip()
            x = line.split("|")[0]
            if x == signup_email:
                duplicate = True

def password_field():
    global signup_password
    signup_password = password_entry.get()
    print(signup_password)

    wn_signup_password.destroy()
    logged_in_wn = tk.Tk()
    logged_in_wn.config(bg="#FFFFFF")

    account_password_hashed = hashlib.sha256(signup_password.encode('utf-8')).hexdigest()

    if duplicate:
        print("Sorry, that email is already taken.")
    elif not duplicate and email_syntax_check:
        with open("accounts.txt", "a", encoding="utf-8") as account:
            account.write(f"{signup_email}|{account_password_hashed}\n")
        print("Account created successfully! Please log in to continue.")

# Checks if user chose to login
def login():
    global logged_in_as
    global logged_in

    # Hashes the password before checking it against the hashed accounts.txt
    account_password_login_hashed = hashlib.sha256(account_password_login.encode('utf-8')).hexdigest()

    # Opens account.txt in read mode and compares hashed user password input with the hashed password found in accounts.txt
    with open("accounts.txt", "r", encoding="utf-8") as account:
        # Iterates through each line in accounts.txt to compare it to user's alleged password
        for line in account:
            line = line.strip()
            x, y = line.split("|")
            if x == account_email_login and y == account_password_login_hashed:
                print("Login successful! Welcome back!")
                logged_in = True
                logged_in_as = account_email_login
                break
            else:
                print("Password or email incorrect.")

# Checks if user chose to signup
def signup_screen():
    wn.destroy()
    global wn_signup
    wn_signup = tk.Tk()

    wn_signup.geometry("650x500")
    wn_signup.title("Undemail Signup")
    wn_signup.config(background="#ffffff")

    email_label = tk.Label(text="Please enter email:")
    email_label.place(x=268, y=150)


    global email_entry
    email_entry = tk.Entry()
    email_entry.place(x=250, y=250)

    email_entry_button = tk.Button(text="Done")
    email_entry_button.place(x=303, y=300)
    email_entry_button.config(command=email_field)

if logged_in:
    yorn = input("Would you like to send an email [1] or check inbox [2]? \n[1] [2]")
    if yorn.lower() == "1":
        receiver_email = input("Please input receiver email: ")
        email_subject = input("Please input email subject: ")
        email_body = input("Please input email contents: ")
        syntax_check = receiver_email + email_subject + email_body
        for char in syntax_check:
            if char == "|":
                syntax_check_bool = False
        if syntax_check_bool:
            with open ("mail.txt", "a", encoding="utf-8") as mail:
                mail.write(f"{logged_in_as}|{receiver_email}|{email_subject}|{email_body}")
    elif yorn.lower() == "2":
        with open("mail.txt", "r", encoding="utf-8") as mail:
            for line in mail:
                line = line.strip()
                sender, receiver, subject, body = line.split("|")
                if receiver == logged_in_as:
                    you_have_mail = True
                else:
                    you_have_mail = False
        if you_have_mail:
            print(f"FROM: {sender} \nTO: {receiver} \nSUBJECT: {subject} \nCONTENT: {body}")
        
        elif not you_have_mail:
            print("You have no mail.")

# Tkinter
wn = tk.Tk()

wn.geometry("650x500")
wn.title("Undemail")
wn.config(background="#ffffff")

welcome_text = tk.Label(wn, text="Welcome to undemail!", font=("Arial", 20, "bold"))
welcome_text.place(x=180, y=50)

login_button = tk.Button(text="Login")
login_button.config(command=login)
login_button.place(x=370, y=350)

signup_button = tk.Button(text="Signup")
signup_button.config(command=signup_screen)
signup_button.place(x=200, y=350)

wn.mainloop()
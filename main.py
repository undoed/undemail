# Imports
import tkinter
import hashlib

# Definitions
logged_in = False
syntax_check_bool = True
you_have_mail = False
duplicate = False

# Tkinter
#wn = tkinter.Tk()

#wn.geometry("500x500")
#wn.title("Undemail")
#wn.config(background="#ffffff")

#wn.mainloop()

prompt = input("Welcome to undemail! Would you like to log in [1], or sign up [2] ? \n[1] [2]: ")

if prompt == "1":
    account_email_login = input("Please enter account email: ")
    account_password_login = input("Please enter the corresponding account password: ")
    account_password_login_hashed = hashlib.sha256(account_password_login.encode('utf-8')).hexdigest()
    with open("accounts.txt", "r", encoding="utf-8") as account:
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

if prompt == "2":
    account_email = input("Please enter account email: ")
    account_password = input("Please enter the corresponding account password: ")
    account_password_hashed = hashlib.sha256(account_password.encode('utf-8')).hexdigest()
    syntax_check_signup = account_email + account_password
    with open("accounts.txt", "r", encoding="utf-8") as account:
        for line in account:
            line = line.strip()
            x, y = line.split("|")
            if x == account_email_login:
                duplicate = True
    if duplicate:
        print("Sorry, that email is already taken.")
    elif not duplicate:
        with open("accounts.txt", "a", encoding="utf-8") as account:
            account.write(f"{account_email}|{account_password_hashed}\n")
        print("Account created successfully! Please log in to continue.")

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
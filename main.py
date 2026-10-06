# Definitions
logged_in = False
syntax_check_bool = True

prompt = input("Welcome to undemail! Would you like to log in [1], or sign up [2] ? \n[1] [2]: ")

if prompt == "1":
    account_email_login = input("Please enter account email: ")
    account_password_login = input("Please enter the corresponding account password: ")

    with open("accounts.txt", "r", encoding="utf-8") as account:
        for line in account:
            line = line.strip()
            x, y = line.split(":")
            if x == account_email_login and y == account_password_login:
                print("Login successful! Welcome back!")
                logged_in = True
                logged_in_as = account_email_login
                break

elif prompt == "2":
    account_email = input("Please enter account email: ")
    account_password = input("Please enter the corresponding account password: ")
    syntax_check_signup = account_email + account_password
    # checks
    for char in syntax_check:
            if char == ":":
                syntax_check_bool = False
    if syntax_check_bool:
        with open("accounts.txt", "a", encoding="utf-8") as account:
            account.write(f"{account_email}:{account_password}\n")
    print("Account created successfully! Please log in to continue.")

if logged_in:
    yorn = input("Would you like to send an email [1] or check inbox [2]? \n[1] [2]")
    if yorn.lower() == "1":
        receiver_email = input("Please input receiver email: ")
        email_subject = input("Please input email subject: ")
        email_body = input("Please input email contents: ")
        syntax_check = receiver_email + email_subject + email_body
        for char in syntax_check:
            if char == ";":
                syntax_check_bool = False
        if syntax_check_bool:
            with open ("mail.txt", "a", encoding="utf-8") as mail:
                mail.write(f"{logged_in_as};{receiver_email};{email_subject};{email_body}")
    elif yorn.lower() == "2":
        with open("mail.txt", "r", encoding="utf-8") as mail:
            for line in mail:
                line = line.strip()
                sender, receiver, subject, body = line.split(";")
                if receiver == logged_in_as:
                    print(f"FROM: {sender} \nTO: {receiver} \nSUBJECT: {subject} \nCONTENT: {body}")
                else:
                    print("You have no mail.")
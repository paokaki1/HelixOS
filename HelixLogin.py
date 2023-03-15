login_pass = open('password.txt')
login_name = open('username.txt')
l_p = login_pass.read()
l_n = login_name.read()

while True:
    login = input(str("Please enter your password "  + l_n + ": "))
    if login == l_p:
        print("You did it! Welcome to the home!")
        import os
        os.startfile('HelixDesktop.py')
        break
    else:
        print("Wrong Password. Oops")

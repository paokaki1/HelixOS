print("Welcome to the setup! My name is Helis! Guardian of HelixOS! Ill help you set up!")
name = input(str("Please enter your display name:"))
pas = input(str("Please enter your password to log in:"))

with open ('username.txt','w') as f:
    f.writelines(name)

with open('password.txt','w') as f:
    f.writelines(pas)

    print("You completed the setup! Congratulations, reverting back to previous page!")

    os.startfile('HelixHome.py')
    import os
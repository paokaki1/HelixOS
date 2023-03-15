print("HelixOS")
print("Welcome to your new computer, that runs the new HelixOS")
print("Here are options..")
print("""
[1] Start Setup
[2] Setup completed!""")

select = input('[?]: ')

if select == '1':
    print("Starting the setup..")
    import os

    os.startfile('HelixSetup.py')

if select == '2':
    print("Starting Login..")
     
    import os 
    os.startfile('HelixLogin.py')

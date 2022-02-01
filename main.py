menu = ""
while menu != "1" or menu != "2":
    menu = input("Would you like to save a new password or view your old ones"
                 "\n1. Input Password"
                 "\n2. View Password"
                 "\n3. Exit")
    if menu == '1':
        softwareName = input("Enter the name of the software you are using")
        userName = input("Enter your username for the software")
        passWord = input("Enter your password for the software")

    if menu == '2':
        print("Display Passwords")

    if menu == '3':
        exit(1)



def validate_pass():
    while True:
        password= input("Please enter a password: ")
        if len(password) < 15:
            print("Unacceptable password. Please make sure your password has at least 15 letters or more.")

validate_pass()
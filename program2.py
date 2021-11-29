def validate_pass():
    count, upper, digit, special= 0, 0, 0, 0
    password= input("Please enter a password here: ")
    for word in password:
            if word.isalpha():
                count += 1
            if word.isupper():
                upper += 1
            if word.isdigit():
                digit += 1
    for i in password:        
            if i == '~' or i == '`' or i == '!' or i == '@' or i == '#' or i == '$' or i == '%' or i == '^' or i == '&' or i == '*' or i == '(' or i == ')' or i == '_' or i == '–' or i == '+' or i == '=' or i == '{' or i == '[' or i == '}' or i == ']' or i == '|' or i == '/' or i == ':' or i == ';' or i == '“' or i == '‘' or i == '<' or i == ',' or i == '>' or i == '.' or i == '?':
                special += 1
    #conditions
    else:
        while True:
            if count >15 and upper >= 1 and digit >= 1 and special >= 1:
                print("Valid Password")
                break
            if upper == 0:
                print("Invalid. Your password should include at least one uppercase letter.")
                validate_pass()
            if digit == 0:
                print("Invalid. Your password should include a number in it.")
                validate_pass()
            if special == 0:
                print("Invalid. Your password should include at least one special character.")
                validate_pass()
            if count < 15:
                print("Invalid. Your password should at least include 15 characters.")
                validate_pass()
            break
            
validate_pass()
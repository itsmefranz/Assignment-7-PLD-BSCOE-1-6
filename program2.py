def validate_pass():
    upper, digit, special= 0, 0, 0
    password= input("Please enter a password here: ")
    for i in password:
        for word in password.split():
            if word.any([x.isupper() for x in password]):
                upper += 1
            if word.any([x.isdigit() for x in password]):
                digit += 1
            if i == '~' or i == '`' or i == '!' or i == '@' or i == '#' or i == '$' or i == '%' or i == '^' or i == '&' or i == '*' or i == '(' or i == ')' or i == '_' or i == '–' or i == '+' or i == '=' or i == '{' or i == '[' or i == '}' or i == ']' or i == '|' or i == '/' or i == ':' or i == ';' or i == '“' or i == '‘' or i == '<' or i == ',' or i == '>' or i == '.' or i == '?':
                special += 1
    else:
       if upper <1:
           print("Invalid. Your password should include at least one uppercase letter.")
           if digit <1:
               print("Invalid. Your password should include a number in it.")
               if special < 1:
                   print("Invalid. Your password should include at least one special character.")
                   if len(password) < 15:
                       print("Invalid. Your password should at least include 15 characters.")
    if (upper >= 1 and digit >= 1 and special >= 1):
        print("Valid Password")

validate_pass()
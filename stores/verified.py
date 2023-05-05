email = "['test1', 'test2']"
email_params = list()
if email is not None:
    if '[' in email and ']' in email:
        email = email.replace('[', '').replace(']', '')
        for param in email.split(','):
            email_params.append(str(param.capitalize()))
        print("Non liste")
    else:
        print("Est list")

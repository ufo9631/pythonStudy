def account_login():
    password=input('Password:')
    if password=='12345':
        print('Login success!')
    else:
        print('Wrong password or invalid input!')
        account_login()
#account_login()     #调用

password_list=['*#*#','12345']
def account_login1():
    password=input('Password:')
    password_correct=password==password_list[-1]
    password_reset=password==password_list[0]
    if password_correct:
        print('Login success!')
    elif password_reset:
        new_password=input('Enter a new password:')
        password_list.append(new_password)
        print('Your password has changed successfully!')
        account_login1()
    else:
        print('Wrong password or invalid input!')
        account_login1()
account_login1()        
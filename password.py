# Password manager(write now just a prototype)
# ***TO DO
# ******** 1)Add a file to store data maybe jscon or xml or cvs to store passwords
#*** 2)use encryption to make it secure
#*** 3) decryption on copying
#*** 4) use some easy algo
#***%5) sone changes


#dictonary to be replace by file
PASSWORD = dict(gmail='abcd1234',facebook='abcd1234',digilocker='abcd1234',github='abcd1234')


import sys, pyperclip

#checking if command line argument is supplied or not
if len(sys.argv) < 2:
    print('Usage python password.py [account] -- copy account password')
    sys.exit()

#inputing account name
account = sys.argv[1]

#checking whther account exists or not
if account in PASSWORD:
    pyperclip.copy(PASSWORD[account])
    print(f'Password of {account} copied to clipboard')
#adding on demand of user password to given account name
else:
    print('there is no account named {account}')
    print(f'want to add password to this account:(y/n) ')
    reply = input()
    if reply == 'n':
        sys.exit()
    for i in range(3):
        password = input(f'enter password to {account}: ')
        re_password = input(f'reenter password to {account}: ')
        if password != re_password:
            print(f'this is your {i+1}th attempt(max 3 allowed ... )')
            if i != 2:
                print('passwords donot match try again')
            if(i == 2):
                print('Good Bye...')
                sys.exit()
        else:
            break
    PASSWORD[account] = password
    print(f'password to {account} added succesfully')
    print(f'want to copy password of this account to clipboard:(y/n) ')
    reply = input()
    if reply == 'n':
        del password
        sys.exit()
    pyperclip.copy(password)
    print(f'copied succesfully')
    del password





# Password manager(write now just a prototype)
# ***TO DO
# ******** 1)Add a file to store data maybe jscon or xml or cvs to store passwords-->//done
#*** 2)use encryption to make it secure//done
#*** 3) decryption on copying//done
#*** 4) use some easy algo//done

import sys, pyperclip,csv
from crypt import Cryption

#checking if command line argument is supplied or not
if len(sys.argv) < 4:
    print('Usage python password.py [firstname] [account] [key] -- copy account password for a user')
    sys.exit()

#inputing account name && firstname
firstname = sys.argv[1]
account = sys.argv[2]
key = int(sys.argv[3])
a = Cryption()

#opening file
with open('password.csv') as mypass:
    pass_reader = csv.DictReader(mypass)

    for mypassword in pass_reader:
        if(mypassword['account'].lower()==account.lower()) and (mypassword['firstname'].lower()==firstname.lower()):
            #pyperclip.copy(mypassword['password'])
            pyperclip.copy(a.decrytion(mypassword['password'],key))
            print('password copied to clipboard')
            sys.exit()

print(f"could not find password for {firstname}'s {account} account")

reply = input("want to add your password(y/n):  ")
if(reply=='y'):
    firstname = input('enter your first name:\t')
    account = input('enter your account name: \t')
    password = input('enter your password: \t')

    password = a.encryption(password,key)
else:
    sys.exit()
with open(r'password.csv','a',newline='\n') as mypasswrite:
    fieldnames = ['firstname','account','password']
    writer = csv.DictWriter(mypasswrite,fieldnames=fieldnames)

    writer.writerow({'firstname':firstname,'account':account,'password':password})
    print('added succesfully')
    sys.exit()







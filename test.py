import csv,sys
from crypt import Cryption

account_name = 'gmail'
user_name = 'Rahul'
key = 3
a = Cryption()

with open('password.csv') as mypass:
    csv_reader = csv.DictReader(mypass)

    for line in csv_reader:
        if (account_name.lower() == line['account'].lower()) and (user_name.lower() == line['firstname'].lower()):
            print(f'password of {line["account"]} owned by {line["firstname"]}:{a.decrytion(line["password"],key)}')
            sys.exit()

with open(r'password.csv','a',newline='\n') as mypasswrite:
    fieldnames = ['firstname','account','password']
    writer = csv.DictWriter(mypasswrite,fieldnames=fieldnames)
    
    writer.writerow({'firstname':'Rahul','account':'gmail','password':a.encryption('rahmailg',key)})


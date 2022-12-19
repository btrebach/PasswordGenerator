
import string
import random

#get password length
length = int(input("Enter desired password length: "))

print('''Choose character set for password from these :
        1. Letters
        2. Numbers
        3. Special Characters
        4. Exit''')

characterList = ""

#get character set for password
while(True):
    choice = int(input("Select an option "))
    if(choice == 1):
        #add letters to the characterList
        characterList += string.ascii_letters
    elif(choice == 2):
        #add numbers to the characterList
        characterList += string.digits
    elif(choice == 3):
        #add special chararacters to the characterList
        characterList += string.punctuation
    elif(choice == 4):
        #end when 4 is selected
        break
    else:
        #error handling for any selection other than 1-4
        print("Please select a valid option")

password = []

for i in range(length):
    #pick random character from characterList
    randomchar = random.choice(characterList)
    #append randomchar to password
    password.append(randomchar)

#print the newly generated password
print("Your randomly generated password is " + "".join(password))
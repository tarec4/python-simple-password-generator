#-*- coding: utf-8 -*-
import random
import string

letters = string.ascii_letters
special_chars = string.punctuation
numbers = string.digits

ls = letters + special_chars + numbers
lsn = letters + numbers + special_chars

running = True

def createpassword():
    global lsn,lenps
    ps = str()
    for i in range(lenps):
        ps += random.choice(lsn)
    password = ps
    print(password)

while running == True:
    print("Welcome to the password generator. Please specify the length of your password as a number. To disable special characters, add a '-' to the end of the number. For example, 4-.")
    lenps = input("-")
    if "-" in lenps:
        lenps = int(lenps.replace("-",""))
        lsn = ls.replace(special_chars,"")
    else:
        lenps = int(lenps)
    if lenps >= 4:
        createpassword()
    else:
        print("Password length cannot be less than 4")
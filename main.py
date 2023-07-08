import random
import subprocess
import sys
import tkinter as tk
print('Welcome To Your Password Generator')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*().,?0123456789'

while True:
    # number of passwords we will generate for the user
    while True:
        number = input('Amount of passwords to generate: ')
        try:
            number = int(number)
        except:
            print('please only input a number > 0')
            continue
        if number < 1:
            print('Minimum passwords is 1: ')
            continue
        break

    while True:
        length = input('Input your password length: ')
        try:
            length = int(length)
        except:
            print("length must be an integer > 6")
            continue
        if length < 6:
            print("minimum 6 characters")
            continue
        break

    print('\nhere are your passwords: ')
    f = open("generated_passwords.txt", "w+")
    for pwd in range(number):
        passwords = ''
        for c in range(length):
            passwords += random.choice(chars)
        f.write(f"{passwords}\n")
    f.close()
    opener = "open" if sys.platform == "darwin" else "xdg-open"
    subprocess.call([opener, "generated_passwords.txt"])
    reset = input("\nGenerate more passwords? y/n: ")
    reset.lower()
    if reset == 'y' or reset == 'yes':
        continue
    else:
        break

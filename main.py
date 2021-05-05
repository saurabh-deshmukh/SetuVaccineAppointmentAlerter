# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import time
import setu
import os


def screen_clear():
    # for mac and linux(here, os.name is 'posix')
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        # for windows platfrom
        _ = os.system('cls')


def main():
    invalidpins = True
    print("Enter no more than 10 Pincodes")
    while invalidpins:
        pincode = str(input("Enter Pincodes (Comma separated, no space eg: 400001,400002\n:"))
        pins = pincode.split(",")
        if len(pins) > 10:
            print("You have entered more than 10 Pincodes.\nTry again.")
        else:
            invalidpins = False


    age = 18
    in_age = str(input("Age group (18/45): "))
    if in_age == '45':
        age = 45


    verbos = input("Print everything? Y/N (Default is No): ")
    if (verbos == "Y") or (verbos == "y") or (verbos == "Yes") or (verbos == "yes"):
        v = True
    else:
        v = False


    while True:
        screen_clear()
        print(f'Searching locations: {pins}\nFor age group {age}+')
        setu.setu(pins, v, False, age)
        print(f'\n\tSearching again in 30 secs.\n\tClose the window to stop searching.'
              f'\n\tClose and Re-run to program to change the \'Pincodes\' and \'Age\' parameters'
              f'\n\tIf you getting error "Error 400: Bad Request", check the entered pincode.')
        time.sleep(30)
        screen_clear()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

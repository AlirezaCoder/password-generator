from random import randint
import string

passwords_count = 10
passwords = []
length = 0
letters = list(string.ascii_lowercase)
numbers = range(0, 9)
special_chars = list(string.punctuation)


def check_input(_input):
    if not _input:
        print("please enter a valid number")
        return False
    elif not _input.isnumeric():
        print("please enter only number")
        return False
    elif not 10 <= int(_input) <= 20:
        print("please enter a number between 10 and 20")
        return False
    return True


def generate_password():
    password = ""
    for _ in range(length):
        selector = randint(1, 3)
        if selector == 1:
            password += str(letters[randint(0, len(letters)-1)])
        elif selector == 2:
            password += str(numbers[randint(0, len(numbers) - 1)])
        else:
            password += str(special_chars[randint(0, len(special_chars) - 1)])
    return password


while True:
    print("please enter password length between 10 and 20. enter exit to close password generator")
    user_input = input()
    if user_input.lower() == "exit":
        exit()
    if not check_input(user_input):
        continue
    length = int(user_input)
    for i in range(passwords_count):
        print("PASS" + str(i+1) + ": " + generate_password())





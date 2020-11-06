from tkinter import Tk
from tkinter import messagebox
from tkinter import simpledialog
# imorting module Tkinter to use GUI


def ask_user():
    ask = simpledialog.askstring("Task", "Do you want to encrypt or decrypt?")
    return ask
# this line ask the user to choose to enc. or decr.


def user_message():
    message = simpledialog.askstring("Message", "Enter the message: ")
    return message
# this function asks user to type the message then it saves as a varible

root = Tk()
root.withdraw()
# the command to start Tkinter module


def even(number):
    return number % 2 == 0
# this function will check if there is even number of characters


def get_even_letters(message):
    even_letters = []  # make an empty list to store even letters.
    for counter in range(0, len(message)):
        if even(counter):
            even_letters.append(message[counter])
    return even_letters


def get_odd_letters(message):
    odd_letters = []
    for counter in range(0, len(message)):
        if not even(counter):
            odd_letters.append(message[counter])
    return odd_letters


def swap_letters(message):
    letter_sum = []
    if not even(len(message)):
        message = message + 'z'
    even_letters = get_even_letters(message)
    odd_letters = get_odd_letters(message)
    for counter in range(0, int(len(message)/2)):
        letter_sum.append(odd_letters[counter])
        letter_sum.append(even_letters[counter])
    new_message = "".join(letter_sum)
    return new_message


while True:
    ask = ask_user()  # what user wants
    if ask == "encrypt":
        message = user_message()  # get the msg. to enc.
        encrypted = swap_letters(message)
        messagebox.showinfo("Ciphertext of the message is: ", encrypted)
    elif ask == "decrypt":
        message = user_message()  # get the msg. to decr.
        decrypted = swap_letters(message)
        messagebox.showinfo("Real text of the message is:", decrypted)
    else:
        break
root.mainloop()  # keep Tkinter working


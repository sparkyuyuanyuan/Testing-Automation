

# Imports
import tkinter
from tkinter import ttk
import requests
import os
import string
import json
# import pyautogui
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
import time


# print(pyautogui.size())

# window settings
window = tkinter.Tk()
window.configure(background='black')
window.title('Form-Filler')
window.geometry('400x330')
window.resizable(0, 0)

# Create info frame
parentFrame = tkinter.Frame(width=220, height=330,
                            borderwidth=2, relief='groove')
parentFrame.grid(row=0, column=0, rowspan=2)
parentFrame.grid_rowconfigure((0, 11), weight=0)
parentFrame.grid_columnconfigure((0), weight=1)
parentFrame.grid_propagate(0)
# window.grid_rowconfigure(0, weight=1)
# window.grid_columnconfigure(0, weight=1)
dropdownFont = ('tahoma', 8)

# Create entry frame
secondFrame = tkinter.Frame(width=180, height=270,
                            borderwidth=2, relief='groove')
secondFrame.grid(row=0, column=1)
secondFrame.grid_propagate(0)
secondFrame.grid_columnconfigure((0, 1), weight=1)

# Create run button frame
runFrame = tkinter.Frame(
    width=180, height=60, borderwidth=2, relief='groove')
runFrame.grid(row=1, column=1)
runFrame.grid_propagate(0)
runFrame.grid_columnconfigure((0, 1), weight=1)

# web fields variables
# TODO: Open Sharklasers.com, get field with email, assign variable to userEmail, then proceed
# TODO: Come back to this and make checkbox for user defined or autofill for fields
# By default, autofill, checkbox ungreys input for password, name, lastname
userEmail = tkinter.StringVar()
userEmail.set('')
userPassword = 'Password1!'
# Could make these user defined but no need atm.
# userPassword = tkinter.StringVar()
# userPassword.set('')
# Same with the names
fName = 'TestUser'
lName = 'UserLast'

# tkinter functions


# Defining and locating elements
def loginFunction():
    # Import global for input
    userEmailValue = userEmail.get()

    print("Running Main Function...")

    time.sleep(3)

    info4 = tkinter.Label(parentFrame, text="Main Function Success!")
    info4.grid(row=3, pady=3)
    driver.find_element_by_name("email").send_keys(userEmailValue)
    driver.find_element_by_name("pw").send_keys(userPassword)
    driver.find_element_by_name("pwConf").send_keys(userPassword)
    driver.find_element_by_name("firstName").send_keys(fName)
    driver.find_element_by_name("lastName").send_keys(lName)
    driver.find_element_by_name("lastName").send_keys(Keys.RETURN)
    # driver.find_element_by_class_name(MuiButtonBase-root).click()
    # driver.find_element_by_class_name(MuiButtonBase-root).submit()
    time.sleep(2)
    print("Fields Entered, Checking For Confirmation...")
    info5 = tkinter.Label(parentFrame, text="Text Fields Entered \u2713")
    info5.grid(row=4, pady=3)
    assert "check your email to confirm" in driver.page_source
    info6 = tkinter.Label(
        parentFrame, text="On Email Confirmation Page \u2713")
    info6.grid(row=5, pady=3)
    # Clear the cache after submission
    time.sleep(1)
    print("Removing Cookies...")
    # info7 = tkinter.Label(parentFrame, text="Removing Cookies...")
    # info7.grid(row=6, pady=3)
    driver.delete_all_cookies()
    time.sleep(2)
    info8 = tkinter.Label(parentFrame, text="Cookies Deleted \u2713")
    info8.grid(row=7, pady=3)
    time.sleep(1)
    info9 = tkinter.Label(parentFrame, text="Completed!")
    info9.grid(row=8, pady=3)
    print("Cookies Deleted")
    print("Completed!")


# Initial val and disabled state for email/password/names
emailLabel = tkinter.Label(secondFrame, text='Email', state='disabled')
emailLabel.grid(row=1, pady=3)
emailEntry = tkinter.Entry(
    secondFrame, textvariable=userEmail, state='normal')
emailEntry.grid(row=2, pady=3)
passLabel = tkinter.Label(secondFrame, text='Password', state='disabled')
passLabel.grid(row=3, pady=3)
passEntry = tkinter.Entry(
    secondFrame, textvariable=userPassword, state='disabled')
passEntry.grid(row=4, pady=3)
fNameLabel = tkinter.Label(secondFrame, text='First Name', state='disabled')
fNameLabel.grid(row=5, pady=3)
fNameEntry = tkinter.Entry(
    secondFrame, textvariable=fName, state='disabled')
fNameEntry.grid(row=6, pady=3)
lNameLabel = tkinter.Label(secondFrame, text='Last Name', state='disabled')
lNameLabel.grid(row=7, pady=3)
lNameEntry = tkinter.Entry(
    secondFrame, textvariable=lName, state='disabled')
lNameEntry.grid(row=8, pady=3)


def enableEntry():
    print('entry enabled')
    global userEmail, userPassword, fName, lName, emailLabel, emailEntry, passEntry, passLabel, fNameEntry, fNameLabel, lNameEntry, lNameLabel
    if (chkVal.get() == 0):
        print(chkVal.get())
        emailLabel = tkinter.Label(secondFrame, text="Email", state='normal')
        emailEntry = tkinter.Entry(
            secondFrame, textvariable=userEmail, state='normal')
        passLabel = tkinter.Label(secondFrame, text="Password", state='normal')
        passEntry = tkinter.Entry(
            secondFrame, textvariable=userPassword, state='normal')
        fNameLabel = tkinter.Label(
            secondFrame, text='First Name', state='normal')
        fNameEntry = tkinter.Entry(
            secondFrame, textvariable=fName, state='normal')
        lNameLabel = tkinter.Label(
            secondFrame, text='Last Name', state='normal')
        lNameEntry = tkinter.Entry(
            secondFrame, textvariable=lName, state='normal')
    if (chkVal.get() == 1):
        print(chkVal.get())
        emailLabel = tkinter.Label(
            secondFrame, text='Email TEST', state='disabled')
        emailEntry = tkinter.Entry(
            secondFrame, textvariable=userEmail, state='disabled')
        passLabel = tkinter.Label(
            secondFrame, text='Password', state='disabled')
        passEntry = tkinter.Entry(
            secondFrame, textvariable=userPassword, state='disabled')
        fNameLabel = tkinter.Label(
            secondFrame, text='First Name', state='disabled')
        fNameEntry = tkinter.Entry(
            secondFrame, textvariable=fName, state='disabled')
        lNameLabel = tkinter.Label(
            secondFrame, text='Last Name', state='disabled')
        lNameEntry = tkinter.Entry(
            secondFrame, textvariable=lName, state='disabled')


# Checkbutton allowing editing of Email/pass/name fields.
chkVal = tkinter.IntVar()
tkinter.Checkbutton(secondFrame, text='User Set Value', command=enableEntry,
                    variable=chkVal, onvalue=0, offvalue=1, pady=5).grid(row=0, columnspan=2)

# Main Button
runBtn = tkinter.Button(runFrame, text='Test Login', command=loginFunction)
runBtn.grid(row=0, columnspan=2, pady=3)

# Browser instance, navigation and check for correct page Title
# infoBox.set('Opening Window...')
driver = webdriver.Chrome()
driver.get("https://subscribe2.buffalonews.com/register")
# infoBox.set('Checking Correct Page...')
time.sleep(2)
pageTitle = driver.title
print(pageTitle)
info1 = tkinter.Label(parentFrame, text="Checking Correct Page...")
info1.grid(row=0, pady=3)
assert "Subscribe to The Buffalo News" in driver.title
print('Correct Page!')
info2 = tkinter.Label(parentFrame, text="On BN Subscribe!")
info2.grid(row=1, pady=3)
time.sleep(1)
info3 = tkinter.Label(parentFrame, text="Waiting For User...")
info3.grid(row=2, pady=3)


print('Standby For User Input...')

window.mainloop()

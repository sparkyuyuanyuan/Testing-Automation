

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
window.geometry('400x230')
window.resizable(0, 0)

# Create parent frame
parentFrame = tkinter.Frame(width=220, height=230,
                            borderwidth=2, relief='groove')
parentFrame.grid(row=0, column=0, rowspan=2)
parentFrame.grid_rowconfigure((0, 11), weight=1)
parentFrame.grid_columnconfigure((0, 1), weight=1)
parentFrame.grid_propagate(0)
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
dropdownFont = ('tahoma', 8)

# Create walkthrough frame
secondFrame = tkinter.Frame(width=180, height=170,
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
userEmail = ""
userPassword = "Ab111111"
fName = "TestUser"
lName = "UserLast"

# tkinter functions

# Browser instance, navigation and check for correct page Title
# infoBox.set('Opening Window...')
driver = webdriver.Chrome()
driver.get("https://subscribe2.buffalonews.com/register")
# infoBox.set('Checking Correct Page...')
time.sleep(2)
pageTitle = driver.title
print(pageTitle)
assert "Subscribe to The Buffalo News" in driver.title
print('Correct Page!')
print('Standby For User Input...')


# Defining and locating elements
def loginFunction():
    print("Running Main Function...")
    driver.find_element_by_name("email").send_keys(userEmail)
    driver.find_element_by_name("pw").send_keys(userPassword)
    driver.find_element_by_name("pwConf").send_keys(userPassword)
    driver.find_element_by_name("firstName").send_keys(fName)
    driver.find_element_by_name("lastName").send_keys(lName)
    driver.find_element_by_name("lastName").send_keys(Keys.RETURN)
    # driver.find_element_by_class_name(MuiButtonBase-root).click()
    # driver.find_element_by_class_name(MuiButtonBase-root).submit()
    time.sleep(2)
    print("Fields Entered, Checking For Confirmation...")
    assert "check your email to confirm" in driver.page_source
    # Clear the cache after submission
    print("Removing Cookies...")
    driver.delete_all_cookies()
    print("Cookies Deleted")
    print("Completed!")


window.mainloop()

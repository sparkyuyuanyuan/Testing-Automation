

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


# Browser instance, navigation and check for correct page Title
driver = webdriver.Chrome()
driver.get("https://subscribe2.buffalonews.com/register")
time.sleep(2)
pageTitle = driver.title
print(pageTitle)
assert "Subscribe to The Buffalo News" in driver.title
print('Correct Page')


# print(pyautogui.size())

# window settings
# window = tkinter.Tk()
# window.configure(background='black')
# window.title('Form-Filler')
# window.geometry('400x300')
# window.resizable(0, 0)

# web fields
# TODO: Open Sharklasers.com, get field with email, assign variable to userEmail, then proceed
userEmail = ""
userPassword = "Ab111111"
fName = "TestUser"
lName = "UserLast"

# tkinter functions

# Defining and locating elements


# def login(url, email, password, passconfirm, fname, lname):
driver.find_element_by_name("email").send_keys(userEmail)
driver.find_element_by_name("pw").send_keys(userPassword)
driver.find_element_by_name("pwConf").send_keys(userPassword)
driver.find_element_by_name("firstName").send_keys(fName)
driver.find_element_by_name("lastName").send_keys(lName)
driver.find_element_by_name("lastName").send_keys(Keys.RETURN)
# driver.find_element_by_class_name(MuiButtonBase-root).click()
# driver.find_element_by_class_name(MuiButtonBase-root).submit()


def get_clear_browsing_button(driver):
    return driver.find_element_by_css_selector('* /deep/ #clearBrowsingDataConfirm')


time.sleep(2)
print("Fields Entered, Checking For Confirmation...")
assert "check your email to confirm" in driver.page_source

# Clear the cache after submission
print("Removing Cookies...")
driver.delete_all_cookies()
print("Cookies Deleted")
print("Completed!")

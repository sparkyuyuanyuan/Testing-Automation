# Testing-Automation

Python & Selenium automation for the registration process while testing. 
GUI built in tkinter. 

## Overview
Run "Form-Filler.py" to start
Initializes Chrome browser to Subscribe testing page
Verifies that desired page loads & displays correctly. 
Awaits user input. 

tkinter GUI launches and allows for use of entered unique email. 
Password, First Name and Last Name all follow pre-set defaults. 
(Option to set by user coming soon)
When fields are set, click "test login" to complete form. 
Program will complete registration, then check to make sure it progressed to the confirmation page. 
Lastly, cookies are deleted from session. 
Completion message displayed. 

---

### TODO:

- Other options available to be set by user
- Auto-open SL, then Subscribe page
  - Eventually, open SL, scrape generated email, copy field, paste in Subscribe 
- Error handling for timeouts, email already in use, etc. 

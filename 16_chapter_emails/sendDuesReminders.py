#!python3 
#This program sends email reminders to members who have not paid for 
#the latest month. Details of members are in a spreadsheet. 

import os, smtplib, openpyxl

username = input("Enter your email address: ")
password = input("Enter your password: ")

wb = openpyxl.load_workbook('duesRecords.xlsx')
ws = wb.active 

# Members who have not paid. key: name, value: email. 
members = {}
latestMonth = ws.cell(row=1, column=ws.max_column).value

# Iterating through each row of excel sheet 
for row in ws.iter_rows(min_row=2):
    # If member has not paid, store their name as the key and email as value in members
    if row[ws.max_column - 1].value != 'paid':
        name = row[0].value
        email = row[1].value 
        members[name] = email 

# Logging in to personal email 
print("Logging in to your email account...")
smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
print(smtpObj.ehlo())
print(smtpObj.starttls())
print(smtpObj.login(username, password))

# Sending personalized email to each member
for name in members:
    print("Sending email to {}".format(name))
    body = 'Subject: Due Fees\nDear {}, you have forgotten to pay your fees the month of {}. Do pay ASAP.'.format(name, latestMonth)
    sendmailStatus = smtpObj.sendmail(username, members[name], body)
    if sendmailStatus != {}:
        print("There was a problem sending email to {}: {}".format(name, sendmailStatus))

print("Done!")
smtpObj.quit()
        
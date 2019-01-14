#! python3
# program that takes a list of people’s email addresses and a list of 
# chores that need to be done and randomly assigns chores to people

# emailer is a module contained in /usr/lib/python3.6 that helps to send email using my gmail account
import emailer, random, shelve

# Logging in to gmail 
smtpObj = emailer.login()

# Connecting to db 
db = shelve.open('addresses', writeback=True)
# Initial populating database 
# db['alice'] = {'email': 'alice@example.com', 'chores': []}
# db['ben'] = {'email': 'ben@example.com', 'chores': []}
# db['david'] = {'email': 'david@example.com', 'chores': []}
# db['shawn'] = {'email': 'shawn@example.com', 'chores': []}

chores = ['dishes', 'bathroom', 'vacuum', 'walk dog']

# Loop through addresses
for name in db: 
    # Choose a random chore. If chore done before, choose another one. 
    while True:
        randomChore = random.choice(chores)
        if randomChore not in db[name]['chores']:
            break 

    # Record down chore in chores list for person, & remove chore from chores list  
    db[name]['chores'].append(randomChore)
    chores.remove(randomChore)
    print("{} will do {}.".format(name, randomChore))

    # Send email to person with assigned chore 
    message = "Subject: Chore for the Week\nDear {}, you are chosen to do the chore: {}. Enjoy and work hard!".format(name, randomChore)
    emailer.sendemail(smtpObj, db[name]['email'], message)

# Closing db, logging out of gmail
db.close()    
emailer.logout(smtpObj) 

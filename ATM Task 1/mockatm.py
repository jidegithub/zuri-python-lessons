# from datetime import date
# from datetime import time
from datetime import datetime

user = input('what is your username? \n')
allowedUsers = ['jide', 'bimpe', 'jumoke']
allowedPassword = ['passwordjide', 'passwordbimpe', 'passwordjumoke']

if(user in allowedUsers):
  print('Hello %s' % user)
  password = input('enter your password? \n')
  userId = allowedUsers.index(user) 
  today = datetime.now()
  if(password == allowedPassword[userId]):
    print(f'you are now logged in {user}')
    print(f'today\'s date is: {today}')
    print('These are the available options')
    print('1. Withdrawal')
    print('2. Cash Deposit')
    print('3. Complaint')

    selectedOption = int(input('Please select an option \n') or '0')

    if(selectedOption == 1):
      amount = int(input('How much would you like to withdraw? \n'))
      print(f'processing \u20A6{amount}')
      print('take your cash')
    elif(selectedOption == 2):
      deposit = int(input('How much would you like to deposit? \n')) + 405000
      print(f'current balance: \u20A6{deposit}')
    elif(selectedOption == 3):
      complaint = input('What issue will you like to report? \n')
      print('Thank you for contacting us.')
    elif(selectedOption == 0): print('you did\'nt select an option please try again')

  else:
    print('password incorrect')
else:
  print('incorrect username, try again')


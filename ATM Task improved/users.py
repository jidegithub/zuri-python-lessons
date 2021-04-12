import json

users = '''
{
  "users":[
  {
    "id": "6935684884",
    "email": "m.lawal@gmail.com",
    "first_name": "morire",
    "last_name": "lawal",
    "password": "mlawal",
    "account_number": 1326008519
  },
  {
    "id": "8725028055",
    "email": "p.ikechukwu@gmail.com",
    "first_name": "permanent",
    "last_name": "ikechuwku",
    "password": "pikechukwu",
    "account_number": 1998001066
  },
  {
    "id": "8076679877",
    "email": "h.alaga@gmail.com",
    "first_name": "hafusat",
    "last_name": "alaga",
    "password": "halaga",
    "account_number": 2238238543
  }
  ]
}
'''

data = json.loads(users)
datalist = (data['users'])
current_user = ""

def does_account_number_exist(account_number):
  for user in datalist:
    if(account_number == user["account_number"]):
      global current_user
      current_user = user
      return True
      break
  return False
     

def authenticated_user(account_number, password):
  if(does_account_number_exist(account_number)):
    if(password == current_user["password"]):
      return current_user
    else: 
      print('password incorrect')
  else:
    return False

def create(account_number, first_name, last_name, email, password, iden):
  data = {
    "id": iden,
    "email": email,
    "first_name": first_name,
    "last_name": last_name,
    "password": password,
    "account_number": account_number
  },

  with open('users.json', 'w') as outfile:
    json.dump(data, outfile)
    return True

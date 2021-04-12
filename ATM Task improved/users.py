import json

with open('./users.json') as user_json_file:
  datalist = json.load(user_json_file)
  # datalist = (data['users'])

# print(datalist)

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
    
def append_list(data):
  datalist.append(data)
  with open('users.json', 'w') as outfile:
    json.dump(datalist, outfile)

def create(account_number, first_name, last_name, email, password, iden):
  new_data = {
    "id": iden,
    "email": email,
    "first_name": first_name,
    "last_name": last_name,
    "password": password,
    "account_number": account_number
  }
  append_list(new_data)
  return True

  

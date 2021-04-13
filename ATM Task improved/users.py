import json

with open('./users.json') as user_json_file:
  datalist = json.load(user_json_file)
  # datalist = (data['users'])

# print(datalist)

current_user = ""
current_user_index = None

def does_account_number_exist(account_number):
  for index, user in enumerate(datalist):
    if(account_number == user["account_number"]):
      global current_user
      global current_user_index

      current_user = user
      current_user_index = index 
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

def update_account_balance(amount, type):
  if(type == "deposit"):
    current_user["account_balance"] = current_user["account_balance"] + amount
    updated_current_user = current_user
  elif(type == "withdrawal"):
    current_user["account_balance"] = current_user["account_balance"] - amount
    updated_current_user = current_user
  else:
    return None

  append_list(updated_current_user)
  # print(current_user_index)

def get_account_balance():
  return current_user["account_balance"]


  

# register
# - first name, last name, password, email
# - generate user account number


# login
# - account number & password


# bank operations

# Initializing the system
import random
import json
from getpass import getpass
import users
import validation


def init():
  print("Welcome to bankPHP")

  have_account = int(input("Do you have account with us: 1 (yes) 2 (no) \n"))

  if have_account == 1:

    login()

  elif have_account == 2:

    register()

  else:
    print("You have selected invalid option")
    init()


def login():
  print("********* Login ***********")
  "\n"
  account_number_from_user = int(input("What is your account number? \n"))

  is_valid_account_number = validation.account_number_validation(account_number_from_user)

  if is_valid_account_number:
    password = getpass("What is your password \n")
    user = users.authenticated_user(account_number_from_user, password)
    if(user):
      bank_operation(user)
    else: 
      print('Invalid account or password')
      login()
  else:
    print("Account Number Invalid: check that you have up to 10 digits and only integers")
    init()


def register():
  print("****** Register *******")
  "\n"
  email = input("What is your email address? \n")
  first_name = input("What is your first name? \n")
  last_name = input("What is your last name? \n")
  password = getpass("Create a password for yourself \n")
  print('processing..')

  account_number = generation_account_number()
  iden = generation_account_number()

  is_user_created = users.create(account_number, first_name, last_name, email, password, iden)

  if is_user_created:
    print("Your Account Has been created")
    print(" == ==== ====== ===== ===")
    print("Your account number is: %d" % account_number)
    print("Make sure you keep it safe")
    print(" == ==== ====== ===== ===")
    login()
  else:
    print("Something went wrong, please try again")
    register()


def bank_operation(user):
  print(f"Welcome {user['first_name']} {user['last_name']}")

  selected_option = int(input("What would you like to do? (1) deposit (2) withdrawal (3) Balance (4) Logout (5) Exit \n"))

  if selected_option == 1:
      deposit_operation()
  elif selected_option == 2:
      withdrawal_operation()
  elif selected_option == 3:
      get_current_balance()
  elif selected_option == 4:
      logout()
  elif selected_option == 5:
      exit()
  else:

    print("Invalid option selected")
    bank_operation(user)


def withdrawal_operation():
  print("withdrawal")
  amount = int(input("how much do you want to withdraw (NGN)? \n"))
  users.update_account_balance(amount, "withdrawal")
  return get_current_balance()
  # get current balance
  # get amount to withdraw
  # check if current balance > withdraw balance
  # deduct withdrawn amount form current balance
  # display current balance


def deposit_operation():
  print("Deposit Operations")
  amount = int(input("how much do you want to deposit (NGN)? \n"))
  users.update_account_balance(amount, "deposit")
  return get_current_balance()
  # get current balance
  # get amount to deposit
  # add deposited amount to current balance
  # display current balance


def generation_account_number():
  return random.randrange(1111111111, 9999999999)

def get_current_balance():
  print("current balance: ")
  print(users.get_account_balance())

def logout():
  login()


init()
#Data200-Yang_HW1

fail_login_count = 0
success_login_count = 0
default_admin = '123'
products_dict = {
    'SamSung TV':{'Very Bad':30,'Bad':20,'Average':0,'Good':50,'Very Good':20},
    'Hitachi AC':{'Very Bad':30,'Bad':20,'Average':0,'Good':50,'Very Good':20},
}
feedback_dict = {
     1: "Very Bad", 2: "Bad", 3: "Average", 4: "Good", 5: "Very Good"
}

def admin_id_check(user_id):
    global success_login_count, fail_login_count
    is_correct = False
    if user_id == default_admin:
        success_login_count += 1
        print('Admin login successful')
        is_correct = True
    else:
        fail_login_count += 1
        print('Invalid Admin ID')
    #
    return is_correct

def product_feedback():
    print('\nUser feedback:')
    for product, feedback in products_dict.items():
          print(f'{product}: {feedback}')

def display_info():
     print(f"\nFailed Login counts:{fail_login_count}, Successful Login counts:{success_login_count}")
     product_feedback()

def add_item(item_name):
     temp = {item_name : {'Very Bad':0,'Bad':0,'Average':0,'Good':0,'Very Good':0}}
     products_dict.update(temp)
     print(f'{item_name} has been added. ')

#Screen 1: Accept the user input. 1 ( for Admin) and 2 (for customer)
first_id = int(input("Please press 1 for Admin and 2 for customer: "))

if first_id == 1:
     # screen 2
     user_id = (input("Please enter your Admin ID: "))

     is_correct = admin_id_check(user_id=user_id)

     if is_correct:
          display_info()
          input_str = input('Do you want add a new item? Yes/[No]')
          add_new =  input_str.capitalize() == 'YES' or input_str.capitalize() == 'Y'
          if add_new:
               add_item(item_name=input('Input new item name: '))
               product_feedback()

elif first_id == 2:
     # screen 4
     #print('screend 4')
     print('Please choose your items from the following list, then provide feedback: ')
     for key in products_dict.keys():
          print(key)
     item_input = input('Your choice: ')

     if item_input in products_dict:
          feedback_input = int(input('Please write your feedback, 1 = Very bad, 2 = Bad, 3 = Average, 4 = Good and 5 very good: '))
          if feedback_input in feedback_dict:
               products_dict[item_input][feedback_dict[feedback_input]] += 1
               print('Thank you for your feedback')
          else:
              print('Invalid input, please enter a whole number between 1 and 5.')
     else:
          print('Item not found')
    
else:
     print('Invalid input, please try again')
     









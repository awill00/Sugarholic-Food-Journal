intro = print ('''This is a food journal to keep track of what sugar was eatten and how much. Please be sure to write what you have eatten seperately and amount you have eaten''')
new_entry_choice = 'Y'
breakfast = []
lunch = []
dinner = []
snack = []
dessert = []
username = ''
password = ''
error_code = []

def food_entry():
    while True:
        new_entry_begin = input(f'Good afternooon {username}! Would you like to start a new entry? ')
    
        if new_entry_begin == 'y' or  new_entry_begin == 'Y':
            new_entry_choice = input('Please enter "b" for Breakfast, "l" for Lunch, "d" for Dinner. For Snacks, and Desserts enter "s". ')
        elif new_entry_begin == 'n' or new_entry_begin == 'N':
            # should probably go back to new entry choice, could also show view entries
            print('Go back to login')
            
        #  new_entry_choices for breakfast, lunch, dinner, snack, dessert
        if new_entry_choice == 'b' or  new_entry_choice == 'B':
            breakfast_entry = input('Please enter Breakfast item: ')
            breakfast.append(breakfast_entry)
            print('Breakfast is served')
            return breakfast 
            
        if new_entry_choice == 'l' or new_entry_choice == 'L':
            lunch_entry = input ('Please enter Lunch item: ')
            lunch.append(lunch_entry)
            print('Lunch is served!')
            return lunch
        elif new_entry_choice == 'd' or new_entry_choice == 'D':
            dinner_entry = input('Please enter dinner item: ')
            dinner.append(dinner_entry)
            print('Dinner is served')
            return dinner
    
        elif new_entry_choice == 's' or new_entry_choice == 'S':
            # snack or dessert entry to differentiate
            snackin = input('Please enter "1" for Snack, or "2"for Dessert: ')
            if snackin == '1':
                snack_entry = input('Please enter your snack item: ')
                snack.append(snack_entry)
                return snack
            elif snackin == '2':
                dessert_entry = input('Please enter dessert item: ')
                dessert.append(dessert_entry)
                return dessert
    # Continuation of new_entry_choices for breakfast, lunch, dinner, snack, dessert
        elif new_entry_choice == 'l' or new_entry_choice == 'L':
            print('Lunch is served!')
        elif new_entry_choice == 'd' or new_entry_choice == 'D':
            print('Dinner is served')

food_entry()

'''


ask user if they want to start a new entry
# Good afternooon {username}! Would you like to start a new entry?
- user enters Y for yes
- create new entry by displaying date/time
for each new entry display todays date and the time
ask user if they want to start with the breakfast category

# Today is July 12 2024, would you like to start with Breakfast?
-user enters Y for yes
entry will be saved under breakfast
# Please enter breakfast item and press enter(ex. bacon, egg, sausage, oatmeal):
-user enters info presses enter
# Would you like to add additonal items? Y/N
- user enters Y
# Please enter additonal breakfast item :

if not ask whether they want to start with Breakfast, Lunch, or Dinner. Also snack or dessert.


'''

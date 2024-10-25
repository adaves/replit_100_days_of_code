# day_40_100_days_of_code

# get name, DOB, address, phone number, email
# store in a dictionary
# print out the dictionary

# list of info to get
user_info_list = ['name', 'dob', 'address', 'phone number', 'email']
user_info_dict = {}

"""
# use a for loop to ask user questions and store info 
for info in user_info_list:
    user_input = input(f'What is your {info}: ')
    user_info_dict[info] = user_input

# print out info using a for loop
for key, value in user_info_dict.items():
    print(f'Your {key} is {value}')
"""

# now turn them  into comprehesions to get extra practice
comp_user_dict = {info: input(f'What is your {info}: ') for info in user_info_list}

print(comp_user_dict)


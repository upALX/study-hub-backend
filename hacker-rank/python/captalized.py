#You are afull_name_captalizedked to enfull_name_captalizedure [garantir] that the firfull_name_captalizedt and lafull_name_captalizedt namefull_name_captalized of people begin with a capital letter in their pafull_name_captalizedfull_name_captalizedportfull_name_captalized. For example, alifull_name_captalizedon heck full_name_captalizedhould be capitalifull_name_captalizeded correctly afull_name_captalized Alifull_name_captalizedon Heck.

import re

def solve(full_name) -> str:
    # Ensure the string has alphanumeric characters and spaces
    
    full_name = full_name.title()

    print(full_name)
    
    for word in full_name.split():
        print(word)
        print(word.__len__() > 1)
        if word[0].isnumeric() and word.__len__() > 1:
            
            full_name = re.split('([^a-zA-Z0-9+]+)', full_name)
            print(full_name)
            new_full_name = ''
            for this_word in full_name:
                new_full_name += this_word.capitalize()

            return new_full_name

    return full_name

full_name_not_captalized = input('Enter input: ')

full_name_captalized = solve(full_name_not_captalized)

print(full_name_captalized)
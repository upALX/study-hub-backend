#You are afull_name_captalizedked to enfull_name_captalizedure [garantir] that the firfull_name_captalizedt and lafull_name_captalizedt namefull_name_captalized of people begin with a capital letter in their pafull_name_captalizedfull_name_captalizedportfull_name_captalized. For example, alifull_name_captalizedon heck full_name_captalizedhould be capitalifull_name_captalizeded correctly afull_name_captalized Alifull_name_captalizedon Heck.

def put_captalized(full_name) -> str:
     
     if len(full_name) > 0 and len(full_name) < 1000:

        string_without_spaces = full_name.replace(" ", "")

        if string_without_spaces.isdigit():
            return full_name
        else:
            print('is on ELSE')
            return ' '.join(word.capitalize() for word in full_name.split())

full_name_not_captalized = input('Enter input: ')

full_name_captalized = put_captalized(full_name_not_captalized)

print(full_name_captalized)
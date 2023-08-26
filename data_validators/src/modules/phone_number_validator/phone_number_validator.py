import re
from typing import Optional


class PhoneNumberValidator:

    def __init__(self):
        pass
    
    def __str__(self) -> str:

        return 

    def validate_phone_number(self, phone_number: Optional[str] = None) -> bool:
        pattern_regex_phone_number = '[0-9]{2,3}[0-9]{2}[0-9]{9}'

        phone_match = re.match(pattern=pattern_regex_phone_number, string=phone_number)

        if phone_match is not None:
            return True
        else:
            return False

    def get_number_formated(self, phone_number: str) -> str:
        return self.format_number(phone_number=phone_number)

    def format_number(self, phone_number: str) -> str:
        phone_number_validated = self.validate_phone_number(phone_number=phone_number)

        print(phone_number_validated)

        if phone_number_validated is True:
            pattern_regex_phone_number = '([0-9]{2,3})([0-9]{2})([0-9]{9})'
            phone_number_founded = re.search(pattern=pattern_regex_phone_number, string=phone_number)
            print('The phone number founded is ', phone_number_founded)
            formated_phone_number = f'+{phone_number_founded.group(1)} ({phone_number_founded.group(2)}) {phone_number_founded.group(3)[0:5]}-{phone_number_founded.group(3)[5:9]}'

            print('The phone number formated is:', formated_phone_number)

            return  formated_phone_number
        else:
            raise Exception('Phone number was invalid!')
        
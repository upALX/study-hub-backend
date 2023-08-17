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

    def get_number(self) -> str:
        return self.number

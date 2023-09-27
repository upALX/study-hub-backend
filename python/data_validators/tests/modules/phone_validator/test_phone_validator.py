from modules.phone_number_validator.phone_number_validator import PhoneNumberValidator


class TestPhoneValidator:

    phone_number_validator = PhoneNumberValidator()

    def test_phone_validator_with_brazilian_number_sucess(self):

        phone_number_validated = self.phone_number_validator.validate_phone_number(phone_number='5551980115295')

        assert phone_number_validated == True

    def test_get_formated_phone_number_by_number(self): 
        phone_number_formated = self.phone_number_validator.get_number_formated(
            phone_number='5551980115295'
        )

        assert phone_number_formated == '+55 (51) 98011-5295'
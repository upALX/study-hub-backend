from src.modules.address_validator.address_validator import AddressValidator


class TestAddressValidator:

    address_validator = AddressValidator()
    location_number = '04545005'
    url = f'https://viacep.com.br/ws/{location_number}/json/'

    def test_get_information_address_by_location_number(self):
        address_information = self.address_validator.get_information_by_location_number(
            location_number=self.location_number
        )

        print(address_information)

        assert type(address_information) == type({})
        assert address_information['bairro'] == 'Vila Olímpia'
        assert address_information['logradouro'] == 'Rua das Fiandeiras'
        assert address_information['ddd'] == '11'


        

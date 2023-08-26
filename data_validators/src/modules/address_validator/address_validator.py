import requests


class AddressValidator:


    def __init__(self) -> None:
        pass

    def get_information_by_location_number(self, location_number: str) -> dict:
        is_valid_address_number = self.validate_location_number(
            location_number=location_number
        )

        if is_valid_address_number:
            information_by_location_number = requests.get(
                url=f'https://viacep.com.br/ws/{location_number}/json/'
            )

            information_by_location_number_dict = information_by_location_number.json()

            return information_by_location_number_dict
        else:
            raise Exception(f'The location number {location_number} was invalid')

    def validate_location_number(self, location_number: str) -> bool:

        if len(location_number) == 8:
            return True
        else:
            return False
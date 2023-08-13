from validate_docbr import CPF, CNPJ


class DocumentNumberValidator:

    def __init__(self, document_number: str):
        self.document_number = document_number
    
    def __str__(self) -> str:
        document_number_valid = self.choice_validation_by_document_number()
        return f'The valid document number is {document_number_valid}'
        
    def choice_validation_by_document_number(self) -> str:
        if len(self.document_number) == 11:
            print('IS INDIVIDUAL')
            document_validated = self.individual_document_number_validator()
            return document_validated
        elif len(self.document_number) == 14:
            print('IS COMPANY')
            document_validated = self.company_document_number_validator()
            return document_validated
        else:
            raise Exception(f'The document number {self.document_number} has lenght not acceptable!')
    
    def individual_document_number_validator(self) -> bool:
        cpf = CPF()
        if cpf.validate(doc=self.document_number) is False:
            return ValueError(f'The individual document number {self.document_number} has not 11 lenght.')
        else:
            return self.build_document_number_image(document_number=self.document_number, type_document='individual')
    
    def company_document_number_validator(self) -> bool:
        cnpj = CNPJ()
        if cnpj.validate(doc=self.document_number) is False:
            raise ValueError(f'The individual document number {self.document_number} has not 14 lenght.')
        else:
            return self.build_document_number_image(document_number=self.document_number, type_document='company')
        
    def build_document_number_image(self, document_number: str, type_document: str) -> str:
        if type_document.lower() == 'individual':
            return f'{document_number[0:3]}.{document_number[3:6]}.{document_number[6:9]}-{document_number[9:11]}'
        elif type_document.lower() == 'company':
            return f'{document_number[0:2]}.{document_number[2:5]}.{document_number[5:8]}/{document_number[8:12]}-{document_number[12:15]}'
        else:
            raise Exception(f'The document number {document_number} was not valid to generate a mask!')
    
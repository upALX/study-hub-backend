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
            return ValueError(f'The individual document number {self.document_number} was not on the rules to valid individual document number!')
        else:
            return cpf.mask(doc=self.document_number)
    
    def company_document_number_validator(self) -> bool:
        cnpj = CNPJ()
        if cnpj.validate(doc=self.document_number) is False:
            raise ValueError(f'The company document number {self.document_number} is not on the rules to valid company document number!')
        else:
            return cnpj.mask(doc=self.document_number)
        
from modules.documents_validator.document_number_validator import DocumentNumberValidator
from validate_docbr import CNPJ

cnpj = CNPJ()

print(cnpj.generate())

document_number = input()

document_validated = DocumentNumberValidator(document_number=document_number)

print(document_validated)

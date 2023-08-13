from modules.documents_validator.document_number_validator import DocumentNumberValidator

document_number = input()

document_validated = DocumentNumberValidator(document_number=document_number)

print(document_validated)

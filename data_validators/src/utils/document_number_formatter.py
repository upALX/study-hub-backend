class DocumentNumberFormatter:

    def build_document_number_image(self, document_number: str, type_document: str) -> str:
        if type_document.lower() == 'individual':
            return f'{document_number[0:3]}.{document_number[3:6]}.{document_number[6:9]}-{document_number[9:11]}'
        elif type_document.lower() == 'company':
            return f'{document_number[0:2]}.{document_number[2:5]}.{document_number[5:8]}/{document_number[8:12]}-{document_number[12:15]}'
        else:
            raise Exception(f'The document number {document_number} was not valid to generate a mask!')
        
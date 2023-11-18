class ExceptionsFromApi(Exception):
    def __init__(self, title, status_code, message, more_information) -> None:
        self.title = title
        self.description = message
        self.http_status = status_code
        self.more_info = more_information

class InternalError(ExceptionsFromApi):
    code = "API500"

    def __init__(self) -> None:
        title = "Internal Error"
        http_status = 500
        message = "An internal error has occurred and its being investigated"
        more_information = "open an issue and report this problem so it can be resolved and mapped"
        super().__init__(message=message, title=title, http_status=http_status, more_information=more_information)
        
class ServerRequestError(Exception):
    pass

class DocumentNotExistError(ServerRequestError):
    def __init__(self):
        message = "this post doesn't exist. Try another id"
        super().__init__(message)
    
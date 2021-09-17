class PostNotFoundError(Exception):

    def __init__(self):

        message = "this post doesn't exist. Try another id"

        super().__init__(message)


class InvalidKeyError(Exception):
    
    def __init__(self):

        message = 'Make sure you only send avaliable keys. Like: title, author, content or tags'

        super().__init__(message)


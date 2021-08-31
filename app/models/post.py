from datetime import datetime
class Post:
    def __init__(self, title: str, author: str,  content: str, tags: list,  **kwargs) -> None:
        self.id: int = 1

        self.title: str = title
        self.author: str = author
        
        self.created_at: str = datetime.utcnow().strftime("%d/%m/%Y às %H:%M")
        self.update_at: str = ''

        self.content: str = content
        self.tags: str = tags

    def update_id(self, id):
        self.id = int(id)



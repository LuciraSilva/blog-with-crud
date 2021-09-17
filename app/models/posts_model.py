from app.exceptions.posts_exceptions import InvalidKeyError, PostNotFoundError
from pymongo import MongoClient
from dotenv import load_dotenv 
from datetime import datetime
import os

load_dotenv()

client = MongoClient(os.getenv('DB_HOST'), int(os.getenv('DB_PORT')))

db = client[os.getenv('DB_NAME')]

class Post:
    def __init__(self, title: str, author: str,  content: str, tags: list,  **kwargs) -> None:
            self.id: int = 1

            self.title: str = title

            self.author: str = author
            
            self.created_at: str = datetime.utcnow().strftime("%d/%m/%Y às %H:%M")

            self.updated_at: str = ''

            self.content: str = content

            self.tags: str = tags

    def create_new_id(self):

        posts = Post.get_all()

        if posts:
            self.id = int(posts[-1]['id']) + 1        

    def save(self):

        self.create_new_id()

        db.posts.insert_one(self.__dict__)

        saved_data = Post.get_by_id(self.id)

        return saved_data

    @staticmethod
    def get_all() -> list:
        
        posts = list(db.posts.find({}, {'_id': False}))

        return posts

    @staticmethod
    def get_by_id(id: int) -> dict:

        filtered_data = db.posts.find_one({'id': id}, {'_id': False})

        if not filtered_data:
            raise PostNotFoundError

        return filtered_data

        
    @staticmethod
    def update(id: int, new_data):
        
        avaliable_keys = ['title', 'author', 'content', 'tags']

        for k in new_data.keys():
            if k not in avaliable_keys:
                raise InvalidKeyError

        db.posts.update_one({'id': id}, {'$currentDate': {'updated_at': True}, '$set': new_data})

        updated_data = Post.get_by_id(id)

        return updated_data


    def delete(id: int):

        deleted_data = db.posts.find_one_and_delete({'id': id}, {'_id': False})

        if not deleted_data:
            raise PostNotFoundError
            
        return deleted_data

    
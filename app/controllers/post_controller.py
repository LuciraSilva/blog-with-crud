from app.models.errors import DocumentNotExistError
from app.models.post import Post

from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

client = MongoClient(os.getenv('DATABASE_URL'), int(os.getenv('DATABASE_PORT')))


db = client['kenzie']


def get_posts():
    posts = list(db.posts.find())

    for post in posts:
        del post['_id']
    return posts


def get_one_post(id: int):
    posts = get_posts()

    filtered_post = [post for post in posts if post['id'] == id]

    if not filtered_post:
        raise DocumentNotExistError
    return filtered_post.pop()


def create_post(post: Post):
    posts = get_posts()

    if posts:
        post.update_id(posts[-1]['id'] + 1)

    db.posts.insert_one(post.__dict__)
    return {'message': 'post was created with success'}


def delete_post(post_id: int):
    deleted_post = db.posts.find_one_and_delete({"id": post_id})

    if not deleted_post:
        raise DocumentNotExistError

    del deleted_post['_id']
    return deleted_post


def update_post(post_id: int, data: dict):

    db.posts.find_one_and_update({"id": post_id}, 
    {"$set": data, "$currentDate": {"update_at": True }})

    post = get_one_post(post_id)
    return post.pop()
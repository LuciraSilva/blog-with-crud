from app.exceptions.posts_exceptions import InvalidKeyError, PostNotFoundError
from flask import request, jsonify
from app.models.posts_model import Post


def read_posts():

    data = Post.get_all()

    return jsonify(data), 200


def read_post_by_id(id: int):

    try:
        return Post.get_by_id(id), 200

    except PostNotFoundError as e:

        return {'message': str(e)}, 404


def create_post():

    datas = request.get_json()

    try:
        post = Post(**datas)

        created_data = post.save()

        return jsonify(created_data), 201

    except TypeError:

        return {'message': """Make sure you send all required data.\
        Like: title, author, content and tags"""}, 406


def update_post(id: int):

    data = request.get_json()
    
    try:
        updated_data = Post.update(id, data)

        return jsonify(updated_data), 200

    except PostNotFoundError as e:

        return {'message': str(e)}, 404
    
    except InvalidKeyError as e:

        return {'message': str(e)}, 422


def delete_post(id: int):
    
    try:
        return Post.delete(id), 200
        
    except PostNotFoundError as e:
        
        return {'message': str(e)}, 404

        

    
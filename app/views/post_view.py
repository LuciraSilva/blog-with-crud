from app.models.errors import DocumentNotExistError
from flask import Flask, request, jsonify
from app.models.post import Post
from app.controllers import post_controller

def post_view(app: Flask):

    @app.route('/posts', methods=['GET', 'POST'])
    def read_or_create_posts():

        if request.method == 'GET':
            return jsonify(post_controller.get_posts()), 200

        datas = request.json

        try:
            post = Post(**datas)

            return post_controller.create_post(post), 201

        except TypeError:
            return {'message': 'is missing required data'}, 406

    @app.get('/posts/<int:id>')
    def read_post_by_id(id: int):

        try:
            return post_controller.get_one_post(id), 200

        except DocumentNotExistError as e:

            return {'message': str(e)}, 404

    @app.route('/posts/<int:id>', methods=['PATCH', 'DELETE'])
    def update_or_delete_post(id: int):

        data = request.json
        
        if request.method == 'PATCH':

            try:

                return post_controller.update_post(id, data), 200

            except DocumentNotExistError as e:

                return {'message': str(e)}, 404

        try:
            return post_controller.delete_post(id), 200
            
        except DocumentNotExistError as e:
            
            return {'message': str(e)}, 404
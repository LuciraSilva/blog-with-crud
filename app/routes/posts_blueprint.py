from app.controllers.posts_controller import create_post, delete_post, read_post_by_id, read_posts, update_post
from flask import Blueprint

bp = Blueprint('bp_posts', __name__, url_prefix='/posts')

bp.post('')(create_post)

bp.get('')(read_posts)

bp.get('/<int:id>')(read_post_by_id)

bp.patch('/<int:id>')(update_post)

bp.delete('/<int:id>')(delete_post)
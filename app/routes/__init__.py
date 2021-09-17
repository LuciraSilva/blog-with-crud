from flask import Blueprint
from . import posts_blueprint

bp = Blueprint('bp_api', __name__, url_prefix='/api')

bp.register_blueprint(posts_blueprint.bp)
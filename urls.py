from flask import Blueprint

bp = Blueprint('urls', __name__)

@bp.route('/', methods=['GET'])
def index():
    return 'core-tcico', 200
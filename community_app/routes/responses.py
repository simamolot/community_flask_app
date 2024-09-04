from flask import Blueprint

response_bp = Blueprint('response', __name__, url_prefix='/responses')


@response_bp.route('/')  # url/responses/
def get_all_responses():
    return 'ALL RESPONSES'

@response_bp.route('/add', methods=['POST'])
def add_new_response():
    return 'RESPONSE ADDED'
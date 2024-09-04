from crypt import methods

from flask import Blueprint


questions_bp = Blueprint('questions', __name__, url_prefix='/questions')


@questions_bp.route('/', methods=['GET'])  # url/questions/
def get_all_questions():
    return 'ALL QUESTIONS'

@questions_bp.route('/add', methods=['POST'])
def add_new_question():
    return 'QUESTION ADDED'
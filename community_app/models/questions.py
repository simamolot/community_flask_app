from community_app import db
from datetime import datetime


class Question(db.Model):
    __tablename__ = 'questions'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(300), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


    responses = db.relationship('Response', backref='question')

    def __str__(self):
        return f'Question {self.text}'


class Statistics(db.Model):
    __tablename__ = 'statistics'
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'), primary_key=True)
    agree_count = db.Column(db.Integer, nullable=False, default=0)
    disagree_count = db.Column(db.Integer, nullable=False, default=0)

    def __str__(self):
        return (f'Statistics for question {self.question_id}, agreed  {self.agree_count}, '
                f'disagreed: {self.disagree_count}')

from flask import Flask

from app import db
app = Flask(__name__)

class EMPLOYEE(db.Model):
    ID = db.Column(db.Integer, primary_key=True)
    USRNAME = db.Column(db.String(64), unique=True, nullable=False)
    FIRSTNAME_TH = db.Column(db.String(250), unique=True, nullable=False)


    def __repr__(self):
        return f'<User {self.USRNAME}>'


class CER_REPORT(db.Model):
    ID = db.Column(db.Integer, primary_key=True)
    sYear = db.Column(db.Integer, unique=True, nullable=False)
    Sample = db.Column(db.String(2500), unique=True, nullable=False)
    Country = db.Column(db.String(2500), unique=True, nullable=False)
    Result = db.Column(db.String(2500), unique=True, nullable=False)
    # def __repr__(self):
    #     return f'<User {self.USRNAME}>'
    def to_dict(self):
        return {col.name: getattr(self, col.name) for col in self.__table__.columns}
    

    
from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from datetime import datetime
from flask_login import UserMixin

class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_secure = db.Column(db.String(255))
    password_hash = db.Column(db.String(255))
    projects = db.relationship("Projects", backref="user", lazy="dynamic")
    commenting = db.relationship("Comments", backref="commenti", lazy="dynamic")

class Role(db.Model):
       __tablename__ = 'roles'
       id = db.Column(db.Integer,primary_key = True)
       name = db.Column(db.String(255))
       users = db.relationship('User',backref = 'role',lazy="dynamic")
       
       
       def __repr__(self):
           return f'User {self.name}'

class Projects(db.Model):
    '''
    defines the table instance of our projects table
    '''
    __tablename__= 'projects'

    id = db.Column(db.Integer, primary_key=True)
    project = db.Column(db.String)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    category = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    complete = db.Column(db.Boolean)
    comments = db.relationship('Comments',backref = 'comment',lazy="dynamic")

class Comments(db.Model):
    __tablename__='comments'
    id=db.Column(db.Integer,primary_key=True)
    user_id=db.Column(db.Integer, db.ForeignKey('users.id'))
    projects_id=db.Column(db.Integer, db.ForeignKey('projects.id'))
    details=db.Column(db.Text())

    def as_dict(self):
        return {'details': self.details}    

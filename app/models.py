from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from datetime import datetime
from flask_login import UserMixin
from . import login_manager

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))
class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_hash = db.Column(db.String(255))
    projects = db.relationship("Projects", backref="user", lazy="dynamic")
    comment = db.relationship("Comments", backref="user", lazy ="dynamic")
  

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self,password):
            return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'User {self.username}'

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
    title = db.Column(db.String)
    actual_post = db.Column(db.String) 
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    category = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    photo = db.Column(db.String)

    def save_project(self):
        '''
        function to save project
        '''
        db.session.add(self)
        db.session.commit()

    @classmethod
    def clear_projects(cls):
        '''
        function that clears all the project form after submission
        '''
        Projects.all_projects.clear()

class Comments(db.Model):
    '''
    comment class that create instance of comment
    '''
    __tablename__ = 'comment'

    #add columns
    id = db.Column(db. Integer, primary_key=True)
    comment_name = db.Column(db.String(255))
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    blog_id = db.Column(db.Integer, db.ForeignKey("blogs.id"))

    def save_comment(self):
        '''
        save the comment per blog
        '''
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls,id):
        comment = Comments.query.order_by (Comments.date_posted.desc()).all()
        return comment 

    @classmethod
    def delete_comment(cls,id):
        comment = Comments.query.filter_by(id=id).first()
        db.session.delete(comment)
        db.session.commit()
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,SubmitField,BooleanField,TextAreaField,SelectField,FileField
from wtforms.validators import Required, Email, EqualTo
from flask_wtf.file import FileField, FileRequired, FileAllowed
from app import photos

class ProjectForm(FlaskForm):
    title = StringField('Project title',validators=[Required()])
    post = TextAreaField('Brief Description of Your Project',validators=[Required()])
    category = SelectField('Category',choices=[('Moringa_School_Project','Moringa_School_Project'),('General_Project','General_Project')])
    content = TextAreaField('Github Link',validators=[Required('File is empty')])
    photo = FileField(validators=[FileAllowed(photos, u'Image only!'), FileRequired(u'File was empty!')])
    submit = SubmitField('Submit')
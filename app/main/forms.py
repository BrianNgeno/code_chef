from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,SubmitField,BooleanField,TextAreaField,SelectField
from wtforms.validators import Required, Email, EqualTo

class ProjectForm(FlaskForm):
    title = StringField('Project title',validators=[Required()])
    category = SelectField('Category',choices=[('Moringa_School_Project','Moringa_School_Project'),('General_Project','General_Project')])
    content = TextAreaField('Github Link',validators=[Required()])
    submit = SubmitField('Submit')
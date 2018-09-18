from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,SubmitField,BooleanField,TextAreaField,SelectField


class ProjectForm(FlaskForm):
    title = StringField('Project title',validators=[Required()])
    category = SelectField('Category',choices=[('Moringa_School_Project','Moringa_School_Project'),('General_Project','General_Project')])
    content = TextAreaField('Your Blog.'validators=[Required()])
    submit = SubmitField('Submit')
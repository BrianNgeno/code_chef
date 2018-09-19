from flask import render_template, request,redirect, url_for,abort
from . import main
from ..models import User,Projects,Role
from flask_login import login_required,current_user
from .forms import ProjectForm
from .. import db

@main.route('/')
def index():
    '''
    view root page function that returns the index page
    '''
    title = 'Home - Welcome to The Best Blog Site Worldwide You Think of It We help share It.'
    return render_template('index.html',title = title)



@main.route('/project/new',methods=['GET','POST'])

def new_project():
   
    form = ProjectForm()
    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data
        new_project = Projects(title=title,category= form.category.data,user=current_user)
        new_project.save_project()
        return redirect(url_for('.index'))
    return render_template('new_project.html',form=form)

@main.route('/project/view')
def view_project():
    '''
    route that returns projects
    '''
    projects = Projects.query.order_by(Projects.date_posted.desc()).all()
    return redirect(url_for('.index'))
    return render_template('project.html', project=project)

# @main.route('/add_screenshot',methods= ['POST'])
# @login_required
# def save_screenshot():
#     if 'photo' in request.files:
#         filename = photos.save(request.files['photo'])
#         path = f'photos/{filename}'
#         Projects.photo = path
#         db.session.commit()
#     return  render_template('projects.html')
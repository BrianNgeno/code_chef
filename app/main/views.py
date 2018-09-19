from flask import render_template, request,redirect, url_for,abort
from . import main
from ..models import User,Projects,Role
from flask_login import login_required,current_user
from .forms import ProjectForm
from .. import db, photos

@main.route('/')
def index():
    '''
    view root page function that returns the index page
    '''
    title = 'Home - Welcome to The Best Blog Site Worldwide You Think of It We help share It.'
    return render_template('index.html',title = title)



@main.route('/project/new',methods=['GET','POST'])
@login_required
def new_project():
   
    form = ProjectForm()
    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data
        post = form.actual_post.data
        user=current_user
        filename = photos.save(form.photo.data)
        photo = form.photo.data
        file_url = photos.url(filename)
        new_project = Projects(title=title,category= form.category.data,user=user,photo=file_url)
         
        db.session.add(new_project)
        db.session.commit()
        return redirect(url_for('main.view_project'))
    return render_template('new_project.html',form=form)

@main.route('/project/view')
def view_project():
    '''
    route that returns projects
    '''
    project = Projects.query.filter_by(category='Moringa_School_Project')
    images = 'images/404.jpg'

    return render_template('projects.html', project=project, images=images)

@main.route('/add_screenshot',methods= ['POST'])
@login_required
def save_screenshot():
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        Projects.photo = path
        db.session.commit()
    return  render_template('projects.html')
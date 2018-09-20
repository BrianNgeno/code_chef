from flask import render_template, request,redirect, url_for,abort
from . import main
from ..models import User,Projects,Role,Comments
from .forms import ProjectForm, CommentForm
from .. import db, photos
from flask_login import login_required,current_user

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
        actual_post = form.post.data
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
    Projec = Projects.query.filter_by(category='General_Project')
    images = 'images/404.jpg'

    return render_template('projects.html', project=project, images=images,projec=projec)


@main.route('/new/comment/<int:id>',methods = ['GET','POST'])
@login_required
def new_comment(id):
    form = CommentForm()
    if form.validate_on_submit():
        view = Comments(comment_name = form.comment_name.data,user=current_user, projects_id =id)
        view.save_comment()
        return redirect(url_for('main.view_comments'))
    return render_template('comments.html',form = form,view=view)

@main.route('/comment/<int:id>/view')
def view_comments(id):
    comment = Comments.query.filter_by(project_id = id)
    return render_template('comment.html',comment = comment)

@main.route('/delete_comment/<int:id>')
@login_required
def delete_comment(id):
    if current_user.is_authenticated:
        comment = Comments.query.filter_by(id = id).first()
        db.session.delete(comment)
        db.session.commit()
        return redirect(url_for('main.view_comments'))
    return render_template('comments.html')

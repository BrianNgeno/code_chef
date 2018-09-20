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
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'

        new_project = Projects(title=title,actual_post=actual_post,category= form.category.data,user=user,photo=path)

         
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
    projo = Projects.query.filter_by(category='General_Project')
    images = 'images/404.jpg'

    return render_template('projects.html', project=project, images=images,projo=projo)


@main.route('/new/comment/<int:id>',methods = ['GET','POST'])
@login_required
def new_comment(id):
    form = CommentForm()
    comment = Comments.query.filter_by(projects_id = id)

    if form.validate_on_submit():
        views = Comments(comment_name = form.comment_name.data,user=current_user, projects_id =id)
        views.save_comment()
        return redirect(url_for('main.new_comment',id=id))
    return render_template('comments.html',form = form, comment = comment)

@main.route('/delete_comment/<int:id>')
@login_required
def delete_comment(id):
    if current_user.is_authenticated:
        comment = Comments.query.filter_by(id = id).first()
        db.session.delete(comment)
        db.session.commit()
        return redirect(url_for('main.view_comment',id=id))
    return render_template('comments.html')

@main.route('/view_comment/<int:id>')
@login_required
def view_comment(id):
    comment = Comments.query.filter_by(id = id).first()
    return render_template('comments.html',comment=comment)
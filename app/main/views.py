from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import Projects,User,Comments
from flask_login import current_user
from app import db

@main.route('/')
def index():
    title = 'Dashboard' if current_user.is_authenticated else 'Home'
    projects = Projects.query.all()
    categories = db.session.query(Projects.category).distinct().all()
    definedcategories = [('Moringa School Projects',),('General Projects',),('Implemented Ideas',)]
    categories = set(categories+definedcategories)
    incomplete = Projects.query.filter_by(complete=True).all()
    print(incomplete)
    return render_template('dashboard.html', type='post', title = title,posts=projects,categories=categories,uncompleted=incomplete)


@main.route('/new_project_idea')
def new_project_idea():
    return render_template('pitch_dashboard.html',title='new project idea')

@main.route('/project_ideas')
def ideas():
    title = 'Project ideas'
    return render_template('pitch_dashboard.html',title=title)

@main.route('/Workedon_ideas')
def workedon_ideas():
    title = 'Workedon ideas'
    return render_template('pitch_dashboard.html',title=title)

@main.route('/implemented_ideas')
def implemented_ideas():
    title = 'implemented ideas'
    return render_template('pitch_dashboard.html',title=title)
@main.route('/')
def dashboard():
    title = 'Dashboard' if current_user.is_authenticated else 'Home'
    projects = Projects.query.all()
    categories = db.session.query(Projects.category).distinct().all()
    definedcategories = [('Moringa School Projects',),('General Projects',),('Implemented Ideas',)]
    categories = set(categories+definedcategories)
    incomplete = Projects.query.filter_by(complete=True).all()
    print(incomplete.project)
    return render_template('dashboard.html', title = title,posts=projects,categories=categories,uncompleted=incomplete)

@main.route('/newproject')
def pitch():
    newpost = Projects(project=request.args['pitch_ideas'],category=request.args['category'], complete=False)
    db.session.add(newpost)
    db.session.commit()
    newposts=[newpost]

    return render_template('ideas_dashboard.html',type='post',posts=newposts)
 
@main.route('/complete/<int:id>',methods=["POST","GET"])
def complete(id):
    fetchedproject = Projects.query.filter_by(id=id).first()
    fetchedproject.complete = True
    db.session.commit()

    return 'Changed'

@main.route('/delete/<int:id>',methods=["POST","GET"])
def delete(id):
    fetchedproject = Projects.query.filter_by(id=id).first()
    db.session.delete(fetchedproject)
    db.session.commit()

    return 'Changed'

@main.route('/newcomment/<int:postid>', methods = ['GET','POST'])
def new_comment(postid):
    new_comment = Comments(details = str(request.form['details']),projects_id=str(request.form['post']))
    # # save commen
    db.session.add(new_comment)
    db.session.commit()
    newcomments=[new_comment]
    return render_template('dashboard.html',type='comment',comments=newcomments)
    
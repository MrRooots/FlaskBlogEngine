from flask import Blueprint, render_template
from flask import request, redirect, url_for
from flask_security import login_required

from .forms import PostCreationForm
from models import Post
from app import database

# https://www.youtube.com/watch?v=UqRawhLNE-0&list=PLe4mIUXfbIqaLWrzsSDQAAK3_NQB1jBZZ&index=7
posts = Blueprint('post', __name__, template_folder='templates')


# localhost:5000/posts
@posts.route('/')
def display_posts():
  search_query = request.args.get('search_query', None)

  if search_query is not None:
    posts_list = Post.query.filter(Post.title.contains(search_query) | Post.body.contains(search_query))
  else:
    posts_list = Post.query.order_by(Post.creation_date.desc())

  page = request.args.get('page', None)

  if page is not None and page.isdigit():
    page = int(page)
  else:
    page = 1

  post_slice = posts_list.paginate(page=page, per_page=5)

  return render_template(
    'posts/display_posts.html',
    posts=posts_list,
    post_slice=post_slice
  )


@posts.route('/create', methods=['POST', 'GET'])
@login_required
def display_post_creation_form():
  if request.method == 'POST':
    title = request.form.get('title', '')
    body = request.form.get('body', '')

    try:
      new_post = Post(title=title, body=body)
      database.session.add(new_post)
      database.session.commit()
      return redirect(url_for('post.display_post_details', slug=new_post.slug))

    except:
      print('Errors during post saving')

  else:
    return render_template(
      'posts/display_post_creation_form.html',
      form=PostCreationForm()
    )


@posts.route('/<slug>')
def display_post_details(slug):
  return render_template(
    'posts/display_post_details.html',
    post=Post.query.filter(Post.slug == slug).first()
  )


@posts.route('/<slug>/edit', methods=['POST', 'GET'])
def display_post_edit_form(slug):
  post = Post.query.filter(Post.slug == slug).first()  # Get the post from db

  # Check the method type
  if request.method == 'GET':
    form = PostCreationForm(obj=post)  # Display form with existing information from db

    return render_template('posts/display_post_edit_form.html', post=post, form=form)

  elif request.method == 'POST':
    # formdata - new data from user, obj - existing data from db
    form = PostCreationForm(formdata=request.form, obj=post)  # Display form with existing information from db
    form.populate_obj(post)  # Update the existing in db data by received from user
    database.session.commit()  # Save the changes to db

    return redirect(url_for('post.display_post_details', slug=post.slug))

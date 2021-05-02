from flask_security import UserMixin, RoleMixin

from time import time
from datetime import datetime
from app import database
from utils import slugify

# Post-Tag relationship table
post_tag_relation_database = database.Table(
  'post_tag',
  database.Column('post_id', database.Integer, database.ForeignKey('post.id')),
  database.Column('tag_id', database.Integer, database.ForeignKey('tag.id')),
)


# Simplest post model
class Post(database.Model):
  id = database.Column(database.Integer, primary_key=True)
  title = database.Column(database.String(256))
  slug = database.Column(database.String(256), unique=True)
  body = database.Column(database.Text)
  creation_date = database.Column(database.DateTime, default=datetime.now())

  tags = database.relationship(
    'Tag', secondary=post_tag_relation_database, backref=database.backref('posts'), lazy='dynamic'
  )

  def __init__(self, *args, **kwargs):
    super(Post, self).__init__(*args, **kwargs)
    if self.title:
      self.slug = slugify(self.title, 'Post')
    else:
      self.slug = slugify(str(int(time())), 'Post')

  # Magic method that will return the object name while using print(object)
  def __repr__(self):
    return f'<Post id: {self.id} title: {self.title}>'


# Simplest tag model
class Tag(database.Model):
  id = database.Column(database.Integer, primary_key=True)
  title = database.Column(database.String(256), unique=True)
  slug = database.Column(database.String(256), unique=True)

  def __init__(self, *args, **kwargs):
    super(Tag, self).__init__(*args, **kwargs)
    if self.title:
      self.slug = slugify(self.title, 'Tag')
    else:
      self.slug = slugify(str(int(time())), 'Tag')

  def __repr__(self):
    return f'<Tag id: {self.id}, title: {self.title}>'


# User-Role relationship table
user_role_relation_database = database.Table(
  'user_role',
  database.Column('user_id', database.Integer, database.ForeignKey('user.id')),
  database.Column('role_id', database.Integer, database.ForeignKey('role.id')),
)


# Simple user model
class User(database.Model, UserMixin):
  id = database.Column(database.Integer, primary_key=True)
  email = database.Column(database.String(100), unique=True)
  password = database.Column(database.String(255))
  active = database.Column(database.Boolean)
  roles = database.relationship(
    'Role', secondary=user_role_relation_database, backref=database.backref('users'), lazy='dynamic'
  )


# Simple user role model
class Role(database.Model, RoleMixin):
  id = database.Column(database.Integer, primary_key=True)
  name = database.Column(database.String(100), unique=True)

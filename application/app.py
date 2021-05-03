from flask import Flask, redirect, url_for, request

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView

from flask_security import SQLAlchemyUserDatastore
from flask_security import Security, current_user

from config import Config

# Initializing the Flask application itself
app = Flask(__name__)

# Apply configurations from a special class
app.config.from_object(Config)

# Create a database
database = SQLAlchemy(app)

# To avoid the circular import error - db is needed in models module
from models import Post, Tag, User, Role

# Migration
migrate = Migrate(app, database)

# Manager
manager = Manager(app)
manager.add_command('database', MigrateCommand)


class AdminMixin:
  @staticmethod
  def is_accessible():
    return current_user.has_role('admin')

  @staticmethod
  def inaccessible_callback(name, **kwargs):
    return redirect(url_for('security.login', next=request.url))


# Admin models
class AdminView(AdminMixin, ModelView):
  pass


class HomeAdminView(AdminMixin, AdminIndexView):
  pass


class BaseModelView(ModelView):
  def on_model_change(self, form, model, is_created):
    if is_created:
      from utils import slugify
      model.slug = slugify(model.title, model.__class__.__name__)
    return super(BaseModelView, self).on_model_change(form, model, is_created)


# View that controls the content of admin post creation form
class PostAdminView(AdminMixin, BaseModelView):
  form_columns = ['title', 'body', 'tags']


# View that controls the content of admin tag creation form
class TagAdminView(AdminMixin, BaseModelView):
  form_columns = ['title', 'posts']


# Admin dashboard
admin = Admin(app, 'Blog Homepage', url='/', index_view=HomeAdminView())

# Endpoint -> to remove blueprints name conflicts {before if discover another way ;/}
# Endpoint: http://127.0.0.1:5000/admin/_posts/
admin.add_view(PostAdminView(Post, session=database.session, endpoint='_posts'))
# Endpoint: http://127.0.0.1:5000/admin/_tags/
admin.add_view(TagAdminView(Tag, session=database.session, endpoint='_tags'))

# Flask security section
user_datastore = SQLAlchemyUserDatastore(database, User, Role)
security = Security(app, user_datastore)

from app import app
from posts.posts_blueprint import posts
from tags.tags_blueprints import tags
from views import display_homepage

# Posts application
app.register_blueprint(posts, url_prefix='/posts')
app.register_blueprint(tags, url_prefix='/tags')

if __name__ == '__main__':
  app.run()

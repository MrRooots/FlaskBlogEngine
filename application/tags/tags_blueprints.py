from flask import Blueprint, render_template
from models import Tag
from .forms import TagCreationForm

tags = Blueprint('tag', __name__, template_folder='templates')


@tags.route('/')
def display_tags():
  return render_template(
    'tags/display_tags.html',
    tags=Tag.query.all()
  )


@tags.route('/<slug>')
def display_tag_details(slug):
  return render_template(
    'posts/display_tag_details.html',
    tag=Tag.query.filter(Tag.slug == slug).first_or_404()
  )

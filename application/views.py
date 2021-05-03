from flask import render_template
from app import app


# Function to display the homepage
@app.route('/')
@app.route('/home/')
def display_homepage():
  function_name = display_homepage.__name__
  return render_template('homepage.html', function_name=function_name)


@app.errorhandler(404)
def page_not_found(_):  # Takes event as argument
  return render_template('404.html'), 404


from wtforms import Form, StringField


# Tag creation form
class TagCreationForm(Form):
  title = StringField('title')

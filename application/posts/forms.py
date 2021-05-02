from wtforms import Form, StringField, TextAreaField


# Post creation form
class PostCreationForm(Form):
  title = StringField('Title')
  body = TextAreaField('Body')

from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class BookingForm(FlaskForm):
      event_name = StringField('Event Name', validators=[Required()])
      email = StringField('Enter Email', validators=[Required()])
      phone_number = StringField('Phone Number', validators=[Required()])
      submit = SubmitField('Book')
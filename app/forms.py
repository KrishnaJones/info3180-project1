from flask_wtf import FlaskForm
from wtforms.validators import InputRequired
from wtforms import StringField,IntegerField,TextAreaField,FloatField,SelectField
from flask_wtf.file import FileField, FileRequired, FileAllowed

class PropertyForm(FlaskForm):
	title = StringField('Property Title', validators=[InputRequired()])
	description = TextAreaField('Description', validators=[InputRequired()])
	num_of_bedrooms = IntegerField('No. of Rooms', validators=[InputRequired()])
	num_of_bathrooms = IntegerField('No. of Bathrooms', validators=[InputRequired()])
	price = FloatField('Price', validators=[InputRequired()])
	type = SelectField('Property Type', choices = [('House'),('Apartment')])
	location = StringField('Location', validators=[InputRequired()])
	photo = FileField('Photo', validators=[FileRequired(),FileAllowed(['jpg', 'png'], 'Only Images!')])

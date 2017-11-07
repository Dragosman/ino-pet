from flask_wtf import Form
from wtforms import StringField, BooleanField, DecimalField, SelectField
from wtforms.validators import DataRequired

class LoginForm(Form):
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)

class EditFoodForm(Form):
	pass

	# astea toate ar trebui sa fie search (next, after MVP - search to select them)
	# poate le facem din FE - send to FE
	food_company = StringField(u'Food Company', validators=[DataRequired()])
	food_name = StringField(u'Food Name', validators=[DataRequired()])
	food_type = SelectField(u'Food Type', choices=[('dry', 'Uscata'), ('can', 'Conserva'), ('other', 'Alt tip')])
	food_quantity = DecimalField(u"Cantitate totala in grame", places=2, rounding=None, use_locale=False, number_format=None)
	food_frequency = DecimalField(u"Cantitate totala in grame", places=2, rounding=None, use_locale=False, number_format=None)

	





class AddFoodForm(Form):
	pass

class EditAlertsForm(Form):
	pass

class EditDogForm(Form):
	pass

class AddDogForm(Form):
	pass

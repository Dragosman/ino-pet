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
	food_company = StringField(u'foodCompany', validators=[DataRequired()])
	food_name = StringField(u'foodName', validators=[DataRequired()])
	food_type = SelectField(u'foodType', choices=[('dry', 'Uscata'), ('can', 'Conserva'), ('other', 'Alt tip')])
	food_quantity = DecimalField(u"newQuantity", places=2, rounding=None, use_locale=False, number_format=None)
	food_frequency = DecimalField(u"newFrequency", places=2, rounding=None, use_locale=False, number_format=None)







class AddFoodForm(Form):
	pass

class EditAlertsForm(Form):
	pass

class EditDogForm(Form):
	catel_name = StringField('catel-name', validators=[DataRequired()])
	catel_breed = StringField('catel-breed', validators=[DataRequired()])
	catel_dob = StringField('catel-dob', validators=[DataRequired()])
	catel_weight = StringField('catel-weight', validators=[DataRequired()])
	
	catel_vaccine_last = StringField('catel-ultim-vaccin', validators=[DataRequired()])
	catel_vaccine_last_type = StringField('catel-ultim-vaccin-tip', validators=[DataRequired()])
	catel_vaccine_next = StringField('catel-next-vaccin', validators=[DataRequired()])
	
	catel_di_last = StringField('catel-ultim-di', validators=[DataRequired()])
	catel_di_last_type = StringField('catel-ultim-di-tip', validators=[DataRequired()])
	catel_di_next = StringField('catel-next-di', validators=[DataRequired()])

	catel_de_last = StringField('catel-ultim-de', validators=[DataRequired()])
	catel_de_last_type = StringField('catel-ultim-de-tip', validators=[DataRequired()])
	catel_de_next = StringField('catel-next-de', validators=[DataRequired()])

class AddDogForm(Form):
	pass

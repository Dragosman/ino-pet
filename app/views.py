from flask import render_template, flash, redirect, request
from app import app
#from .forms import LoginForm
import helpers as hl
from .forms import EditDogForm

@app.route('/')
@app.route('/index.html', methods=['GET', 'POST'])
def index():
    
    dogs = hl.getDogs()
    alerts = hl.getAlerts() 
    form1 = EditDogForm()

    if request.method == 'POST':
    	if form1.validate:
    		return "Form posted"
    		# need to redirect and post data / modify the data in the firebase data base - tomorrow
    	'''    	
    	if form1.validate_on_submit():
    		flash('Multumim! Datele au fost salvate!')
    		return redirect('/index')
    	'''
    
    return render_template("index.html",
    	title='Inopet Dashboard',
    	dogs=dogs,
    	alerts=alerts,
    	form1 = form1)

@app.route('/food.html')
def food():
    #user = {'nickname': 'Dragos'}  # user fals
    
    food = hl.getFood() 


    return render_template("food.html",
                           title='Inopet Dashboard - Mancare',
                           food=food,
                           )



'''
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
    	flash('Login requested for OpenID="%s", remember me=%s' % (form.openid.data, str(form.remember_me.data)))
    	return redirect('/index')

    return render_template('login.html', 
                           title='Sign In',
                           form=form,
                           providers=app.config['OPENID_PROVIDERS'])
'''
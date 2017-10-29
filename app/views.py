from flask import render_template, flash, redirect
from app import app
#from .forms import LoginForm
import helpers as hl

@app.route('/')
@app.route('/index.html')
def index():
    #user = {'nickname': 'Dragos'}  # user fals
    
    dogs = hl.getDogs()
    alerts = hl.getAlerts() 


    return render_template("index.html",
                           title='Inopet Dashboard',
                           dogs=dogs,
                           alerts=alerts)

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
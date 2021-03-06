from flask import Flask, render_template, request, flash, redirect
from app import app
#from .forms import LoginForm
import helpers as hl
from .dogs import Dog
from .food import *
from .forms import EditDogForm, EditFoodForm, AddFoodForm

@app.route('/')
@app.route('/index.html', methods=['GET', 'POST'])
def index():
    
    dogs = hl.getDogs()
    alerts = hl.getAlerts() 
    form1 = EditDogForm()
    msg1 = ""

    if request.method == 'POST':
    	if form1.validate_on_submit():
    		# transform un obiect dog
    		# hl.updateDog(key, dog)
    		dog1 = Dog()
    		dog1.key = form1.data['catel_k']
    		dog1.name = form1.data['catel_name']
    		dog1.weight=form1.data['catel_weight']
    		dog1.breed=form1.data['catel_breed']
    		dog1.dob=form1.data['catel_dob']
    		dog1.vaccine_last = {"date":form1.data['catel_vaccine_last'], "name":form1.data['catel_vaccine_last_type']}
    		dog1.vaccine_next = {"date":form1.data['catel_vaccine_next'], "name":"NEXT"}
    		dog1.depar_int_last = {"date":form1.data['catel_di_last'], "name":form1.data['catel_di_last_type']}
    		dog1.depar_int_next = {"date":form1.data['catel_di_next'], "name":"NEXT"}
    		dog1.depar_ext_last = {"date":form1.data['catel_de_last'], "name":form1.data['catel_de_last_type']}
    		dog1.depar_ext_next = {"date":form1.data['catel_de_next'], "name":"NEXT"}

    		print (dog1.vaccine_last)
    		print(dog1.depar_ext_next)

    		print (dog1.depar_int_last)
    		
    		hl.updateDog(dog1.key, dog1)
    		msg1='Multumim! Schimbarile tale fost salvate!'

    		
    	else: 
    		msg1="Ai uitat sa completezi toate campurile!"


    		
    		# aici codul de save
    		#return "Form posted"
    		# need to redirect and post data / modify the data in the firebase data base - tomorrow
    	'''    	
    	if form1.validate_on_submit():

    	'''
    	flash(msg1)
    	return rdirect("index.html") 

    return render_template("index.html",
    	title='Inopet Dashboard',
    	dogs=dogs,
    	alerts=alerts,
    	form1 = form1,
    	msg1=msg1)

@app.route('/food.html', methods=['GET', 'POST'])
def food():
    #user = {'nickname': 'Dragos'}  # user fals
    
    food = hl.getFood() 
    form1 = EditFoodForm()
    form2 = AddFoodForm()
    msg1 = ""

    if request.method=="POST":
    	if form1.validate_on_submit():
    		food1 = Food()
    		food1.key=form1.data['food_k']
    		food1.name = form1.data['food_name']
    		food1.company=""
    		food1.type=form1.data["food_type"]
    		food1.quantity=float(form1.data["food_quantity"])
    		food1.freq = float(form1.data["food_frequency"])
    		 

    		a,b = days_estimator(food1)
    		food1.days_estimated = a
    		food1.quantity=str(form1.data["food_quantity"])
    		food1.freq = str(form1.data["food_frequency"])
    		hl.updateFood(food1.key, food1)
    		msg1="Multumim! Schimbarile tale fost salvate!"
			
    		
    	else:
    		msg1="Ai uitat sa completezi toate campurile!"   		
    		
    	flash(msg1)
    	return redirect("food.html")

    return render_template("food.html",
                           title='Inopet Dashboard - Mancare',
                           food=food, form1=form1, form2=form2, msg1=msg1
                           )


@app.route('/alerts.html', methods=['GET', 'POST'])
def alerts():
	alerts = hl.getAlerts() 

	return render_template("alerts.html", title="Inopet Dashboard - Alerte", alerts = alerts)

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
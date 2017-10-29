import datetime as dt
date_format = "%d/%m/%Y"

class Food:
	def __init__(self):
		self.key=""
		self.company=""
		self.name=""
		self.type=""
		self.quantity=""
		self.guide={"error":"", "quants":[]}
		self.freq=""
		self.days_estimated=""
		
	def setBasics(self, company, name, tp, quantity, freq, key=""):

		#self.company=company
		self.company=company
		self.name=name
		self.type=tp
		self.quantity=quantity
		self.freq=freq
		if key!="":
			self.key=key


	def setGuide(self, error, quants):
		self.guide["error"]=error
		self.guide["quants"]=quants

	def updateQuantity(self, no_bags=1, quant=10000, total_quant=0):
		if total_quant!=0:
			self.quantity=total_quant
		else:
			self.quantity = no_bags*quant

	def days_estimator(self):
		self.days_estimated=int(float(self.quantity)/float(self.freq))
		return int(float(self.quantity)/float(self.freq))


def quantity_mapper():
	# hardcode values to simplify the values for Hills Zd dry and canned
	return [700, 180]


def add_days(initial_date="NOW", days=30):

	if initial_date=="NOW":
		b = dt.datetime.today().strftime("%d/%m/%Y")
		b = dt.datetime.strptime(b,date_format)
		end_date = b + dt.timedelta(days)
		return end_date.strftime(date_format)
	else:
		date_1 = dt.datetime.strptime(initial_date, date_format)
		end_date = date_1 + dt.timedelta(days)
		end_date1 = dt.datetime.strftime(end_date, date_format)
		return end_date1.strftime(date_format)


def retract_days(initial_date="NOW", days="10"):
	if initial_date=="NOW":
		b = dt.datetime.today().strftime("%d/%m/%Y")
		b = dt.datetime.strptime(b,date_format)
		end_date = b - dt.timedelta(days)
		return end_date.strftime(date_format)
	else:
		date_1 = dt.datetime.strptime(initial_date, date_format)
		end_date = date_1 - dt.timedelta(days)
		end_date1 = dt.datetime.strftime(end_date, date_format)
		return end_date1


#-------
def days_estimator(food):
	#addition_date = date when we have the food home
	
	total_quantity = float(food.quantity)
	quantity_per_day=0.0

	#cod care estimeaza based on food and kg_dogs
	# quantity_per_day
	quant = quantity_mapper()
	if food.name=="ZD" and food.type=="dry":
		quantity_per_day=quant[0]
	elif food.name=="ZD" and food.type=="can":
		quantity_per_day=quant[1]


	total_days = total_quantity/quantity_per_day
	return (total_days, add_days("NOW", total_days))
	





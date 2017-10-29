import datetime as dt
date_format = "%d/%m/%Y"

class Alert:
	def __init__(self):
		self.name=""
		self.key=""
		self.type=""
		self.first={"date":"", "sent":""}
		self.second={"date":"", "sent":""}
		self.description=""
	def getBasics():
		return(self.name, self.type, self.first, self.second)
 
	def setBasics(self, name, typ, first, second, description, key=""):
		self.key = key
		self.name=name
		self.type=typ
		self.first=first
		self.second=second
		self.description = description
		if key!="":
			self.key=key		


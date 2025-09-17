from datetime import data
class person :
def __init__(self,name,country,dob):
self.name=name
self.country=coumtry
self.dob=dob
# calculate the age of the person based on their date of birth
def calage(self):
today=date.today()
age = today.year-self.dob.year
if today < date(today.year,selfe.dob.month,self.dob.day):
age -= 1
return age
p1 = person("Sam", "ongole", date(2007,9,22))

print("calculateed age for each person")
print("**********************************")
print("person 1:")
print("Name:",p1.name)
print("Country:".p1.country)
print("Date of birth:".p1.dob)
print("Age:",p1.calage())


from peewee import *
from playhouse.shortcuts import model_to_dict
from datetime import date
from helper import validateCarNumber , parseCarNumber
db = SqliteDatabase('svt.db')

class Cars(Model):
  number = TextField(primary_key=True)
  model = TextField()
  modelYear = TextField()
  odometer = IntegerField()
  color = TextField()
  engineNumber = TextField()
  chassisNumber = TextField()
  purchasedFrom = TextField()
  purchasedOn = DateField()
  purchaseLocation = TextField()
  purchaseReference = TextField()
  ownerNumber = IntegerField()
  soldTo = TextField()
  soldOn = DateField()
  soldLocation = TextField()
  transferDone = TextField()
  insuranceDate = DateField()
  pollutionDate = DateField()
  fine = TextField()
  purchasePrice = IntegerField()
  expenses = IntegerField()
  salePrice = IntegerField()
  remarks = TextField()

  class Meta:
    database = db

db.connect()
db.create_tables([Cars])

def purchaseCar(number,model,modelYear,odometer,color,engineNumber,chassisNumber,purchasedFrom,purchasedOn,purchaseLocation,purchaseReference,ownerNumber,purchasePrice):
  if not validateCarNumber(number):
    return 'Invalid Car Number'
  modelYear = str(modelYear)
  if not len(modelYear) != 4 and (not modelYear.isdigit()):
    return 'Invalid Model Year'
  purchasedOn = date.fromisoformat(purchasedOn)
  soldTo = ''
  soldOn = date.today()
  soldLocation = ''
  transferDone = 'f'
  insuranceDate = date.fromisoformat(insuranceDate)
  pollutionDate = date.fromisoformat(pollutionDate)
  fine = 'No fines'
  expenses = 0
  salePrice = 0
  remarks = 'No remarks'
  return Cars(number=number,model=model,modelYear=modelYear,odometer=odometer,color=color,engineNumber=engineNumber,chassisNumber=chassisNumber,purchasedFrom=purchasedFrom,purchasedOn=purchasedOn,purchaseLocation=purchaseLocation,purchaseReference=purchaseReference,ownerNumber=ownerNumber,soldLocation=soldLocation,soldOn=soldOn,soldTo=soldTo,transferDone=transferDone,insuranceDate=insuranceDate,pollutionDate=pollutionDate,fine=fine,purchasePrice=purchasePrice,expenses=expenses,salePrice=salePrice,remarks=remarks).save(force_insert=True)

def resp(data):
  resp = []
  for i in data:
    i = model_to_dict(i)
    i['numberHuman'] = parseCarNumber(i['number'])
    resp.append(i)
  return resp

def getCar(number):
  return resp(Cars.select().where(Cars.number == number))

def getAllCars():
  return resp(Cars.select())
    
def getUnsoldCars():
  return resp(Cars.select().where(Cars.salePrice == 0))

def getUntransferedCars():
  return resp(Cars.select().where(Cars.transferDone == 'f'))

def searchCars(searchText):
  return resp(Cars.select().where(
    (Cars.model.contains(searchText))|(Cars.modelYear.contains(searchText))|
    (Cars.color.contains(searchText))|(Cars.number.contains(searchText))))

def editRemarks(number,newRemarks):
  Cars.update(remarks=newRemarks).where(Cars.number == number)
  return True

def editExpenses(number,newExpenses):
  Cars.update(expenses=newExpenses).where(Cars.number == number)
  return True

def transferCar(number):
  Cars.update(transferDone='t').where(Cars.number == number)
  return True

def sellCar(number,soldTo,soldOn,soldLocation,transferDone,insuranceDate,pollutionDate,expenses,salePrice,remarks):
  insuranceDate = date.fromisoformat(insuranceDate)
  pollutionDate = date.fromisoformat(pollutionDate)
  soldOn = date.fromisoformat(soldOn)
  Cars.update(soldTo=soldTo,soldOn=soldOn,soldLocation=soldLcation,transferDone=transferDone,insuranceDate=insuranceDate,pollutionDate=pollutionDate,expenses=expenses,salePrice=salePrice,remarks=remarks).where(Cars.number == number)
  return True

def deleteCar(number):
  Cars.delete().where(Cars.number == number)
  return True
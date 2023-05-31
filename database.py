from peewee import *
from datetime import date
from helper import validateCarNumber
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
  insuranceDate = date.today()
  pollutionDate = date.today()
  fine = 'No fines'
  expenses = 0
  salePrice = 0
  remarks = 'No remarks'
  try:
    Cars(number=number,model=model,modelYear=modelYear,odometer=odometer,color=color,engineNumber=engineNumber,chassisNumber=chassisNumber,purchasedFrom=purchasedFrom,purchasedOn=purchasedOn,purchaseLocation=purchaseLocation,purchaseReference=purchaseReference,ownerNumber=ownerNumber,soldLocation=soldLocation,soldOn=soldOn,soldTo=soldTo,transferDone=transferDone,insuranceDate=insuranceDate,pollutionDate=pollutionDate,fine=fine,purchasePrice=purchasePrice,expenses=expenses,salePrice=salePrice,remarks=remarks).save()
    return True
  except Exception as error:
    return str(error)

def getAllCars():
  return db.select()
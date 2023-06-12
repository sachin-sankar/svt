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
  fuelType = TextField()
  transmissionType = TextField()
  serviceHistory = TextField()
  purchasedFrom = TextField()
  purchasedOn = DateField()
  purchaseLocation = TextField()
  purchaseReference = TextField()
  ownerNumber = IntegerField()
  soldTo = TextField()
  soldOn = DateField()
  soldLocation = TextField()
  saleReference = TextField()
  transferDone = TextField()
  transferDate = DateField()
  insuranceDate = DateField()
  pollutionDate = DateField()
  fine = TextField()
  remarks = TextField()

  class Meta:
    database = db

db.connect()
db.create_tables([Cars])

def purchaseCar(number,model,modelYear,odometer,color,engineNumber,chassisNumber,fuelType,transmissionType,purchasedFrom,purchasedOn,purchaseLocation,purchaseReference,ownerNumber,insuranceDate,pollutionDate,serviceHistory,fine):
  number = number.strip().replace(' ','').lower()
  if not validateCarNumber(number):
    return 'Invalid Car Number'
  modelYear = str(modelYear)
  if not len(modelYear) != 4 and (not modelYear.isdigit()):
    return 'Invalid Model Year'
  purchasedOn = date.fromisoformat(purchasedOn)
  soldTo = ''
  soldOn = date.today()
  soldLocation = ''
  saleReference = ''
  transferDone = 'f'
  insuranceDate = date.fromisoformat(insuranceDate)
  pollutionDate = date.fromisoformat(pollutionDate)
  transferDate = date.today()
  fine = 'No fines'
  remarks = 'No remarks'
  Cars(number=number,model=model,modelYear=modelYear,odometer=odometer,color=color,engineNumber=engineNumber,chassisNumber=chassisNumber,purchasedFrom=purchasedFrom,purchasedOn=purchasedOn,purchaseLocation=purchaseLocation,purchaseReference=purchaseReference,ownerNumber=ownerNumber,soldLocation=soldLocation,soldOn=soldOn,soldTo=soldTo,transferDone=transferDone,insuranceDate=insuranceDate,pollutionDate=pollutionDate,fine=fine,remarks=remarks,fuelType=fuelType,transmissionType = transmissionType,saleReference=saleReference,serviceHistory=serviceHistory,transferDate=transferDate).save(force_insert=True)
  return number

def resp(data):
  resp = []
  for i in data:
    i = model_to_dict(i)
    i['numberHuman'] = parseCarNumber(i['number'])
    i['remarks'] = i['remarks'].replace('\n','')
    resp.append(i)
  return resp

def getCar(number):
  return resp(Cars.select().where(Cars.number == number))

def getAllCars():
  return resp(Cars.select())
    
def getUnsoldCars():
  return resp(Cars.select().where(Cars.soldTo == ''))

def getUntransferedCars():
  return resp(Cars.select().where(Cars.soldTo != '', Cars.transferDone == 'f'))

def searchCars(searchText):
  return resp(Cars.select().where(
    (Cars.model.contains(searchText))|(Cars.modelYear.contains(searchText))|
    (Cars.color.contains(searchText))|(Cars.number.contains(searchText))))

def editCar(number,newRemarks):
  q = Cars.update(remarks=newRemarks)
  q.where(Cars.number == number).execute()
  db.commit()
  return True

def transferCar(number,dateDone):
  Cars.update(transferDone='t',transferDate=date.fromisoformat(dateDone)).where(Cars.number == number).execute()
  db.commit()
  return True

def sellCar(number,soldTo,soldOn,soldLocation,insuranceDate,pollutionDate,remarks,saleReference):
  insuranceDate = date.fromisoformat(insuranceDate)
  pollutionDate = date.fromisoformat(pollutionDate)
  soldOn = date.fromisoformat(soldOn)
  Cars.update(soldTo=soldTo,soldOn=soldOn,soldLocation=soldLocation,insuranceDate=insuranceDate,pollutionDate=pollutionDate,remarks=remarks,saleReference=saleReference).where(Cars.number == number).execute()
  db.commit()
  return True

def deleteCar(number):
  Cars.delete().where(Cars.number == number).execute()
  db.commit()
  return True
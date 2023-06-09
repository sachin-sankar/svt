from flask import Flask, request, render_template, redirect , send_file
from flask_cors import CORS
import database
from csv import writer
from datetime import date

app = Flask('Svt',template_folder='mysite/templates',static_folder='mysite/static')
CORS(app)

@app.route('/')
def homePage():
  return render_template('index.html',
                         unsoldCars=database.getUnsoldCars(),
                         unTransferedCars=database.getUntransferedCars())


@app.route('/cars/<car>')
def viewCarPage(car):
  return render_template('car.html', cars=database.getCar(car))


@app.route('/cars/<car>/edit', methods=['POST'])
def editCarPage(car):
  database.editCar(car, request.form['remarks'])
  return redirect(f'/cars/{car}')


@app.route('/cars/<car>/to/<date>')
def toCarEndpoint(car,date):
  database.transferCar(car,date)
  return redirect(f'/cars/{car}')

@app.route('/cars/<car>/sell')
def sellCarPage(car):
  return render_template('sell.html',car=database.getCar(car)[0])

@app.route('/cars/<car>/sell/api',methods=['POST'])
def sellCarEndpoint(car):
  data = request.form.to_dict()
  data['number'] = car
  database.sellCar(**data)
  return redirect(f'/cars/{car}')

@app.route('/cars/search/<term>')
def searchPage(term):
  return render_template('search.html',cars = database.searchCars(term))

@app.route('/cars/download')
def download():
  cars = database.getAllCars()
  fname = f'Vishva Cars - {date.today().strftime("%d-%m-%Y")}.csv'
  with open(fname,'w') as file:
    csvFile = writer(file)
    csvFile.writerow(list(cars[0].keys()))
    cars = [i.values() for i in cars]
    csvFile.writerows(cars)
  return send_file(fname,as_attachment=True)

@app.route('/cars/buy')
def buyPage():
  return render_template('buy.html')

@app.route('/cars/buy/api',methods=['POST'])
def buyEndpoint():
  data = request.form.to_dict()
  car = database.purchaseCar(**data)
  return redirect(f'/cars/{car}')

@app.route('/cars/<car>/print')
def printPage(car):
  car = database.getCar(car)[0]
  serial = car['purchasedOn'].strftime("%b/%Y").upper()
  return render_template('print.html',car=car,serial = serial)

@app.route('/cars/<car>/delete')
def deleteCar(car):
  database.deleteCar(car)
  return redirect('/')

@app.route('/verify',methods=['post'])
def verifyUser():
  data = request.get_json()['pw']
  print(data)
  if data == 'admin':
    return '',200
  else:
    return '',403

@app.route('/ping')
def ping():
  return 'pong'
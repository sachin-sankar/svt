from flask import Flask, request, render_template, redirect , send_file
from flask_cors import CORS
import database

app = Flask('Svt')
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
  database.editCar(car, request.form['expenses'], request.form['remarks'])
  return redirect(f'/cars/{car}')


@app.route('/cars/<car>/to')
def toCarEndpoint(car):
  database.transferCar(car)
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
app.run('0.0.0.0', port=8080)

@app.route('/cars/download')
def download():
  

from flask import Flask, Request, render_template
from flask_cors import CORS
import database

app = Flask('Svt')
CORS(app)


@app.route('/')
def homePage():
  return render_template('index.html',
                         unsoldCars=database.getUnsoldCars(),unTransferedCars=database.getUntransferedCars())


app.run('0.0.0.0', port=8080)

from json import load
import database

'''
with open('Svt Purchase (1).json','r') as file:
  data = load(file)

for i in data:
  print(purchaseCar(**i))
'''
print(len(database.getAllCars()))
print(len(database.getUnsoldCars()))
print(len(database.getUntransferedCars()))

while True:
  print(database.searchCars(input('::> ')))
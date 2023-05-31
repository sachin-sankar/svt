from json import load
from database import purchaseCar , getAllCars

'''
with open('Svt Purchase (1).json','r') as file:
  data = load(file)

for i in data:
  purchaseCar(**i)
'''
print(getAllCars())
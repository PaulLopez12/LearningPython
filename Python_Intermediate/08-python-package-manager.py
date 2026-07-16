### Python Package Manager ###

# PIP https://pypi.org

# pip install pip
# pip --version
# pip list
# pip uninstall 

import numpy
import pandas
import requests
from mypackage import arithmetics

numpy_array = numpy.array([35, 24, 62, 52, 30, 30, 17])
print(type(numpy_array))

print(numpy_array * 2)
print("---------------------")

response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=151")
print(response)
print(response.status_code)
print(response.json())
print("---------------------")

# Arithmetics Package
print(arithmetics.sum_two_values(1,4))
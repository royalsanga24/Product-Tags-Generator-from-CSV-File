import chunk
import csv
from itertools import product
from . import api
# import api
from datetime import datetime as dt
def handle_uploaded_File(f):
    path = 'media\\media\\'
    with open(path+f, 'r+') as csvfile:
        csv_read = csv.reader(csvfile)
        next(csv_read)
        result_tags = []
        for line in csv_read:
            a = api.get(line)
            result_tags.append(a)

        return result_tags

def get_csv_products(f):
    path = 'media\\media\\' 
    date_time = str(dt.now())
    path2 = 'app\\result\\' + f
    with open(path+f, 'r+') as csvfile:
        csv_read = csv.reader(csvfile)
        next(csv_read)
        result_tags = []
        products = []
        for line in csv_read:
            products.append(line)
        return products

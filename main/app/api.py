from cgitb import reset
from unittest import result
import requests
import json
import csv

def get(product):
    url = "https://twinword-category-recommendation-api.p.rapidapi.com/recommend/"
    querystring = {"text":product}

    headers = {
        "X-RapidAPI-Key": "0b5f43f641msh8ea409c6e9b34e4p1a4b13jsn0e86ad14e593 ",
        "X-RapidAPI-Host": "twinword-category-recommendation-api.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    resultresp = response.json()
    result_categories = resultresp['categories']
    return result_categories

# nutrition.py
import requests


def fetch_food_data(barcode):
    response = requests.get(f"https://world.openfoodfacts.org/api/v0/product/{barcode}.json")
    data = response.json()
    return data

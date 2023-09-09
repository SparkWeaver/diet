# main.py
from barcode import scan_barcode
from nutrition import fetch_food_data


def main():
    # Step 1: Scan barcode and get the barcode data
    barcode_data = scan_barcode()

    # Step 2: Fetch food data using the barcode data
    nutrition_data = fetch_food_data(barcode_data)

    # Step 3: Extract the necessary information and store them in variables
    if nutrition_data['status'] == 1:
        product_data = nutrition_data['product']

        kcal = product_data.get('nutriments', {}).get('energy-kcal_100g', 'Unknown kcal')
        protein = product_data.get('nutriments', {}).get('proteins_100g', 'Unknown protein')
        fat = product_data.get('nutriments', {}).get('fat_100g', 'Unknown fat')

        print(f"Kcal per 100g: {kcal}")
        print(f"Protein per 100g: {protein}")
        print(f"Fat per 100g: {fat}")

        # Here, you have the kcal, protein, and fat stored in variables
        # You can further use these variables in any calculations you wish to perform

    else:
        print("Product not found.")


if __name__ == "__main__":
    main()

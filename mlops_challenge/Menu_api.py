from flask import Flask, jsonify, request
import os
app = Flask(__name__)
import json
# Load the menu data from the JSON files
menu_data = []

def load_json_files(directory):
    json_data = []

    # Iterate over all files in the directory
    for filename in os.listdir(directory):
        # Check if the file is a JSON file
        if filename.endswith('.json'):
            file_path = os.path.join(directory, filename)
            try:
                with open(file_path, 'r') as file:
                    # Load the JSON data from the file
                    data = json.load(file)
                    json_data.append(data)
            except (IOError, OSError, json.JSONDecodeError) as e:
                print(f"Error loading JSON file '{filename}': {str(e)}")

    return json_data


@app.route('/api/customers/<customer_id>', methods=['GET'])
def get_customer_by_id(customer_id):
    for customer in menu_data:
        if customer['id'] == customer_id:
            return jsonify({
                'name': customer['name'],
                'location': f"{customer['city']}, {customer['state']}",
                'menu_url': customer['menu_url']
            })
    return jsonify({'error': 'Customer not found'}), 404


@app.route('/api/foods/<food_term>', methods=['GET'])
def get_customers_by_food(food_term):
    customers = []
    for customer in menu_data:
        if food_term.lower() in customer['raw_text'].lower():
            customers.append({
                'name': customer['name'],
                'location': f"{customer['city']}, {customer['state']}",
                'menu_url': customer['menu_url']
            })
    if customers:
        return jsonify(customers)
    return jsonify({'error': 'No customers sell this food'}), 404


if __name__ == '__main__':
    menu_data = load_json_files(".")
    app.run()

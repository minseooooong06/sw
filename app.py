# -*- coding: utf-8 -*-
import random
from flask import Flask, jsonify, render_template, request
from data import RESTAURANTS, CATEGORIES_WITH_MENUS

app = Flask(__name__)

# Route to serve the main HTML page
@app.route('/')
def index():
    return render_template('index.html')

# API endpoint: List all categories and their associated menus
@app.route('/api/categories', methods=['GET'])
def get_categories():
    return jsonify(CATEGORIES_WITH_MENUS)

# API endpoint: Fetch and filter restaurants
@app.route('/api/restaurants', methods=['GET'])
def get_restaurants():
    category = request.args.get('category')
    menu_item = request.args.get('menu')
    search_query = request.args.get('search')
    
    results = RESTAURANTS
    
    # 1. Filter by category (e.g. 한식, 일식)
    if category:
        results = [r for r in results if r['category'] == category]
        
    # 2. Filter by menu (e.g. 제육볶음, 파스타)
    if menu_item:
        filtered = []
        for r in results:
            # Check if restaurant serves this specific menu item (match substring or exact name)
            for m in r['menus']:
                if menu_item.lower() in m['name'].lower():
                    filtered.append(r)
                    break
        results = filtered
        
    # 3. Filter by search query (restaurant name, category, or menu item)
    if search_query:
        search_query = search_query.strip().lower()
        filtered = []
        for r in results:
            name_match = search_query in r['name'].lower()
            desc_match = search_query in r['description'].lower()
            location_match = search_query in r['location'].lower()
            menu_match = False
            for m in r['menus']:
                if search_query in m['name'].lower():
                    menu_match = True
                    break
            
            if name_match or desc_match or location_match or menu_match:
                filtered.append(r)
        results = filtered
        
    return jsonify(results)

# API endpoint: Get a random restaurant
@app.route('/api/random', methods=['GET'])
def get_random_restaurant():
    category = request.args.get('category')
    
    candidates = RESTAURANTS
    if category:
        candidates = [r for r in candidates if r['category'] == category]
        
    if not candidates:
        return jsonify({"error": "No restaurants found for the selected category"}), 404
        
    random_restaurant = random.choice(candidates)
    return jsonify(random_restaurant)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

from flask import Flask, render_template, request, send_from_directory
from flask_material import Material
import os

app = Flask(__name__)
Material(app)

@app.route('/')
def home():
    guest_info = get_guest_info()
    tot_din_cost = dinner_cost(guest_info['dinner_order'])
    return render_template('home.html', sent=None, guest_info=guest_info, tot_din_cost=tot_din_cost)

@app.route('/favicon.ico')
def fav():
    print(os.path.join(app.root_path, 'static'))
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico')


def get_guest_info(): # Data Type Tutorial

    name = 'Sensei Span' # String, collection of characters
    
    age = 23 #  Integer

    account_balance = 420.69 # Double, Number with a decimal

    diamond_status =  True # Boolean, True or False

    extra_guests = ['Naruto', 'Sasuke', 'Sakura'] # List, collection of values (can be of mostly any types)

    dinner_order = { # Dictionary, collection of values with a key to retrieve them
        'Main Course': 'Sushi',
        'Drink': 'Sparkling Water',
        'Appetizer': 'Wontons',
        'Misc': ['Spicy Mayo', 'Chopsticks', 'Soy Sauce'],
        'Quantity': 4
    }

    guest_info = {
        'name': name,
        'age': age,
        'account_balance': account_balance,
        'diamond_status': diamond_status,
        'extra_guests': extra_guests,
        'dinner_order': dinner_order
    }

    return guest_info


def dinner_cost(dinner_order): # Operators, Conditionals, For Loops
    costs = {
        'Sushi': 10,
        'Sparkling Water': 3,
        'Wontons': 7,
        'Spicy Mayo': 0.5,
        'Soy Sauce': 0,
    }
    tot_cost = 0
    for item  in dinner_order.values():
        if type(item) is list:
            for i in item:
                if i in costs.keys(): # If food item has a cost, then add the cost multiplied by the quantity
                    tot_cost += costs[i] * dinner_order['Quantity']
        else:
            if item in costs.keys():
                tot_cost += costs[item] * dinner_order['Quantity']
    
    return ('%.2f' % round(tot_cost, 2))



if __name__ == '__main__':
    app.run()
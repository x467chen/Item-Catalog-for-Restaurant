from flask import Flask
from flask import render_template, url_for
from flask import request, redirect
from flask import jsonify

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, FoodItem
app = Flask(__name__)

engine = create_engine('sqlite:///restaurant.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

"""mainPage"""
# All Restaurants main page
@app.route('/')
@app.route('/restaurants/')
def showRestaurants():
    restaurants = session.query(Restaurant).all()
    # test url
    return "this is main page, show all restaurant"



#Restaurant-add
@app.route('/restaurants/add/')
def addRestaurant():
    return "this is add a restaurant"

#Restaurant-edit
@app.route('/restaurants/<int:restaurant_id>/edit/')
def editRestaurant(restaurant_id):
	return "This is edit a restaurant"

#Restaurant-delete
@app.route('/restaurants/<int:restaurant_id>/delete/')
def deleteRestaurant(restaurant_id):
    return "this is delete a restaurant"

"""MenuPage"""
#Single restaurant's menu page
@app.route('/restaurants/<int:restaurant_id>/menu')
def showMenu(restaurant_id):
    # restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    # items = session.query(MenuItem).filter_by(restaurant_id=restaurant.id)
    # return render_template('menu.html', restaurant=restaurant, items=items)
    return "this is create a new menu"

#Menu add item page
@app.route('/restaurants/<int:restaurant_id>/menu/add/')
def addItem(restaurant_id):
    return "page to add  a menu item."


#Menu edit page
@app.route('/restaurants/<int:restaurant_id>/menu/<int:menu_id>/edit/')
def editItem(restaurant_id, menu_id):
    return "page to edit a menu item."



#Menu delete page
@app.route('/restaurants/<int:restaurant_id>/menu/<int:menu_id>/delete/')
def deleteItem(restaurant_id, menu_id):
    return "page to delete a menu item."


"""Set JSON ROUTE"""
#Restaurant JSON
@app.route('/restaurants/JSON')
def restaurantJson():
    return "Res-JSON"


#Menu JSON
@app.route('/restaurants/<int:restaurant_id>/menu/JSON')
def MenuJson(restaurant_id):
    return "Menu-JSON"


#Items JSON
@app.route('/restaurants/<int:restaurant_id>/menu/<int:menu_id>/JSON')
def ItemJSON(restaurant_id, menu_id):
    Menu_Item = session.query(MenuItem).filter_by(id=menu_id).one()
    return "Item-JSON"


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)

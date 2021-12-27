from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS
from kijiji import get_kijiji_listings
from houses import House
import json
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="testdatabase"
)

mycursor = db.cursor()
app = Flask(__name__)
api = Api(app)
CORS(app)

# get - get information
# post - modify information / update
# put - add new information
# delete - delete information
# axios.get("localhost:5000/",file)


class homePage(Resource):
    def get(self):
        houses = get_kijiji_listings()
        mycursor.execute("SELECT * FROM housedb")
        print(type(houses[0]))
        for house in mycursor:
            for x in house:
                print(x)
            #houses.append(House(" ", " ", " ", " ", " ", " ", " "))
            houses.append(House(
                str(house[1]), str(houses[2]), str(houses[4]), "0", str(houses[3]), str(houses[5]), str(houses[6])))
        return json.dumps([ob.__dict__ for ob in houses])


class addHouse(Resource):
    def get(self):
        return {'info': 'ok'}

    def put(self):
        info = request.get_json()
        mycursor.reset()
        mycursor.execute(
            "INSERT INTO housedb (listing_name, price, location, description, contact, image) VALUES (%s,%s,%s,%s,%s,%s)", (info['listing_name'], info['price'], info['location'], info['description'], info['contact'], info['image'],))
        db.commit()
        return {'info': 'ITEM ADDED'}


api.add_resource(homePage, '/')
api.add_resource(addHouse, '/add')

if __name__ == '__main__':
    app.run(debug=True)

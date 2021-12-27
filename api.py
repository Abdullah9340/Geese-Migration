from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS
from kijiji import get_kijiji_listings
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
        for house in mycursor:
            print(house)
        return json.dumps([ob.__dict__ for ob in houses])


class addHouse(Resource):
    def put(self):
        info = request.get_json()
        mycursor.execute("INSERT INTO housedb (listing_name, price, location, description, contanct, image)" +
                         f"VALUES ({info['listing_name'],info['price'],info['location'],info['descripion'],info['contact'],info['image']})")
        db.commit()
        return {'info': 'ITEM ADDED'}


api.add_resource(homePage, '/')
api.add_resource(addHouse, '/addItem')
if __name__ == '__main__':
    app.run()

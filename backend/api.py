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
        houses = []
        mycursor.execute("SELECT * FROM housedb")
        for house in mycursor:
            for x in house:
                print(x)
            h = House(str(house[1]), str(house[2]), str(house[4]), "0", str(
                house[3]), str(house[5]), str(house[6]), house[0])
            houses.append(h)
        houses.extend(get_kijiji_listings())
        return json.dumps([ob.__dict__ for ob in houses])


class addHouse(Resource):
    def get(self):
        return {'info': 'Hello World'}

    def put(self):
        info = request.get_json()
        try:
            mycursor.reset()
            mycursor.execute(
                "INSERT INTO housedb (listing_name, price, location, description, contact, image) VALUES (%s,%s,%s,%s,%s,%s)", (info['listing_name'], info['price'], info['location'], info['description'], info['contact'], info['image'],))
            db.commit()
            return {'info': 'ITEM ADDED'}
        except Exception:
            return {'info': 'Error'}


class deleteListing(Resource):
    def get(self):
        return {'info': 'Hello World'}

    def delete(self):
        info = request.get_json()
        try:
            mycursor.reset()
            mycursor.execute(f"DELETE FROM housedb WHERE id = {info['id']}")
            db.commit()
            return {"info": "Item deleted"}
        except Exception:
            return {"info": "Item not Found"}


api.add_resource(homePage, '/')
api.add_resource(addHouse, '/add')
api.add_resource(deleteListing, '/delete')

if __name__ == '__main__':
    app.run(debug=True)

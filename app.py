## Dependencies
import pymongo
from bson.json_util import dumps, loads
from flask import Flask, jsonify, render_template
from flask_cors import CORS, cross_origin

## Flask Setup
app = Flask(__name__)

## Database Setup (MongoDB)
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

## Define database in Mongo
db = client.VideoGamesDB

## Flask Routes
## Homepage
@app.route("/")
def home():
    return render_template("/index.html")

## RUN FLASK APP
if __name__ == "__main__":
    app.run(debug=True)
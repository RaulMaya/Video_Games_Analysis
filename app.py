## Dependencies
import pymongo
import json
import pandas as pd
from bson.json_util import dumps, loads
from flask import Flask, jsonify, render_template
from flask_cors import CORS, cross_origin
import plotly.express as px
import plotly

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
    query =  {'$or': [{'platform': 'PS4'},
    {'platform': 'XOne'},
    {'platform': 'Steam'}]}
    
    results = db.united.find(query)
    preferred_platforms = pd.DataFrame(results)
    preferred_platforms.head(10)

    fig = px.histogram(preferred_platforms[:15], x="name", y="user_score",
             color='platform', barmode='group',
             height=400)
    
    graph = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template("/index.html", df = graph)

## RUN FLASK APP
if __name__ == "__main__":
    app.run(debug=True)
import json
import sqlite3

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly
import plotly.express as px
from flask_jwt_extended import jwt_required
from flask_restful import Resource

# Create your connection.
cnx = sqlite3.connect("data.db")

df = pd.read_sql_query("SELECT * FROM courses", cnx)


class BarChartOne(Resource):
    @jwt_required()
    def get(self):
        arr = np.array(df.groupby("level").num_subscribers.median())
        y = []
        for i in arr:
            y.append(i)

        level = ["All Levels", "Intermediate Level", "Beginner Level", "Expert Level"]
        print(type(level))
        return {"x": level, "y": y}


class BarChartTwo(Resource):
    @jwt_required()
    def get(self):
        arr = np.array(df.groupby("subject").price.mean())
        y = []
        for i in arr:
            y.append(i)
        subject = [
            "Business Finance",
            "Graphic Design",
            "Musical Instruments",
            "Web Development",
        ]
        print(type(subject))
        return {"x": subject, "y": y}


class PieChartOne(Resource):
    @jwt_required()
    def get(self):
        coms = np.array(df["level"].value_counts(sort=True))
        print(coms)
        y = []
        for i in coms:
            print(type(float(i)))
            y.append(float(i))
        Labels = ["All Levels", "Intermediate Level", "Beginner Level", "Expert Level"]
        print(Labels)
        data = []
        for i in range(4):
            data.append({"value": y[i], "name": Labels[i]})
        return {"x": data}


class PieChartTwo(Resource):
    @jwt_required()
    def get(self):
        coms = np.array(df["is_paid"].value_counts(sort=True))
        print(coms)
        y = []
        for i in coms:
            print(type(float(i)))
            y.append(float(i))
        Labels = ["True", "False"]
        print(Labels)
        data = []
        for i in range(2):
            data.append({"value": y[i], "name": Labels[i]})
        return {"x": data}

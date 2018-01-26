##############################################
# Dependencies
##############################################
import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify, session

# Import Scikit Learn
from sklearn.linear_model import LogisticRegression

# Import Pickle
import _pickle as pickle

###############################################
# Datebase Setup
###############################################
# engine = create_engine("")

# # reflect an existing database into a new model
# Base = automap_base()
# # reflect the tables
# Base.prepare(engine, reflect=True)

# # Save reference to the table
# Passenger = Base.classes.passenger

# # Create our session (link) from Python to the DB
# session = Session(engine)

###############################################
# Flask Setup
###############################################
app = Flask(__name__)

###############################################
# Flask Routes
###############################################

# Test Route
@app.route("/")
def home():
    return("Hi!")
    
# Route for Receiving JSONs
@app.route("/practice", methods=["GET","POST"])
def practice():
    
    # Initial
    practiceData = [{}]

    # Inputs
    Initial Velocity 
    Initial Angle 
    Acceleration Due to Gravity 

    # Outputs
    Horizontal Velocity = 
    Vertical Velocity = 
    Free Fall Time = 
    Total Time = 
    Maximum Height = 
    Range = 

    # Convert to DataFrame
    practiceDF = pd.DataFrame(practiceData)
    
    # Separata "Labels" and "Data"
    labels = practiceDF["Success_Failure"].values
    data = practiceDF[["Angle","Velocity"]].values

    # Create a Logistic Model
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(data, labels, random_state=1, stratify=labels)

    from sklearn.linear_model import LogisticRegression
    classifier = LogisticRegression

    # Score the Model
    train_score = classifier.score(X_train, y_train)
    test_score = classifier.score(X_test, y_test)
    
    # Pickle
    pickle.dump(classifier, open("Classifier.sav", 'wb'))

    # Return the Data
    return(str(train_score))

# Route for Filtering JSONs
@app.route("/replay", methods=["GET","POST"])
def replay():
    
    # Replay Data
    replayData = []

    # Filtered List
    filteredData = []

    # Reload the classifier
    classifier = pickle.load(open("", ""))

    # Filter it down using the Classifier
    for x in range(len(replayData)):
        
        print(replayData[x])
        if(classifier.predict([replayData[x]["Angle"], replayData[x]["Velocity"]]) == 1):
            filteredData.append(replayData[x])

        print(len(replayData))
        print(len(filteredData))
    
    # Display only filtered Data
    return(jsonify(filteredData))

############################################
# Flask Boilerplate
############################################
if __name__ == '__main__':
    app.run(port = 9000, debug = True)
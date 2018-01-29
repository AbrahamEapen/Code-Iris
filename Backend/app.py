# Dependencies and Setup
import numpy as np
import pandas as pd
import math
import random, json

# Flask
from flask import Flask, render_template, jsonify, redirect, request, Response

# Import Scikit Learn
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# Import Pickle
import _pickle as pickle

#################################################
# Flask Setup
#################################################
app = Flask(__name__)
#################################################
# Flask Routes
#################################################

# Test Route
@app.route("/")
def home(): 
    return ("Hi!")

# Route for Generate JSONs
@app.route("/generate", methods=["GET", "POST"])
def practice():

    # Initial Data
    angle = [random.randint(1, 90) for k in range(1000)]
    velocity = [random.randint(0, 100) for k in range(1000)]
    velocity = np.array(velocity)
    angle = np.array(angle)
    gravity = 9.8
    horizontal_velocity = velocity * (np.cos(angle*math.pi)/180)
    vertical_velocity = velocity * (np.sin(angle*math.pi)/180)
    free_fall_time = (vertical_velocity/9.8)
    total_time = (2*free_fall_time)
    maximum_height = (2*vertical_velocity/(2*gravity))
    Range = ((velocity**2)*(np.sin(2*angle*3.14/180))/9.8)

    # Creating the DataFrame
    moo = pd.DataFrame({'Angle': angle,
                        'Velocity': velocity,
                        'Horizontal Velocity': horizontal_velocity,
                        'Vertical Velocity': vertical_velocity,
                        'Free Fall Time': free_fall_time,
                        'Total Time': total_time,
                        'Maximum Height': maximum_height,
                        'Range': Range
                        },
                        columns=['Angle','Velocity','Horizontal Velocity','Vertical Velocity','Free Fall Time','Total Time','Maximum_Height','Range']
                        )
    
    # Force a 'pattern' in the results columns
    moo['Result'] = np.where((moo['Range']>= 300)&(moo['Range']<=310),1,0)
    moojson = json.loads(moo.to_json(orient="records"))
 
    # Return only the jsonified version
    return jsonify(moojson)

#    # Sort Values
#    moo = moo.sort_values('Result', ascending=False)
    


# # Route for Training JSONs
# @app.route("/train", methods=["POST"])
# def train():
    
#      #ajax to send json[arrray] to train route
#      #Todo: create code that will recieve json post request
     
#      #research and test using postman

#     # Save the json array as dateframe called moo pretrained
#     # with successful, angle, velcity, and range 

#     # Separate "Labels" and "Data"
#     labels = moopretrained["Success_Failure"].values
#     data = moopretrained[["Angle", "Velocity","Range"]].values
    
#     # Create a Logistic Model
#     X_train, X_test, y_train, y_test = train_test_split(data, labels, random_state=1, stratify=labels)

#     # Model for LogistiRegression
#     classifier = LogisticRegression()
#     classifier.fit(X_train, y_train)
#     classifier.score(X_train, y_train)
#     classifier.score(X_test, y_test)

#     # classifier.predict([65, 30])
#     # classifier.predict([[12121, 23], [65,30]])
#     # newSimulation = [[12121, 23], [65,30]]
#     # success_guesses = classifier.predict([[]])
#     # newSimulation
#     # success_guesses

#     # for num in success_guesses:
#     #     if (num == 1):
#     #         print(num)
#     #         print(newSimulation[num])

#     # for x in range(len(success_guesses)):
#     #     if(success_guesses[x] == 1):
#     #         print(success_guesses[x])
#     #         print(newSimulation[x])

#         # Score the Model
#         train_score = classifier.score(X_train, y_train)
#         test_score = classifier.score(X_test, y_test)

#         # Pickle 
#         pickle.dump(classifier, open("Classifier.sav", 'wb'))

#         # Return the Data
#         return(str(train_score))

# Route for Filtering JSONs
@app.route("/replay", methods=["GET","POST"])
def replay():

    # Generate New Data (replayData)
    # Store as an array called replayData
    angle = [random.randint(1, 90) for k in range(1000)]
    velocity = [random.randint(0, 100) for k in range(1000)]
    velocity =  np.array(velocity)
    angle = np.array(angle)
    gravity = 9.8
    horizontal_velocity = velocity * (np.cos(angle*math.pi)/180)
    vertical_velocity = velocity * (np.sin(angle*math.pi)/180)
    free_fall_time = (vertical_velocity/9.8)
    total_time = (2*free_fall_time)
    maximum_height = (2*vertical_velocity/(2*gravity))
    Range = ((velocity**2)*(np.sin(2*angle*3.14/180))/9.8)

    # Creating the Dataframe
    moo = pd.DataFrame({'Angle': angle,
                        'Velocity': velocity,
                        'Horizontal Velocity': horizontal_velocity,
                        'Vertical Velocity': vertical_velocity,
                        'Free Fall Time': free_fall_time,
                        'Total Time': total_time,
                        'Maximum Height': maximum_height,
                        'Range': Range,
                        },
                        columns=['Angle','Velocity','Horizontal Velocity','Vertical Velocity','Free Fall Time','Total Time','Maximum Height','Range']
                        )

    # Force a 'pattern' in the results columns
    moo['Result'] = np.where((moo['Range']>= 300)&(moo['Range']<=310),1,0)
    moojson = json.loads(moo.to_json(orient="records"))

    # Return an array of the jsonified version
    return jsonify(moojson)

#     # Filtered List
#     filteredData = []

#     # Reload the classifier
#     classifier = pickle.load(open("Classifier.sav", 'rb'))

#     # Filter it down using the Classifier
#     for x in range(len(replayData)):

#         print(replayData[x])
#         if(classifier.predict([replayData[x]["Angle"], replayData[x]["Velocity"], replayData[x]["Range"]) == 1):
#             filteredData.append(replayData[x])

#     print(len(replayData))
#     print(len(filteredData))

#     # Display only filtered Data
#     return(jsonify(filteredData))

#################################################
# Flask Boilerplate
#################################################
if __name__ == '__main__':
    app.run(debug=True)
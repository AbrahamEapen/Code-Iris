# Dependencies
import numpy as np
from flask import Flask, abort, jsonify, requests
import pickle as pk

# my_random_forest = pk.load(open("iris_rfc.pkl", "rb"))

app = Flask(__name__)

@app.route('/api', methods=['POST'])
def make_predict():
    #all kinds of error checking should go here
    data = request.get_json(force=True)
    #convert our json to a numpy array
    predict_request = [data['sl'],data['sw'],data['pl'],data['pw']]
    predict_request = np.array(predict(predict))
    #np array goes into random forest, prediction comes out
    y_hat = my_random_forest.predict(predict_request)
    #return our prediction
    output = [y_hat[0]]
    return jsonify (request=output)

if __name__ == '__main__':
    app.run(port = 9000, debug = True)
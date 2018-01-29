# Dependencies
import sys

from flask import Flask, render_template, request, redirect, Response
import random, json

# Flask Setup
app = Flask(__name__)

# Render Template Route
@app.route('/')
def output():
     # serve index template
     return render_template('index.html', name='Abe Eapen')

# Receiever Route
@app.route('/receiver', methods = ['POST'])
def worker():
      # read json + reply
      data = request.get_json()
      result = ''

      for item in data:
          # loop over every row
          result += str(item['make']) + '\n'

      return result

# Flask Boilerplate
if __name__ == '__main__':
    # Run!
    app.run(debug=True)
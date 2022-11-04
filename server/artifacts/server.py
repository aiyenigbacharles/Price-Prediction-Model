#This is the Python Flask server which would be used as the backend for the Website


#Flask is a Python web application framework
#Jsonify is a Python script that takes csv files as input and outputs the file with the same data in a json format
#util contains all our code routines
from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response #Returns the response that contains all the locations

@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])#This form contains the element 'total_sqft' which is then converted to a float and then stored in total_sqft
    location = request.form['location']#This form contains the element 'location' and then stores it in location
    bhk = int(request.form['bhk'])#This form contains the element 'bhk' which is then converted to an integer and stored in bhk
    bath = int(request.form['bath'])#This form conatins the element 'bath' which is then converted to an integer and stored in bath

    #This function returns us the estimated prices
    response = jsonify({
        'estimated_price': util.get_estimated_price(location,total_sqft,bhk,bath)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response #Returns the response that contains all the home prices

#To return the locations in Banglore city
if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    app.run()
import pickle
import json
import numpy as np

__locations = None
__data_columns = None
__model = None

#This is a function that returns an estimated price given the locations, square foot area, bhk and bathroom
def get_estimated_price(location,sqft,bhk,bath):
    try: #We wrap it up in a try block
        loc_index = __data_columns.index(location.lower()) #loc index stands for location index
    except: #If we can't find index then we initialize it to minus 1
        loc_index = -1

    x = np.zeros(len(__data_columns))#Number of zeros should be length of data columns
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index>=0: #The specific location index will make that particular element 1 and the remaining will be 0 using a dummy one hot encoding
        x[loc_index] = 1

    return round(__model.predict([x])[0],2)#This will take an input and return an output, here we will round the float number to 2 decimal places


def load_saved_artifacts(): #This will load our saved artifacts which are the files containig our home prices and the column.json
    print("loading saved artifacts...start")
    #Both variables will be treated as global variables
    global  __data_columns
    global __locations

    with open("C:/Users/USER/Desktop/Code/IT Project/server/artifacts/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns'] #Whatever object is loaded will be converted into a dictionary
        __locations = __data_columns[3:]  #Using python index slicing to get our the beginning of our locations because our first 3 columns are sqft, bath, bhk

    global __model
    if __model is None:
        with open('C:/Users/USER/Desktop/Code/IT Project/server/artifacts/banglore_home_prices_model.pickle', 'rb') as f: #To open and read our columns.json file
            __model = pickle.load(f)
    print("loading saved artifacts...done")

def get_location_names():
    return __locations

def get_data_columns():
    return __data_columns

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('1st Phase JP Nagar',1000, 3, 3))
    print(get_estimated_price('1st Phase JP Nagar', 1000, 2, 2))
    print(get_estimated_price('Kalhalli', 1000, 2, 2)) # other location
    print(get_estimated_price('Ejipura', 1000, 2, 2))  # other location
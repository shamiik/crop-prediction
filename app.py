import numpy as np
import pickle
import pandas as pd
#from flasgger import Swagger
import streamlit as st 

from PIL import Image

#app=Flask(__name__)
#Swagger(app)

pickle_in = open("SVC_model.pkl","rb")
classifier=pickle.load(pickle_in)

#@app.route('/')
# Define the mapping of numbers to crop names
crop_mapping = {
    1: "Rice",
    2: "Maize", 3: "Jute", 4: "Cotton",
    5: "Coconut",  6: "Papaya",   7: "Orange", 8: "Apple", 9: "Muskmelon",
    10: "Watermelon", 11: "Grapes", 12: "Mango", 13: "Banana", 14: "Pomegranate", 15: "Lentil",
    16: "Blackgram", 17: "Mungbean", 18: "Mothbeans", 19: "Pigeonpeas", 20: "Kidneybeans",
    21: "Chickpea",
    22: "Coffee"
}


#@app.route('/predict',methods=["Get"])
def predict_crop_authentication(nitrogen,phosphorus,potassium,temperature,humidity,ph,rainfall):
    

    prediction=classifier.predict([[nitrogen,phosphorus,potassium,temperature,humidity,ph,rainfall]])
    print(prediction)
    return prediction



def main():
    st.title("Crop Prediction on Soil and others analysis")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Crop Prediction ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    nitrogen = st.text_input("nitrogen","Type Here")
    phosphorus = st.text_input("phosphorus","Type Here")
    potassium = st.text_input("potassium","Type Here")
    temperature = st.text_input("temperature","Type Here")
    humidity = st.text_input("humidity","Type Here")
    ph = st.text_input("ph","Type Here")
    rainfall = st.text_input("rainfall","Type Here")

    result=""
    if st.button("Predict"):
        # result=predict_crop_authentication(nitrogen,phosphorus,potassium,temperature,humidity,ph,rainfall)
        prediction_number = predict_crop_authentication(nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall)
        # Map the prediction number to the crop name
        result = crop_mapping.get(prediction_number, "Unknown Crop")  # Default to "Unknown Crop" if not found
        
    st.success('The output is {}'.format(result))
    
    if st.button("About"):
        st.text("@Shamik")
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()

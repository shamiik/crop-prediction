

import numpy as np
import pickle
import pandas as pd
import streamlit as st 

# Load the trained model
pickle_in = open("RF_classifier_model.pkl", "rb")
classifier = pickle.load(pickle_in)

# Define the mapping of numbers to crop names
crop_mapping = {
    1: "Rice",
    2: "Maize",  3: "Jute", 4: "Cotton", 5: "Coconut",
    6: "Papaya", 7: "Orange", 8: "Apple",  9: "Muskmelon",
    10: "Watermelon", 11: "Grapes",   12: "Mango",   13: "Banana",  14: "Pomegranate",  15: "Lentil",
    16: "Blackgram", 17: "Mungbean", 18: "Mothbeans", 19: "Pigeonpeas", 20: "Kidneybeans",
    21: "Chickpea",  22: "Coffee"
}

def predict_crop_authentication(nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall):
    # Prepare input data
    input_data = [[float(nitrogen), float(phosphorus), float(potassium), 
                   float(temperature), float(humidity), float(ph), float(rainfall)]]
    # Make prediction
    prediction = classifier.predict(input_data)
    return int(prediction[0])  # Ensure we return a scalar integer

def main():
    st.title("Precision Crop Recommendations Using Random Forest")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;"> SmartCrop: AI-Powered Crop Recommendations </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    
    nitrogen = st.text_input("Nitrogen", placeholder=  "Type here the value")
    phosphorus = st.text_input("Phosphorus", placeholder= "Type here the value")
    potassium = st.text_input("Potassium", placeholder="Type here the value")
    temperature = st.text_input("Temperature", placeholder="Type here the value")
    humidity = st.text_input("Humidity", placeholder= "Type here the value")
    ph = st.text_input("pH", placeholder= "Type here the value")
    rainfall = st.text_input("Rainfall", placeholder= "Type here the value")

    result = ""
    if st.button("Predict"):
        try:
            # # Get the prediction number
            # prediction_number = predict_crop_authentication(nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall)
            # # Map the prediction number to the crop name
            # result = crop_mapping.get(prediction_number, "Unknown Crop")  # Default to "Unknown Crop" if not found
            inputs = [float(nitrogen), float(phosphorus), float(potassium), float(temperature), float(humidity), float(ph), float(rainfall)]
            
            # Check if all inputs have the same value
            if len(set(inputs)) == 1:
                st.error("Please input proper values. All values cannot be identical.")
            else:
                # Get the prediction number
                prediction_number = predict_crop_authentication(nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall)
                # Map the prediction number to the crop name
                result = crop_mapping.get(prediction_number, "Unknown Crop")  # Default to "Unknown Crop" if not found
                st.success('The predicted crop is: {}'.format(result))
                
        except ValueError as e:
            st.error(f"Error in input data: {e}")
        except Exception as e:
            st.error(f"An error occurred: {e}")
    
    
with st.sidebar:
    if st.button("About"):
        st.markdown("""
        The Crop Prediction App is a smart tool designed to help farmers, agricultural specialists, and enthusiasts make informed decisions about which crops to grow based on environmental factors. By using machine learning algorithms, the app takes key agricultural inputs such as soil nutrients (nitrogen, phosphorus, potassium), climate data (temperature, humidity, rainfall), and soil pH to accurately recommend the most suitable crops for specific conditions.

        ###Key Features:
        - **Comprehensive Crop Support**: Supports predictions for 22 different crops, ensuring a wide range of options for diverse farming needs.
        - **Data-Driven**: Uses environmental parameters to predict crop suitability, offering data-driven insights to optimize yields.
        - **Simple and Intuitive Interface**: Easy to use for both seasoned farmers and those new to agriculture.
        ###Who Is It For?
        - Farmers seeking to maximize crop yield based on scientific analysis.
        - Agricultural researchers or students looking for insights into crop growth patterns.
        - Enthusiasts aiming to improve farming practices using technology.
        By integrating advanced predictive algorithms with user-friendly design, the app empowers users to make better decisions, minimize risks, and improve resource management in farming.
        """)
        
        
     
if __name__ == '__main__':
    main()


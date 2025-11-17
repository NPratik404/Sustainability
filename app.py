import streamlit as st  
import pickle 
import numpy as np  

with open('lrmodel_sus.pkl','rb') as file:
    model=pickle.load(file)

st.title('Green Tech Sustainability Predictor')
st.write('Enter the following details to predict the sustainability of a green tech company:')

carbon_emissions=st.number_input('Carbon Emissions',min_value=0.0,format="%f")
energy_output=st.number_input('Energy Output',min_value=0.0,format="%f")
renewability_index=st.number_input('Renewability Index',min_value=0.0,format="%f")
cost_efficiency=st.number_input('Cost Efficiency',min_value=0.0,format="%f")

if st.button('Predict Sustainability'):
    input_data=np.array([[carbon_emissions,energy_output,renewability_index,cost_efficiency]])
    prediction=model.predict(input_data)
    if prediction[0]==1:
        st.success('sustainable')
    else:
        st.info('not sustainable, Need to improve')
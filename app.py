import streamlit as st
import pickle
import numpy as np
import plotly
import plotly.express as px

model=pickle.load(open("Health_risk_predict.pkl","rb"))

encoders=pickle.load(open("Label_encoders.pkl","rb"))

st.title("Health Risk Predictor")

age = st.slider("Age",18,80,22)
diet = st.selectbox("Diet Quality",['Poor','Average','Good'])
exercise = st.slider("Exercise Day per Week",0,7,3)
sleep = st.slider("Sleep Hours",3,12,6)
stress = st.selectbox("Stress Level",['Low','Medium','high'])
bmi = st.number_input("BMI",10.0,40.0,22.0)
smoking = st.selectbox("Smoking",["Yes","No"])
alcohol = st.selectbox("Alcohol consumption",['Low','Medium','High'])
family_history = st.selectbox("Family History of Disease",["Yes","No"])


if st.button("Predict Risk"):
    input_data=[age,
                encoders['diet'].transform([diet])[0],
                exercise,
                sleep,
                encoders['stress'].transform([stress])[0],
                bmi,
                encoders['smoking'].transform([smoking])[0],
                encoders['alcohol'].transform([alcohol])[0],
                encoders['family_history'].transform([family_history])[0]
               ]
    prediction=model.predict([input_data])
    probs=model.predict([input_data])
    risk_label=encoders['risk_level'].inverse_transform([prediction[0]])[0]
    st.success(risk_label)

    #Bar Chart for lifestyle factors
    
    factors = {
        "Diet": encoders['diet'].transform([diet])[0],
        "Exercise":exercise,
        "Sleep":sleep,
        "Stress": encoders['stress'].transform([stress])[0],
        "BMI":bmi
    }

    bar_fig=px.bar(
        x=list(factors.keys()),
        y=list(factors.values()),
        labels={"x":"Factors","y":"value"},
        title="Your Lifestyle Factors"

    )
    st.plotly_chart(bar_fig)
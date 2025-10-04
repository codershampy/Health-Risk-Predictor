# Health-Risk-Predictor

Health-Risk-Predictor
📋 Overview

- Health-Risk-Predictor is an interactive web application that estimates an individual’s health risk score based on their lifestyle, habits, and biometric inputs. It uses machine learning to provide personalized insights and visualizations.

🔍 Key Features

User Input Interface — Users can enter features such as age, diet quality, exercise frequency, sleep hours, stress levels, BMI, etc.

Model Prediction — A trained model (stored in Health_risk_predict.pkl) processes user input and outputs a risk score or category.

Label Encoding — Categorical features are handled via label encoders stored in Label_encoders.pkl.

Interactive UI — Built with Streamlit, the app offers sliders, dropdowns, and visual feedback.

Visualization Support — Integrated with Plotly to show interactive charts (if configured in the app).

Dataset & Experimentation — The repository includes synthetic_health_data.csv and a Jupyter notebook (healthrisk.ipynb) to explore the dataset, perform EDA, and train/test the model.

🧩 Repository Structure
File / Folder	Purpose

app.py -	The main Streamlit application script

Health_risk_predict.pkl - Pre-trained ML model for risk prediction

Label_encoders.pkl -	Encoders for converting categorical inputs

synthetic_health_data.csv	- Sample / synthetic dataset used for modeling or demo

healthrisk.ipynb -	Notebook containing data analysis, training routines

requirements.txt -	Python dependencies required to run the app

🌐 Deployment

To deploy this app (e.g. to Streamlit Cloud), ensure your code is pushed to a public GitHub repository. The service will install dependencies from requirements.txt and serve the app.py script.

🎯 Use Cases & Benefits

- Helps users understand their health risk based on behavioral & biometric inputs

- Useful as a demonstration project for combining ML + web UI

- Can be extended to include more data, model improvement, or integration with health APIs

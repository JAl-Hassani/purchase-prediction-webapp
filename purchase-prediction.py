import streamlit as st
import pandas as pd
import joblib

# load model pipeline
model = joblib.load("pipeline_rf.joblib")

# add title and instructions
st.title("Purchase Prediction Model")
st.subheader("Enter customer information and submit for likelihood to purchase")

# age input form
age = st.number_input(
    label="01. Enter the customer's age",
    min_value = 18,
    max_value = 120,
    value = 35
)

# gender input form
gender = st.radio(
    label = "02. Enter the customer's gender",
    options = ["M", "F"]
)

# credit score input form
credit_score = st.number_input(
    label="03. Enter the customer's credit score",
    min_value = 0,
    max_value = 1000,
    value = 500
)

# submit inputs to model
if st.button("Submit"):
    # store inputs in data frame
    data = pd.DataFrame({"age" : [age],
                         "gender" : [gender],
                         "credit_score" : [credit_score]})

    # apply model pipeline using input data to generate prediction
    pred_proba = model.predict_proba(data)[0][1]

    # print prediction
    st.subheader(f"Based on the customer's attributes, the model predicts a purchase probability of {pred_proba: .0%}")
    
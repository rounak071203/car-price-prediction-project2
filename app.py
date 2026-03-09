import streamlit as st
import pandas as pd
import pickle as pkl

st.title("Car Price Prediction Project")
df = pd.read_csv("cleaned_data.csv")
with open("car-price-predictor.pkl", "rb") as f:pipe = pkl.load(f)
companies = sorted(df["company"].unique())
fuel_types = sorted(df["fuel_type"].unique())

col1, col2 = st.columns(2)
with col1:
    company = st.selectbox("Select company", companies)
with col2:
    names = sorted(df["name"][df["company"] == company].unique())
    name = st.selectbox("Select name", names)

col3, col4 = st.columns(2)
with col3:
    year = st.number_input("Enter year", min_value=1990, max_value=2025, value=2020, step=1)
with col4:
    fuel_type = st.selectbox("Select fuel type", fuel_types)

kms_driven = st.number_input("Enter kilometers driven", min_value=10000, value=50000, step=5000)

if st.button("Predict Price"):
    columns = ['company', 'name', 'year', 'kms_driven', 'fuel_type']
    data = [[company, name, year, kms_driven, fuel_type]]
    myinput = pd.DataFrame(data, columns=columns)
    price = pipe.predict(myinput)

    with st.container(border=True):
        st.write("**Company:**", company)
        st.write("**Name:**", name)
        st.write("**Year:**", str(year))
        st.write("**Kilometers Driven:**", str(kms_driven))
        st.write("**Fuel Type:**", fuel_type)
        st.success("Predicted price: ₹" + str(round(price[0,0])))

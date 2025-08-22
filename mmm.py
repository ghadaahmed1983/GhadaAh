import streamlit as st
import pandas as pd

st.title("Hello Streamlit")
st.write("This is my first app 🎉")

name = st.text_input("What's your name?")
age = st.slider("Please Select your Age:", 0, 100, 41)

if st.button("Say Hello"):
    if name:
        st.success(f"Welcome, {name}! 🎉 Your age is {age} !😉")
    else:
        st.error("Please enter your name first 😉")
# إضافة نص عادي
st.write("This is just a simple Streamlit demo.")

data = {
    'Name': ['John', 'Sara', 'Ali'],
    'Age': [25, 30, 22],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)
st.title("📊 Age Chart")
# Show data
st.write("### Data Table")
st.dataframe (df)
#Show bar Chart
st.write("### Age by Name")
st.bar_chart(data=df, x="Name", y="Age")

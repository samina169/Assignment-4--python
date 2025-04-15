import streamlit as st

# Title of the app
st.title("Feet to Inches Converter")

# Input for feet
feet = st.number_input("Enter feet:", min_value=0.0)

# Calculate inches when the button is pressed
if st.button("Convert to Inches"):
    # Conversion factor
    inches = feet * 12
    st.write(f"{feet} feet is equal to {inches} inches.")

import streamlit as st
import math

# Title of the app
st.title("Pythagorean Theorem Calculator")

# Input for the lengths of the two legs
a = st.number_input("Enter length of leg a (in units):", min_value=0.0)
b = st.number_input("Enter length of leg b (in units):", min_value=0.0)

# Calculate hypotenuse when the button is pressed
if st.button("Calculate Hypotenuse"):
    # Calculate hypotenuse using Pythagorean theorem
    hypotenuse = math.sqrt(a**2 + b**2)
    st.write(f"The length of the hypotenuse is {hypotenuse:.2f} units.")

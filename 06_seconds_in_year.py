import streamlit as st

# Title of the app
st.title("Seconds in Years Calculator")

# Input for the number of years
years = st.number_input("Enter number of years:", min_value=0)

# Calculate seconds when the button is pressed
if st.button("Calculate Seconds"):
    # Calculate seconds in the given number of years
    seconds = years * 365 * 24 * 60 * 60  # Assuming 1 year = 365 days
    st.write(f"There are {seconds} seconds in {years} years.")

import streamlit as st

# Title of the app
st.title("Energy Calculation using E=mc²")

# Input for mass
mass = st.number_input("Enter mass (in kg):", min_value=0.0)

# Calculate energy when the button is pressed
if st.button("Calculate Energy"):
    # Speed of light in m/s
    c = 299792458
    # Calculate energy
    energy = mass * c**2
    st.write(f"The energy is {energy} Joules.")

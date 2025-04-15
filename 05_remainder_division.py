import streamlit as st

# Title of the app
st.title("Remainder Division Calculator")

# Input for dividend and divisor
dividend = st.number_input("Enter dividend:", min_value=0)
divisor = st.number_input("Enter divisor:", min_value=1)  # Divisor should be at least 1 to avoid division by zero

# Calculate remainder when the button is pressed
if st.button("Calculate Remainder"):
    # Calculate remainder
    remainder = dividend % divisor
    st.write(f"The remainder of {dividend} divided by {divisor} is {remainder}.")

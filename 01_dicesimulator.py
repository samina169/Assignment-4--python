import streamlit as st
import random

# Title of the app
st.title("Dice Simulator")

# Button to roll the dice
if st.button("Roll the Dice"):
    # Generate a random number between 1 and 6
    dice_result = random.randint(1, 6)
    st.write(f"You rolled a {dice_result}!")

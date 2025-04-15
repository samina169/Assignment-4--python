import streamlit as st

# Title of the app
st.title("Tiny Mad Libs")

# Input fields for the Mad Libs
noun = st.text_input("Enter a noun:")
verb = st.text_input("Enter a verb:")
adjective = st.text_input("Enter an adjective:")
adverb = st.text_input("Enter an adverb:")

# Create the story when the button is pressed
if st.button("Create Mad Lib"):
    story = f"Once upon a time, a {adjective} {noun} decided to {verb} {adverb}. It was a day to remember!"
    st.write(story)

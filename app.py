import streamlit as st
import pandas as pd

st.title("Superhero Name Generator 🦸‍♂️🦸‍♀️")

# 4. Text
st.text("Use this app to create your own Superhero name!")

color = st.text_input("Enter your favorite color:")

animal = st.text_input("Enter your favorite animal:")

number = st.number_input("Enter your lucky number:")

option = st.selectbox("What's your superpower?", ["flying", "invisibility", "never spelling anything wrong"])

if st.button("I'm ready to save the world!"):
    
    st.subheader("Your Superhero Profile")
    st.text(f"Your superhero name is: {color} {animal} of {number}!")
    st.text(f"Your superpower is: {option}")

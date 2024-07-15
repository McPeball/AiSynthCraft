import streamlit as st
from aizynthfinder.interfaces import AiZynthApp

#app = AiZynthApp("config.yml")



user_input_smiles = st.text_input("SMILES", "")
# TODO: Implement visualisation of SMILES



user_input_stocks = st.selectbox(
    "Stocks",
    ("", "zinc"))



user_input_exp_pol = st.selectbox(
    "Expansion Policy",
    ("uspto", "ringbreaker"))



#st.write("**Filter Policy**")

min_time = st.slider("**Time**(minimum)", 0, 100)
import streamlit as st
from rdkit import Chem
from rdkit.Chem import Draw

# from aizynthfinder.interfaces import AiZynthApp

# app = AiZynthApp("config.yml")


user_input_smiles = st.text_input("SMILES", "")
# TODO: Implement visualisation of SMILES
if user_input_smiles != "":
    rdkit_molecule = Chem.MolFromSmiles(user_input_smiles)
    Draw.MolToFile(rdkit_molecule, "images/rdkit_molecule.png")
    st.image("images/rdkit_molecule.png")


user_input_stocks = st.selectbox("Stocks", ("", "zinc"))


user_input_exp_pol = st.selectbox("Expansion Policy", ("uspto", "ringbreaker"))


# st.write("**Filter Policy**")

min_time = st.slider("**Time**(minimum)", 0, 100)

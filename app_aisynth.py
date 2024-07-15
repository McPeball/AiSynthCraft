# from smallworld_api import SmallWorld
import streamlit as st
from aizynthfinder.interfaces import AiZynthApp
from molbloom import buy
from rdkit import Chem
from rdkit.Chem import Draw

st.title("AiSynth")
user_input_smiles = st.text_input("SMILES", "")

# TODO: add an error message for edge cases
if user_input_smiles != "":
    rdkit_molecule = Chem.MolFromSmiles(user_input_smiles)
    if rdkit_molecule is None:
        st.error("Invalid SMILES!")
    else:
        Draw.MolToFile(rdkit_molecule, "images/rdkit_molecule.png")
        st.image("images/rdkit_molecule.png")


user_input_stocks = st.selectbox("Stocks", ("", "zinc"))

# if buy(user_input_smiles) is False:

user_input_exp_pol = st.selectbox("Expansion Policy", ("uspto", "ringbreaker"))

user_input_Filter_Policy = st.selectbox("Filter Policy", ("uspto", ""))

# time_to_search = st.slider("**Time**(minutes)", 1, 120)

# max_iterations = st.slider("Max Iterations", 1, 100)

returns_first_solved_route = st.checkbox("display first solved route")

max_tree_depth = st.text_input("max tree depth")

atom_occurences = {}
st.write("**Limit atom occurences**")
carbon = st.checkbox("Carbon")
carbon_occurences = st.text_input("", value="0", key="carbon_occurences")
oxygen = st.checkbox("Oxygen")
oxygen_occurences = st.text_input("", value="0", key="oxygen_occurences")
nitrogen = st.checkbox("Nitrogen")
nitrogen_occurences = st.text_input("", value="0", key="nitrogen_occurences")

if carbon:
    atom_occurences["Carbons"] = carbon_occurences
if oxygen:
    atom_occurences["Oxygens"] = oxygen_occurences
if nitrogen:
    atom_occurences["Nitrogens"] = nitrogen_occurences

st.write("You have selected:")
for element, occurence in atom_occurences.items():
    st.write(f"{occurence} {element}")

search_button = st.button("Run Search", type="secondary")
if search_button:
    pass

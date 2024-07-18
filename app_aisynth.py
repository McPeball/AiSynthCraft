# from smallworld_api import SmallWorld
import streamlit as st
from aizynthfinder.interfaces import AiZynthApp
from molbloom import buy
from rdkit import Chem
from rdkit.Chem import Draw
import os

st.title("AiSynth")
user_input_smiles = st.text_input("**SMILES**", "")

if user_input_smiles != "":
    rdkit_molecule = Chem.MolFromSmiles(user_input_smiles)
    if rdkit_molecule is None:
        st.error("Invalid SMILES!")
    else:
        Draw.MolToFile(rdkit_molecule, "images/rdkit_molecule.png")
        st.image("images/rdkit_molecule.png")

st.write("**Stocks**")
user_input_stocks = st.checkbox("zinc")

user_input_exp_pol = st.selectbox("**Expansion Policy**", ("uspto", "ringbreaker"))

st.write("**Filter Policy**")
user_input_Filter_Policy = st.checkbox("uspto")

# time_to_search = st.slider("**Time**(minutes)", 1, 120)

# max_iterations = st.slider("Max Iterations", 1, 100)

#returns_first_solved_route = st.checkbox("display first solved route")

#max_tree_depth = st.text_input("max tree depth")


# atom_occurences = {}
# st.write("**Limit atom occurences**")
# carbon = st.checkbox("Carbon")
# carbon_occurences = st.text_input("", value="0", key="carbon_occurences")
# oxygen = st.checkbox("Oxygen")
# oxygen_occurences = st.text_input("", value="0", key="oxygen_occurences")
# nitrogen = st.checkbox("Nitrogen")
# nitrogen_occurences = st.text_input("", value="0", key="nitrogen_occurences")

# if carbon:
#     atom_occurences["Carbons"] = carbon_occurences
# if oxygen:
#     atom_occurences["Oxygens"] = oxygen_occurences
# if nitrogen:
#     atom_occurences["Nitrogens"] = nitrogen_occurences

# st.write("You have selected:")
# for element, occurence in atom_occurences.items():
#     st.write(f"{occurence} {element}")

search_button = st.button("Run Search", type="secondary")

if user_input_smiles != '' and user_input_stocks is True and len(user_input_exp_pol) > 0 and user_input_Filter_Policy is True:
    user_input_stocks = 'zinc'
    user_input_Filter_Policy = 'uspto'
    command_to_run = f"aizynthcli --config config.yml --smiles '{user_input_smiles}' --policy {user_input_exp_pol} --filter {user_input_Filter_Policy} --stocks {user_input_stocks}"

    if search_button:
        os.system(command_to_run)

    #TODO: Implement a spinner
    
    #with st.spinner("waiting"):
    #    response = call_streamlit('./trees.json', )
    
    while os.path.exists('./trees.json') is False:
        st.spinner('Processing...')
        if os.path.exists('./trees.json'):
            st.success('Run completed. :)')


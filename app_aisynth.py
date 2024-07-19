import pandas as pd
from aizynthfinder.reactiontree import ReactionTree
import streamlit as st
from molbloom import buy
from rdkit import Chem
from rdkit.Chem import Draw
import os
from pathlib import Path
import shutil

st.title("AiSynthCraft")

def disable():
    st.session_state.disabled = True

if "disabled" not in st.session_state:
    st.session_state.disabled = False

user_input_smiles = st.text_area('Enter SMILES', '')

if user_input_smiles != "":
    all_smiles = user_input_smiles.split()
    if len(all_smiles) == 1:
        rdkit_molecule = Chem.MolFromSmiles(user_input_smiles)
        if rdkit_molecule is None:
            st.error(f"Invalid SMILES: {user_input_smiles}")
        else:
            with open('smiles.txt', 'w') as smiles_file:
                for smiles in all_smiles:
                    smiles_file.write(f"{smiles}\n")
                smiles_file.write('C')
    else:
        all_rdkit_molecules = []
        for smiles in all_smiles:
            rdkit_molecule = Chem.MolFromSmiles(smiles)
            if rdkit_molecule is None:
                st.error(f'Invalid SMILES: {smiles}')
            else:
                all_rdkit_molecules.append(rdkit_molecule)
        
        with open('smiles.txt', 'w') as smiles_file:
            for smiles in all_smiles:
                smiles_file.write(f"{smiles}\n")

        img = Draw.MolsToGridImage(mols=all_rdkit_molecules, molsPerRow=3, subImgSize=(200,200))
        img.save("images/rdkit_molecule.png")
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

search_button = st.button("Run Search", type="secondary", disabled=st.session_state.disabled, key='search_button', on_click=disable)

if user_input_smiles != '' and user_input_stocks is True and len(user_input_exp_pol) > 0 and user_input_Filter_Policy is True:
    user_input_stocks = 'zinc'
    user_input_Filter_Policy = 'uspto'
    command_to_run = f"aizynthcli --config config.yml --smiles smiles.txt --policy {user_input_exp_pol} --filter {user_input_Filter_Policy} --stocks {user_input_stocks}"

    if search_button:

        location_of_png_files = '.'
        dir_list = os.listdir(location_of_png_files)
        for file in dir_list:
            if Path(file).suffix == '.png':
                os.remove(f'{location_of_png_files}/{file}')
            if file == 'output.json.gz':
                os.remove(file)
            if 'molecule' in file:
                shutil.rmtree(file, ignore_errors=True)

        os.system(command_to_run)

        with st.spinner('waiting'):
            while os.path.exists('output.json.gz') is False:
                continue
            if os.path.exists('output.json.gz'):
                st.success('Run completed. :)')
                data = pd.read_json("output.json.gz", orient="table")
                all_trees = data.trees.values
                for i in range(len(all_trees)):
                    os.mkdir(f'molecule{i + 1}')
                    trees_for_first_target = all_trees[i]
                    for itree, tree in enumerate(trees_for_first_target):
                        imagefile = f"molecule{i + 1}/route{itree:03d}.png"
                        ReactionTree.from_dict(tree).to_image().save(imagefile)
                    
                    st.write(f'molecule{i + 1}')
                    st.image(f'molecule{i + 1}/route000.png')

    st.session_state.disabled = False
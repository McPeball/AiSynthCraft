import os

import streamlit as st

from src.checking_files_and_folders import (
    check_data,
    check_images,
    remove_previous_output_files_and_folders,
)
from src.display_output import save_synthetic_routes
from src.process_smiles import get_smiles_and_display_images

# Web app title
st.title("AiSynthCraft")


# Initialise state for buttons
def disable():
    st.session_state.disabled = True


if "disabled" not in st.session_state:
    st.session_state.disabled = False

# Check for pre-existing folders and files
check_images()
check_data()

# Obtain and process user inputed SMILES
user_input_smiles = st.text_area("Enter SMILES", "")

all_smiles = get_smiles_and_display_images(user_input_smiles=user_input_smiles)
smiles_indexes = {}
if all_smiles is not None:
    for smiles in all_smiles:
        smiles_indexes[all_smiles.index(smiles) + 1] = smiles

# Choose molecule stock library
st.write("**Stocks**")
user_input_stocks = st.checkbox("zinc")

# Choose retrosynthetic algorithm(s)
user_input_exp_pol = st.selectbox(
    "**Expansion Policy**", ("uspto", "ringbreaker")
)

# Choose policy for filtering molecules
st.write("**Filter Policy**")
user_input_Filter_Policy = st.checkbox("uspto")

# Set up and run search algorithm for synthetic routes
search_button = st.button(
    "Run Search",
    type="secondary",
    disabled=st.session_state.disabled,
    key="search_button",
    on_click=disable,
)

if (
    user_input_smiles != ""
    and user_input_stocks is True
    and len(user_input_exp_pol) > 0
    and user_input_Filter_Policy is True
):
    user_input_stocks = "zinc"
    user_input_Filter_Policy = "uspto"
    aizynth_config = "data/config.yml"
    smiles_file = "smiles.txt"
    command_to_run = f"aizynthcli --config {aizynth_config} --smiles {smiles_file} --policy {user_input_exp_pol} --filter {user_input_Filter_Policy} --stocks {user_input_stocks}"

    if search_button:

        remove_previous_output_files_and_folders()

        with st.spinner("waiting"):
            os.system(command_to_run)

            while os.path.exists("output.json.gz") is False:
                continue
            if os.path.exists("output.json.gz"):
                st.success("Run completed. :)")
                save_synthetic_routes()

    st.write("Best Synthetic Route for:")
    option = st.selectbox("Select molecule", all_smiles)

    for key, value in smiles_indexes.items():
        if value == option:
            st.image(f"molecule{int(key)}/route000.png")

    st.session_state.disabled = False

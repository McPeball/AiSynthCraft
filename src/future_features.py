import streamlit as st

# Future enhancements to the web app


def add_search_time():
    time_to_search = st.slider("**Time**(minutes)", 1, 120)

    return time_to_search


def add_max_iterations():
    max_iterations = st.slider("Max Iterations", 1, 100)

    return max_iterations


def add_display_first_solved_route():
    display_first_solved_route = st.checkbox("display first solved route")

    return display_first_solved_route


def add_max_tree_depth():
    max_tree_depth = st.text_input("max tree depth")

    return max_tree_depth


def add_atom_occurences():
    atom_occurences = {}
    st.write("**Limit atom occurences**")
    carbon = st.checkbox("Carbon")
    carbon_occurences = st.text_input("", value="0", key="carbon_occurences")
    oxygen = st.checkbox("Oxygen")
    oxygen_occurences = st.text_input("", value="0", key="oxygen_occurences")
    nitrogen = st.checkbox("Nitrogen")
    nitrogen_occurences = st.text_input(
        "", value="0", key="nitrogen_occurences"
    )

    if carbon:
        atom_occurences["Carbons"] = carbon_occurences
    if oxygen:
        atom_occurences["Oxygens"] = oxygen_occurences
    if nitrogen:
        atom_occurences["Nitrogens"] = nitrogen_occurences

    st.write("You have selected:")
    for element, occurence in atom_occurences.items():
        st.write(f"{occurence} {element}")

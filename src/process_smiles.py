import streamlit as st
from rdkit import Chem
from rdkit.Chem import Draw


def get_smiles_and_display_images(user_input_smiles):
    if user_input_smiles != "":
        all_smiles = user_input_smiles.split()
        if len(all_smiles) == 1:
            rdkit_molecule = Chem.MolFromSmiles(user_input_smiles)
            if rdkit_molecule is None:
                st.error(f"Invalid SMILES: {user_input_smiles}")
            else:
                with open("smiles.txt", "w") as smiles_file:
                    for smiles in all_smiles:
                        smiles_file.write(f"{smiles}\n")
                    smiles_file.write("C")
                img = Draw.MolToImage(rdkit_molecule)
                img.save("images/rdkit_molecule.png")
                st.image("images/rdkit_molecule.png")
        else:
            all_rdkit_molecules = []
            for smiles in all_smiles:
                rdkit_molecule = Chem.MolFromSmiles(smiles)
                if rdkit_molecule is None:
                    st.error(f"Invalid SMILES: {smiles}")
                else:
                    all_rdkit_molecules.append(rdkit_molecule)

            with open("smiles.txt", "w") as smiles_file:
                for smiles in all_smiles:
                    smiles_file.write(f"{smiles}\n")

            img = Draw.MolsToGridImage(
                mols=all_rdkit_molecules, molsPerRow=3, subImgSize=(200, 200)
            )
            img.save("images/rdkit_molecule.png")
            st.image("images/rdkit_molecule.png")

        return all_smiles

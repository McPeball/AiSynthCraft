from rdkit import Chem
from rdkit.Chem import Draw
import json

json_file = json.loads('./trees.json')
smiles = json_file.get("smiles")
rdkit_molecule = Chem.MolFromSmiles(smiles)
Draw.MolToFile(rdkit_molecule, "images/rdkit_molecule.png")
#st.image("images/rdkit_molecule.png")

# AiSynthCraft
a web app which acts as a user interface to AiZynthFinder for chemists.

# Installation
## 1. Clone the repository
```sh
git clone git@github.com:McPeball/AiSynthCraft.git
```

## 2. Create the virtual environment with Conda
```sh
conda create "python>=3.9,<3.11" -n aizynth-env -y
```

## 3. Activate the virtual environment
```sh
conda activate aizynth-env
```

## 4. Navigate to the AiSynthCraft folder
```sh
cd AiSynthCraft
```

## 5. Install required Python libraries
```sh
pip install -r requirements.txt
```

## 6. Create a 'data' folder to contain the model files
```sh
mkdir data
```

## 7. Navigate to the 'data' folder
```sh
cd data
```

## 8. Run 'download_public_data' to download the model files
```sh
download_public_data .
```

## 9. Exit 'data' folder
```sh
cd ..
```

## 10. Run the web app
```sh
streamlit run app_aisynth.py
```


# IMPORTANT THINGS TO NOTE
1. Setting up this repository assumes that the user has Anaconda/Mamba installed on the computer.

# Issues?
Please open an issue in the repository. (See top left of the webpage, under "Issues".)
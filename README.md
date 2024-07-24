# AiSynthCraft
a web app which acts as a user interface to AiZynthFinder for chemists.

## Prerequisites
Before you start, ensure you have met the following requirements:
* You have linux os or a subsystem for linux installed such as wsl.
* You have installed anaconda/mamba.

A guide on how to install anaconda can be found [here](https://docs.anaconda.com/anaconda/install/linux/)

## Installation
### 1. Clone the repository
```sh
git clone git@github.com:McPeball/AiSynthCraft.git
```

### 2. Create the virtual environment with Conda
```sh
conda create "python>=3.9,<3.11" -n aizynth-env -y
```

### 3. Activate the virtual environment
```sh
conda activate aizynth-env
```

### 4. Navigate to the AiSynthCraft folder
```sh
cd AiSynthCraft
```

### 5. Install required Python libraries
```sh
pip install -r requirements.txt
```

### 6. Run the web app
```sh
streamlit run app_aisynth.py
```

## Issues?
Please open an issue in the repository. (See top left of the webpage, under "Issues".)
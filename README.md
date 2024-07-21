# AiSynthCraft
a web app which acts as a user interface to AiZynthFinder for chemists.

# Installation
## 1. Clone the repository
```sh
git clone git@github.com:McPeball/AiSynthCraft.git
```

## 2. Create the virtual environment with Conda
```sh
conda create "python>=3.9,<3.11" -n aizynth-env
```

## 3. Activate the virtual environment
```sh
conda activate aizynth-env
```

## 4. Install required Python libraries
```sh
pip install -r requirements.txt
```

## 5. Navigate to the AiSynthCraft folder
```sh
cd AiSynthCraft
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

## 9. 

```sh
pip install -r requirements.txt
```

# Usage
```sh
usage: main.py [-h] --fastq FASTQ --sdf SDF --excel_file EXCEL_FILE [--output OUTPUT]

options:
  -h, --help            show this help message and exit
  --fastq FASTQ         (Required) E.g. 112_R2_001.fastq.gz
  --sdf SDF             (Required) E.g. Crick_bb1_bb2_bb3.sdf
  --excel_file EXCEL_FILE
                        (Required) E.g. BBs_with_oligo_codes.xlsx
  --output OUTPUT       (Optional) Default: data.csv
```

# Running
Run

```sh
python main.py --fastq <filename>.fastq.gz --sdf <filename>.sdf --excel_file <filename>.xlsx
```

# IMPORTANT THINGS TO NOTE
1. The FASTQ file is to be in the format of <filename>.fastq.gz.
2. Each molecule in the SDF file contains a SMILES string.
3. The code is written in a way that adapts to the "BBs_with_oligo_codes.xlsx" file. If an Excel file with different columns is used instead, the code will not work.

# Issues?
Please open an issue in the repository. (See top left of the webpage, under "Issues".)
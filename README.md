# AiSynthCraft
a web app which acts as a user interface to AiZynthFinder for chemists.

## create conda env
conda create "python>=3.9,<3.11" -n aizynth-env;

## activate conda env
conda activate aizynth-env

## install aizynthfinder
python -m pip install aizynthfinder

## get data sets
download_public_data .

## install aizynth dependcy
pip install route_distances

## needed for greenlet
brew install graphviz or conda install conda-forge::graphviz

## install greenlet package
pip install greenlet

## install tensorflow
pip install tensorflow

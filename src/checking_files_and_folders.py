import os
import shutil
from pathlib import Path

import streamlit as st

from tool_functions import check_file_or_folder_exists


def check_images():
    check_images_folder = check_file_or_folder_exists("./images")
    if check_images_folder is False:
        os.mkdir("./images")


def check_data():
    check_data_folder = check_file_or_folder_exists("./data")
    model_files = [
        "./data/uspto_model.onnx",
        "./data/uspto_templates.csv.gz",
        "./data/uspto_ringbreaker_model.onnx",
        "./data/uspto_ringbreaker_templates.csv.gz",
        "./data/uspto_filter_model.onnx",
        "./data/zinc_stock.hdf5",
    ]
    if check_data_folder is False:
        os.mkdir("./data")

    with st.spinner("downloading model files..."):
        for file in model_files:
            check_model_file = check_file_or_folder_exists(file)
            if check_model_file is False:
                os.chdir("./data")
                os.system("download_public_data .")
                os.chdir("../")
                break


def remove_previous_output_files_and_folders():
    location_of_png_files = "."
    dir_list = os.listdir(location_of_png_files)
    for file in dir_list:
        if Path(file).suffix == ".png":
            os.remove(f"{location_of_png_files}/{file}")
        if file == "output.json.gz":
            os.remove(file)
        if "molecule" in file:
            shutil.rmtree(file, ignore_errors=True)

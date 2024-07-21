from pathlib import Path


def check_file_or_folder_exists(folder_path):
    obj = Path(folder_path)

    return obj.exists()

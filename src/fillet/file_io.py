import os
import sys
import hashlib
import subprocess
from pathlib import Path


SCRIPT_DIR = Path(sys.executable).parent if getattr(sys, "frozen", False) else Path(__file__).resolve().parent

SEVEN_ZIP_7Z_EXE = os.path.normpath("C:/Program Files/7-Zip/7z.exe")


def get_sha_256_hash(file_path: str) -> str:
    sha256 = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                sha256.update(chunk)
        return sha256.hexdigest()
    except FileNotFoundError:
        return f"File not found: {file_path}"


def get_all_files_in_tree(directory: str) -> list[str]:
    file_list = []
    for root, _, files in os.walk(directory):
        for file in files:
            file_list.append(os.path.join(root, file))
    return file_list


def is_current_running_script_an_exe() -> bool:
    return getattr(sys, "frozen", False)


def remove_empty_directories_in_directory_tree(directory: str):
    for root, dirs, _ in os.walk(directory, topdown=False):
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            if not os.listdir(dir_path):
                os.rmdir(dir_path)


def remove_directory_from_zip_file(zip_file: str, directory: str):
    if not os.path.isfile(SEVEN_ZIP_7Z_EXE):
        raise RuntimeError('7zip is not installed, please install it from "https://www.7-zip.org/download.html"')

    command = [SEVEN_ZIP_7Z_EXE, 'd', zip_file, f"{directory}"]
    subprocess.run(command, check=True)
    print(f'Removed directory "{directory}" from the ZIP file.')


def get_files_in_directory(directory: str) -> list[str]:
    return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]


def get_directories_in_directory(directory: str) -> list[str]:
    return [d for d in os.listdir(directory) if os.path.isdir(os.path.join(directory, d))]

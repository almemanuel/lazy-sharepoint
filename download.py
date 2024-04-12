from office365_api import SharePoint
import re
import sys
from pathlib import PurePath
from office365.sharepoint.files.file import File

# you can adaptate this for your neceseties
FOLDER_NAME = sys.argv[1]
FOLDER_DEST = sys.argv[2]
FILE_NAME = sys.argv[3]
FILE_NAME_PATTERN = sys.argv[4]


def save_file(file_n:str, file_obj:File.content) -> None:
    """Save a file on the destination directory

    Args:
        file_n (str): file name
        file_obj (File.content): file content
    """
    file_dir_path = PurePath(FOLDER_DEST, file_n)
    with open(file_dir_path, 'wb') as f:
        f.write(file_obj)


def get_file(file_n:str, folder:str) -> None:
    """Get a file from SharePoint

    Args:
        file_n (str): file name on SharePoint
        folder (str): file folder of the file on SharePoint
    """
    file_obj = SharePoint().download_file(file_n, folder)
    save_file(file_n, file_obj)


def get_files(folder:str) -> None:
    """Get all file in a folder on SharePoint

    Args:
        folder (str): folder name
    """
    files = SharePoint()._get_files_list(folder)
    for file in files:
        get_file(file.name, folder)


def get_files_by_pattern(pattern:str, folder:str) -> None:
    """Search for a file by pattern name

    Args:
        pattern (str): pattern to search
        folder (str): folder to try search a file
    """
    files_list = SharePoint()._get_files_list(folder)
    for file in files_list:
        if re.search(pattern, file.name):
            get_file(file.name, folder)


if __name__ == '__main__':
    if FILE_NAME != 'None':
        get_file(FILE_NAME, FOLDER_NAME)
    elif FILE_NAME_PATTERN != 'None':
        get_files_by_pattern(FILE_NAME_PATTERN, FOLDER_NAME)
    else:
        get_files(FOLDER_NAME)
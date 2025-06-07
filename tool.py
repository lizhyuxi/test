# add some tool functions here
import os
def get_file_path(file_name: str, directory: str = "data") -> str:
    """
    Get the full path of a file in the specified directory.

    Args:
        file_name (str): The name of the file.
        directory (str): The directory where the file is located. Defaults to "data".
    Returns:
        str: The full path to the file.
    """
    return os.path.join(directory, file_name)

def ensure_directory_exists(directory: str) -> None:
    """
    Ensure that the specified directory exists. If it does not exist, create it.
    
    Args:
        directory (str): The directory to check or create.
    """
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Directory '{directory}' created.")
    else:
        print(f"Directory '{directory}' already exists.")

def list_files_in_directory(directory: str) -> list:
    """
    List all files in the specified directory.
    
    Args:
        directory (str): The directory to list files from.
        
    Returns:
        list: A list of file names in the directory.
    """
    if not os.path.exists(directory):
        print(f"Directory '{directory}' does not exist.")
        return []
    
    return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
# laotie 666

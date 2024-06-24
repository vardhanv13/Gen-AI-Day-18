import os
def create_directory(directory):
    try :
        os.mkdir(directory)
        print(f'Directory {directory} created successfully')
    except PermissionError:
        print(f"Permission denied to create the directory {directory} ")
    except OSError as e :
        print(f"Error: {e}")
def list_files_in_directory(directory):
    try:
        files = os.listdir(directory)
        files = [f for f in files if os.path.isfile(os.path.join(directory, f))]
        if files:
            print(f"Files in {directory}:")
            for file in files:
                print(file)
        else:
            print(f"No files exist in the directory {directory}.")
    except FileNotFoundError :
        print(f"The directory {directory} does not exist.")
    except PermissionError:
        print(f"Permission denined to access the directory {directory} ")

directory = "Python"
create_directory(directory)
list_files_in_directory(directory)

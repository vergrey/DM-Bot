import logging
import os
import shutil
import sys

import pyzipper


def copy_folders(destination, folders):
    current_directory = os.path.dirname(os.path.abspath(__file__))
    source_path = os.path.join(current_directory, "Code.DM-Bot")

    for folder in folders:
        source_folder = os.path.join(source_path, folder)
        destination_folder = os.path.join(destination, folder)
        
        if os.path.exists(destination_folder):
            shutil.rmtree(destination_folder)
        
        shutil.copytree(source_folder, destination_folder)

def zip_folder(folder_path, output_path, password, compression=pyzipper.ZIP_DEFLATED, encryption=pyzipper.WZ_AES):
    parent_folder = os.path.dirname(folder_path)
    contents = os.walk(folder_path)
    
    # Инициализация логгера
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    
    try:
        with pyzipper.AESZipFile(output_path, 'w', compression=compression, encryption=encryption) as zip_file:
            zip_file.setpassword(password)
            
            for root, folders, files in contents:
                for folder_name in folders:
                    absolute_path = os.path.join(root, folder_name)
                    relative_path = os.path.relpath(absolute_path, parent_folder)
                    logging.info(f"Adding '{absolute_path}' to archive.")
                    zip_file.write(absolute_path, relative_path)

                for file_name in files:
                    absolute_path = os.path.join(root, file_name)
                    relative_path = os.path.relpath(absolute_path, parent_folder)
                    logging.info(f"Adding '{absolute_path}' to archive.")
                    zip_file.write(absolute_path, relative_path)

        logging.info(f"'{output_path}' created successfully.")

    except FileNotFoundError as e:
        logging.error(f"File or directory not found: {e}")
        sys.exit(1)
    except pyzipper.PyZipperError as e:
        logging.error(f"PyZipper error: {e}")
        sys.exit(1)
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    destination_folder = "DM-Bot"
    output_zip_name = destination_folder + ".zip"
    password = b"1Ei2ttDIBadNmDHqh3HRIWpipnxh7DwNM"
    
    folder1 = "templates"
    folder2 = "static"
    
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    
    copy_folders(destination_folder, [folder1, folder2])
    
    zip_folder(destination_folder, output_zip_name, password)
    #pyminizip.compress(destination_folder, None, output_zip_name, password, 0)
    
    print(f"Selected folders are copied to {destination_folder} and compressed into {output_zip_name} with encryption")
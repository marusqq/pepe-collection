
import os

pepe_dir = os.getcwd().split('/')[:-1]
pepe_dir.append('pepes')
pepe_dir = "/".join(pepe_dir) + '/'

def get_list_of_files(dir):
    '''https://thispointer.com/python-how-to-get-list-of-files-in-directory-and-sub-directories/'''
    # create a list of file and sub directories 
    # names in the given directory 
    list_of_files = os.listdir(dir)
    all_files = list()
    # Iterate over all the entries
    for entry in list_of_files:
        # Create full path
        full_path = os.path.join(dir, entry)
        # If entry is a directory then get the list of files in this directory 
        if os.path.isdir(full_path):
            all_files = all_files + get_list_of_files(full_path)
        else:
            all_files.append(full_path)
                
    return all_files

print(
    get_list_of_files(pepe_dir))


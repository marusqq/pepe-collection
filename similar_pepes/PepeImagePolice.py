#!/usr/bin/env python
# -*- coding: UTF-8 -*-
__author__ = "Marius Pozniakovas"
__email__ = "pozniakovui@gmail.com"
"""pepe image checker class
    most of the code taken from
    cw-somil @https://github.com/cw-somil/Duplicate-Remover/blob/master/DuplicateRemover.py"""

import os
from PIL import Image
import imagehash

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


class PepeImagePolice:
    
    def __init__(self, images_dir, hash_size = 20):
        self.images_dir = images_dir
        self.hash_size = hash_size

    def find_duplicates(self, delete=False):
        """
        Find and delete duplicates
        """

        images = get_list_of_files(self.images_dir)
        hashes = {}
        duplicates = []
        for image in images:
            with Image.open(image) as img:
                temp_hash = imagehash.average_hash(img, self.hash_size)
                if temp_hash in hashes:
                    duplicates.append(image)
                else:
                    hashes[temp_hash] = image

        if len(duplicates):
            if delete:
                for duplicate in duplicates:                
                    os.remove(os.path.join(duplicate))


        
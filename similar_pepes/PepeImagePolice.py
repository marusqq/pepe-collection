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
import numpy as np
import itertools

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
                    os.remove(duplicate)

    def find_similar(self, similarity=95, delete=False):
        
        images = get_list_of_files(self.images_dir)
        threshold = 1 - similarity/100
        diff_limit = int(threshold*(self.hash_size**2))

        image_combinations = list(
            itertools.combinations(
                images, 2
            )
        )

        for image_combo in image_combinations:
        
            with Image.open(image_combo[0]) as img:
                hash1 = imagehash.average_hash(img, self.hash_size).hash
        
            with Image.open(image_combo[1]) as img:
                hash2 = imagehash.average_hash(img, self.hash_size).hash
                
                if np.count_nonzero(hash1 != hash2) <= diff_limit:
                    print("{} image found {}% similar to {}".format(
                        image_combo[0],similarity,image_combo[1])
                    )
        


        

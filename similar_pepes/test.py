#https://github.com/cw-somil/Duplicate-Remover/blob/master/DuplicateRemover.py
import os
import imagehash
from PIL import Image
import numpy as np

location_other_imgs = os.getcwd() + '/images'
location1_image = os.getcwd() + '/smug.jpg'

print(location_other_imgs)
print(location1_image)

hash_size = 8
similarity = 85

fnames = os.listdir(
    os.getcwd() + '/images')
threshold = 1 - similarity / 100
diff_limit = int(threshold*(hash_size**2))

with Image.open(location1_image) as img:
    hash1 = imagehash.average_hash(img, hash_size).hash

for image in fnames:
    with Image.open(os.path.join(location_other_imgs,image)) as img:
        hash2 = imagehash.average_hash(img, hash_size).hash
        
        if np.count_nonzero(hash1 != hash2) <= diff_limit:
            print("{} image found {}% similar to {}".format(image,similarity,location1_image))
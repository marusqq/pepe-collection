#!/usr/bin/env python
# -*- coding: UTF-8 -*-
__author__ = "Marius Pozniakovas"
__email__ = "pozniakovui@gmail.com"
"""main"""

import PepeImagePolice
from os import getcwd

pepe_dir = getcwd().split('/')[:-1]
pepe_dir.append('pepes')
pepe_dir = "/".join(pepe_dir) + '/'

police = PepeImagePolice.PepeImagePolice(
    images_dir=pepe_dir,
    hash_size=30
)

police.find_similar(
    delete=False,
)

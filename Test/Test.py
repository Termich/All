
import os

import shutil, os


def remove_folder_contents(path):
    shutil.rmtree(path)
    os.makedirs(path)


remove_folder_contents('Git\All\Test')
 
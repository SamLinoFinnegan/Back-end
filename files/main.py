__winc_id__ = 'ae539110d03e49ea8738fd413ac44ba8'
__human_name__ = 'files'

import os
import zipfile


zip_path = os.path.join(os.getcwd(),os.path.basename("data.zip"))
cache_path = os.path.join(os.getcwd(),os.path.basename("cache"))

print(cache_path)

def clean_cache():
    
    if os.path.exists(cache_path):
        if len(os.listdir(cache_path)) > 0:
            for file in os.listdir(cache_path):
                file_path = os.path.join(cache_path, file)
                os.remove(file_path)
    else:
        os.mkdir(cache_path)


def cache_zip(zip, cache):
    with zipfile.ZipFile(zip, "r") as zip_ref:
        zip_ref.extractall(cache)


def cached_files():
    list_of_paths = []
    if os.path.exists(cache_path):
        for file in os.listdir(cache_path):
            if os.path.isfile(os.path.join(cache_path, file)):
                list_of_paths.append(os.path.abspath(os.path.join(cache_path , file)))
    return list_of_paths


def find_password(path_list):
    for path in path_list:
        for file in open(path):
            if "password" in file:
                password = file.replace("password: ", "").strip()
                return password
    else:
        return "No password was found!"



clean_cache()
cache_zip(zip_path, cache_path)
cached_files()
find_password(cached_files())


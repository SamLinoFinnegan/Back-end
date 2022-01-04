__winc_id__ = 'ae539110d03e49ea8738fd413ac44ba8'
__human_name__ = 'files'

import os
import zipfile


zip_path = os.path.basename("data.zip")
cache_path = os.path.basename("cache")


def clean_cache():
    folder = "cache"
    if os.path.exists(folder):
        if len(os.listdir(folder)) > 0:
            for file in os.listdir(folder):
                os.remove(folder + "/" + file)
    else:
        parent_dir = os.getcwd()
        path = os.path.join(parent_dir, folder)
        os.mkdir(path)


def cache_zip(zip, cache):
    with zipfile.ZipFile(zip, "r") as zip_ref:
        zip_ref.extractall(cache)


def cached_files():
    folder = "cache"
    parent_dir = os.getcwd()
    path = os.path.join(parent_dir, folder)
    list_of_paths = []
    if os.path.exists(path):
        for file in os.listdir(path):
            if os.path.isfile(os.path.join(path, file)):
                list_of_paths.append(os.path.abspath(path + "/" + file))
    return list_of_paths


def find_password(path_list):
    for path in path_list:
        for file in open(path):
            if "password" in file:
                password = file.replace("password: ", "").strip()
                return password
    else:
        return "No password was found!"


os.chdir("C:/Users/Bernard/Desktop/Winc_Academy/vscode/Back-end/files")


clean_cache()
cache_zip(zip_path, cache_path)
cached_files()
print(find_password(cached_files()))

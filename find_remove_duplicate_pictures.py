#!/usr/bin/python3
#Author: Tyler Laudenslager
#        B.S Computer Science / Software Development
#
#Date: 5/19/2022
#Purpose: Detect and Remove Duplicate Picture Files Across A Directory - Recursive Search
#WARNING!!!
#Note: This will remove / modify picture files on your computer


import os
import sys

def find_duplicates(path) -> dict():
    all_files = dict()
    for item in os.listdir(path):
        if os.path.isdir(path + "/" + item):
            for file_name, locations in find_duplicates(path + "/" + item).items():
                if file_name in all_files:
                    all_files[file_name] += locations
                else:
                    all_files[file_name] = locations
        else:
            item = item.lower()
            #https://stackoverflow.com/questions/889333/how-to-check-if-a-file-is-a-valid-image-file#902779
            if item.endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
                if item in all_files:
                    all_files[item].append(path)
                else:
                    all_files[item] = [path]
            else:
                continue
    return all_files

def record_n_remove_duplicates(duplicates_found):
    path_to_file = f"{sys.argv[1]}/duplicates_found.txt"
    f = open(path_to_file, 'w')
    print(f"Searching Location -> {sys.argv[1]}", file=f)
    print(file=f)
    print(f"Duplicate Files Found -> {len(duplicates_found)} Files", file=f)
    for duplicate_file, locations in duplicates_found:
        if len(locations) > 1:
            print(file=f)
            print(f"Duplicate File: {duplicate_file}", file=f)
            print("-"*40, file=f)
            print("Locations Found:", file=f)
            print(*['\t'+x for x in sorted(locations, key=lambda x : len(x))], sep="\n", file=f)
            for file_location in sorted(locations, key=lambda x : len(x))[1:]:
                if os.path.exists(file_location):
                    os.remove(file_location + "/" + duplicate_file)
                    if os.path.isdir(file_location) and len(os.listdir(file_location)) == 0:
                        os.rmdir(file_location)
    f.close()
    print(f"Text file {path_to_file} successfully created!")
    print(f"Duplicate pictures in {sys.argv[1]} have been cleaned up!")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} path_to_directory -> example {sys.argv[0]} C:/Pictures")
    else:
        record_n_remove_duplicates(find_duplicates(sys.argv[1]).items())

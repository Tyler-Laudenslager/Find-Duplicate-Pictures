#!/usr/bin/python3
#Author: Tyler Laudenslager
#        B.S Computer Science / Software Development
#
#Date: 5/19/2022
#Purpose: Detect Duplicate Pictures Across A Directory - Recursive Search
#Note: No deletion / modification of any files on your system
#

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


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} path_to_directory -> example C:/Pictures")
    else:
        print()
        duplicates_found = find_duplicates(sys.argv[1]).items()
        print(f"Duplicate Files Found -> {len(duplicates_found)} Files")
        for duplicate_file, locations in duplicates_found:
            if len(locations) > 1:
                print()
                print(f"Duplicate File: {duplicate_file}")
                print("-"*40)
                print("Locations Found:")
                print(*['\t'+x for x in sorted(locations, key=lambda x : len(x))], sep="\n")

                

#Author: Tyler Laudenslager
#        B.S Computer Science / Software Development
#
#Date: 5/19/2022
#Purpose: Detect Duplicate Pictures Across A Directory - Recursive Search
#
#Programmed On Computer Using Solar Energy - Green Code

import os
import sys

def find_duplicates(path):
    all_files = dict()
    for item in os.listdir(path):
        if os.path.isdir(path + "/" + item):
            for file_name, locations in find_duplicates(path + "/" + item).items():
                if file_name in all_files:
                    all_files[file_name] += locations
                else:
                    all_files[file_name] = [*locations]
        else:
            #https://stackoverflow.com/questions/889333/how-to-check-if-a-file-is-a-valid-image-file#902779
            if item.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
                if item.lower() in all_files:
                    all_files[item.lower()].append(path)
                else:
                    all_files[item.lower()] = [path]
            else:
                continue
    return all_files


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} path_to_directory -> example C:/Pictures")
    else:
        print()
        print("Duplicate Files Found")
        for duplicate_file, locations in find_duplicates(sys.argv[1]).items():
            if len(locations) > 1:
                print("="*20)
                print(duplicate_file)
                print("-"*20)
                print("Found in Locations Listed Below")
                print(*['\t'+x for x in locations], sep="\n")
                print("="*20)

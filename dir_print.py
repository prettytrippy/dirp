#!/usr/bin/env python3

import os
import sys

def directory_info(dir_name, prefix=''):
    if not os.path.exists(dir_name):
        return f"{dir_name} does not exist, dumbfuck.\n"
    
    dir_name = os.path.abspath(dir_name)
    result = f"{prefix}{os.path.basename(dir_name)}/\n"
    files_and_dirs = os.listdir(dir_name)
    files_and_dirs.sort()
    entries = [os.path.join(dir_name, fd) for fd in files_and_dirs]

    dirs = [d for d in entries if os.path.isdir(d)]
    files = [f for f in entries if os.path.isfile(f)]

    for d in dirs:
        result += directory_info(d, prefix + "│   ")
    
    for f in files:
        result += f"{prefix}│   └── {os.path.basename(f)}\n"

    return result

if __name__ == "__main__":
    directory_name = sys.argv[1]
    print(directory_info(directory_name))
# -*- coding: utf-8 -*-
"""SOURCE CODE

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zU3dul0fKUpmjNUuwagXgLCtbQMjUhqM
"""

import os
import shutil
from pathlib import Path

def sync_files(source_dir, dest_dir):
    """
    Synchronize files from source_dir to dest_dir.
    Newer files overwrite older ones. Does not delete files from dest_dir.
    """
    source_dir = Path(source_dir)
    dest_dir = Path(dest_dir)

    if not source_dir.is_dir():
        print(f"Source directory {source_dir} does not exist or is not a directory.")
        return

    # Ensure the destination directory exists
    dest_dir.mkdir(parents=True, exist_ok=True)

    for src_path in source_dir.rglob('*'):
        if src_path.is_file():
            relative_path = src_path.relative_to(source_dir)
            dest_path = dest_dir.joinpath(relative_path)

            if dest_path.exists():
                # Only copy if the source file is newer than the destination file
                if src_path.stat().st_mtime > dest_path.stat().st_mtime:
                    shutil.copy2(src_path, dest_path)
                    print(f"Updated: {dest_path}")
            else:
                dest_path.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(src_path, dest_path)
                print(f"Copied: {dest_path}")

def main():
    source_directory = input("Enter the source directory path: ")
    destination_directory = input("Enter the destination directory path: ")

    sync_files(source_directory, destination_directory)
    print("Synchronization complete.")

if __name__ == "__main__":
    main()
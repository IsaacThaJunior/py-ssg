import os
import shutil


def recursive_file_copier(src, dst):
    # Check if destination exists and deletse it
    if os.path.exists(dst):
        shutil.rmtree(dst)
    # Then creates the destination again
    os.mkdir(dst)

    for item in os.listdir(src):
        src_path = os.path.join(src, item)
        dst_path = os.path.join(dst, item)
        if os.path.isdir(src_path):
            print(f"Creating Directory: {dst_path}")
            recursive_file_copier(src_path, dst_path)
        else:
            print(f"Copying file: {src_path} -> {dst_path}")
            shutil.copyfile(src_path, dst_path)

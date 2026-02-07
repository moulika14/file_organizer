import os
import shutil

folder_path = r"C:\Users\Moulika\Desktop\test_folder"

files = os.listdir(folder_path)

images_folder = os.path.join(folder_path, "Images")
videos_folder = os.path.join(folder_path, "Videos")
files_folder = os.path.join(folder_path, "Files")

if not os.path.exists(images_folder):
    os.makedirs(images_folder)

if not os.path.exists(videos_folder):
    os.makedirs(videos_folder)

if not os.path.exists(files_folder):
    os.makedirs(files_folder)

for file in files:
    name, extension = os.path.splitext(file)

    if extension == ".jpg" or extension == ".png":
        shutil.move(os.path.join(folder_path, file),
                    os.path.join(images_folder, file))

    elif extension == ".mp4":
        shutil.move(os.path.join(folder_path, file),
                    os.path.join(videos_folder, file))

    elif extension == ".txt" or extension == ".pdf":
        shutil.move(os.path.join(folder_path, file),
                    os.path.join(files_folder, file))

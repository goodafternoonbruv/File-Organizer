import os
import shutil

path = r"/Users/maxwell/Downloads/"
file_names = os.listdir(path)

# Define folder names for different file types
folder_names = {
    ".pdf": "pdf files",
    ".jpg": "image files",
    ".zip": "compressed files",
    ".docx": "document files",
    ".png": "image files",
    ".mp3": "audio files",
    ".dmg": "disk images",
    ".mid": "audio files",
    ".swf": "flash files",
    ".tar.bz2": "compressed files",
    ".html": "web files",
    ".rar": "compressed files",
    ".iso": "disk images",
    ".heic": "image files",
    ".wav": "audio files",
    ".svg": "vector graphics",
    ".ssd": "sprite sheets"
}

# Create folders if they don't exist
for folder in folder_names.values():
    if not os.path.exists(os.path.join(path, folder)):
        os.makedirs(os.path.join(path, folder))

# Move files to corresponding folders
for file in file_names:
    for extension, folder in folder_names.items():
        if file.endswith(extension) and not os.path.exists(os.path.join(path, folder, file)):
            shutil.move(os.path.join(path, file), os.path.join(path, folder, file))
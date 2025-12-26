import os

downloads_folder_path = "/path/to/your/downloads/folder"
downloads_files = []
with os.scandir(downloads_folder_path) as files:
    for file in files:
        downloads_files.append(file.name)

categories = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx", ".csv", ".doc"],
    "Videos": [".mp4", ".avi", ".mov", ".mkv"],
    "Music": [".mp3", ".wav", ".aac", ".flac"],
    "Applications": [".exe", ".msi", ".dmg"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Maps": [".map", ".osm", ".kml", ".kmz", ".gpx"]
}

for category in categories.keys():
    category_path = os.path.join(downloads_folder_path, category)
    if not os.path.exists(category_path):
        os.makedirs(category_path)

files_moved = 0
files_not_moved = []
for file_name in downloads_files:
    file_path = os.path.join(downloads_folder_path, file_name)
    if os.path.isfile(file_path):
        file_ext = os.path.splitext(file_name)[1].lower()
        moved = False
        for category, extensions in categories.items():
            if file_ext in extensions:
                dest_path = os.path.join(downloads_folder_path, category, file_name)
                counter = 1
                while os.path.exists(dest_path):
                    name, ext = os.path.splitext(file_name)
                    dest_path = os.path.join(downloads_folder_path, category, f"{name}({counter}){ext}")
                    counter += 1
                os.rename(file_path, dest_path)
                moved = True
                files_moved += 1
                print(f"Moved '{file_name}' to '{category}' folder.")
                break
        if not moved:
            files_not_moved.append(file_name)
print(f"Total files moved: {files_moved}")
print(f"Files not categorized: {files_not_moved}")

if __name__ == "__main__":
    print("File organization complete.")
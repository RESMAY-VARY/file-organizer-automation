import os

def organize_folder(folder_path):
    for filename in os.listdir(folder_path):
        full_path = os.path.join(folder_path, filename)

        # Skip directories
        if os.path.isdir(full_path):
            continue

        # Normalize the filename
        new_name = filename.replace(" ", "_").lower()
        new_path = os.path.join(folder_path, new_name)

        # Rename file
        os.rename(full_path, new_path)

        # Determine extension folder
        ext = new_name.split(".")[-1]
        ext_folder = os.path.join(folder_path, ext)

        # Create folder if needed
        if not os.path.exists(ext_folder):
            os.makedirs(ext_folder)

        # Move file into extension folder
        final_path = os.path.join(ext_folder, new_name)
        os.rename(new_path, final_path)

        print(f"Moved: {new_name} → {ext}/")

# Example usage
organize_folder("/path/to/your/folder")


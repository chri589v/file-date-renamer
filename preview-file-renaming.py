import os
from datetime import datetime

def preview_renaming(folder_path, extension):
    """
    Preview how files would be renamed based on modification date.
    No changes are made.
    """

    extension = extension.lower()

    for filename in os.listdir(folder_path):
        if not filename.lower().endswith(extension):
            continue

        if (
            len(filename) >= 10
            and filename[:10].count("-") == 2
            and filename[:10].replace("-", "").isdigit()
        ):
            continue

        filepath = os.path.join(folder_path, filename)

        try:
            modification_time = os.path.getmtime(filepath)
            modification_date = datetime.fromtimestamp(modification_time)

            date_str = modification_date.strftime("%Y-%m-%d")
            new_filename = f"{date_str}{extension}"

            print(f"{filename} → {new_filename}")

        except Exception as e:
            print(f"Error processing {filename}: {e}")

if __name__ == "__main__":
    folder_path = input("Enter folder path: ").strip()
    extension = input("Enter file extension (e.g. .png): ").strip()

    if not extension.startswith("."):
        extension = "." + extension

    if not os.path.isdir(folder_path):
        print("Invalid folder path.")
    else:
        preview_renaming(folder_path, extension)
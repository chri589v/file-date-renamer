import os
from datetime import datetime

def rename_files_by_date(folder_path, extension):
    """
    Rename files with a specific extension based on their modification date.
    """

    extension = extension.lower()

    for filename in os.listdir(folder_path):
        if not filename.lower().endswith(extension):
            continue

        # Skip files that already start with a date
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
            new_filepath = os.path.join(folder_path, new_filename)

            counter = 1
            while os.path.exists(new_filepath):
                new_filename = f"{date_str}_{counter}{extension}"
                new_filepath = os.path.join(folder_path, new_filename)
                counter += 1

            os.rename(filepath, new_filepath)
            print(f"Renamed: {filename} → {new_filename}")

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
        rename_files_by_date(folder_path, extension)
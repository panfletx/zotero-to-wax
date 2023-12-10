import os
import csv
import shutil

def create_and_copy():
    # Prompt user for the path to the CSV file
    csv_file_path = input("Enter the path to the CSV file: ")

    # Check if the CSV file exists
    if not os.path.exists(csv_file_path):
        print(f"Error: CSV file '{csv_file_path}' not found.")
        return

    # Read CSV file and find the column indices for Key and File Attachments
    key_column_index = -1
    file_attachments_column_index = -1

    with open(csv_file_path, 'r', encoding='utf-8-sig') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader, None)

        if header:
            for i, column_name in enumerate(header):
                if column_name.strip().lower() == "key":
                    key_column_index = i
                elif column_name.strip().lower() == "file attachments":
                    file_attachments_column_index = i

    if key_column_index == -1 or file_attachments_column_index == -1:
        print("Error: Could not find 'Key' or 'File Attachments' columns in the CSV file.")
        return

    # Read CSV file and create directories and copy files
    with open(csv_file_path, 'r', encoding='utf-8-sig') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip the header row if it exists

        for row in reader:
            if len(row) > max(key_column_index, file_attachments_column_index):
                new_directory = row[key_column_index].strip()
                source_paths = [path.strip() for path in row[file_attachments_column_index].split(';')]

                # Create the new directory if it doesn't exist
                os.makedirs(new_directory, exist_ok=True)
                print(f"Created new directory '{new_directory}'")

                # Copy each source file to the new directory
                for source_path in source_paths:
                    # Check if the source file exists
                    if os.path.exists(source_path):
                        shutil.copy(source_path, os.path.join(new_directory, os.path.basename(source_path)))
                        print(f"Copied '{source_path}' to '{new_directory}'")
                    else:
                        print(f"Error: Source path '{source_path}' not found.")

if __name__ == "__main__":
    create_and_copy()

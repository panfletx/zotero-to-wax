import os
import csv
import shutil

def create_and_copy(csv_file):
    # Check if the CSV file exists
    if not os.path.exists(csv_file):
        print(f"Error: CSV file '{csv_file}' not found.")
        return

    # Read CSV file and create directories and copy files
    with open(csv_file, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip the header row if it exists

        for row in reader:
            if len(row) == 2:
                new_directory = row[0].strip()
                source_paths = [path.strip() for path in row[1].split(';')]

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
    csv_file_path = input("Enter the path to the CSV file: ")
    create_and_copy(csv_file_path)
import csv
import os
import random

# Define file paths
input_file_path =  r"N:\Dataset\output_file.csv"  # 33GB file
output_file_path = r"E:\DLR\output_file_2GB.csv"  # Target 2GB file

# Define the approximate number of bytes for 2GB
TARGET_SIZE = 2 * 1024 * 1024 * 1024  # 2GB in bytes

# Function to check file size
def get_file_size(file_path):
    return os.path.getsize(file_path)

# Open the input and output CSV files
with open(input_file_path, mode='r', encoding='utf-8') as input_file:
    reader = csv.DictReader(input_file)

    with open(output_file_path, mode='w', newline='', encoding='utf-8') as output_file:
        writer = csv.DictWriter(output_file, fieldnames=reader.fieldnames)
        writer.writeheader()  # Write the header

        for row in reader:
            # Randomly write rows to the output file
            if random.random() < 0.1:  # Adjust the probability based on the desired size
                writer.writerow(row)
            
            # Check if the output file has reached the target size
            if get_file_size(output_file_path) >= TARGET_SIZE:
                print(f"Output file reached 2GB in size: {get_file_size(output_file_path)} bytes")
                break

print("Random subset of data saved to output_file_2GB.csv")

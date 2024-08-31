# DataSculptor
This is the idea of shaping and refining raw, unstructured data into well-organized, structured formats, emphasizing the process of transformation.

**"Large Unorganized TXT File to Reduced Organized CSV File"**. 

# Large Unorganized TXT File to Reduced Organized CSV File

This project provides a Python solution for converting a large, unstructured text file into an organized CSV format, while also reducing the size of the original file to a more manageable size (approximately 2GB). 

## Overview

Given the challenge of processing extremely large datasets (e.g., a 33GB unstructured text file), this script:
- Converts the raw, unstructured data into an organized CSV file format.
- Randomly samples the data to generate a reduced output file, capped at around 2GB.

The dataset used for this process, such as Amazon product reviews or similar, contains unstructured product and review data, which we aim to convert into structured rows and fields in CSV.

## Key Features

- **Unstructured to Structured Conversion**: Reads unorganized text data, parses it into relevant fields (e.g., productId, title, price, user reviews).
- **Size Reduction via Random Sampling**: Randomly selects rows to reduce the CSV file size while maintaining a representative sample of the data.
- **Efficient File Processing**: Processes large files line-by-line to avoid memory overload.

## Dataset

For this project, we are working with the **Amazon Product Reviews Dataset** from Stanford SNAP. The dataset link can be found here:
[Amazon Product Reviews Dataset](https://snap.stanford.edu/data/amazon/all.txt.gz)

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/nilavanan-ver-4/DataSculptor.git
   cd DataSculptor
   ```

2. **Install required libraries**:  
   Create a virtual environment (optional but recommended), then install any additional dependencies with:
   ```bash
   pip install -r requirements.txt
   ```

   **Note**: The standard libraries (`csv`, `os`, and `random`) are used and do not require installation.

## Usage

### 1. TXT to CSV Conversion

To convert the unstructured text file into a CSV format, use the script `txtToCSV.py`.

```bash
python txtToCSV.py
```

- **Input**: A large unorganized text file (e.g., `all.txt`) with product and review data.
- **Output**: A structured CSV file (e.g., `output_file.csv`).

### 2. CSV Size Reduction

To reduce the size of the generated CSV file (e.g., from 33GB to 2GB), use the `reduce_csv.py` script.

```bash
python reduceCSV.py
```

This script will randomly sample the rows and write them to a new CSV file, stopping once the target size (2GB) is reached.

- **Input**: A large CSV file (e.g., `output_file.csv`).
- **Output**: A reduced-size CSV file (e.g., `output_file_2GB.csv`).

## Example

Here’s an example command to reduce a 33GB CSV file to approximately 2GB:

```bash
python reduceCSV.py
```

After running the script, you will get an output message indicating the file size once it reaches the target.

## Project Structure

```bash
.
├── txtToCSV.py           # Script to convert unstructured TXT data to CSV format
├── reduceCSV.py          # Script to reduce the size of the CSV file by random sampling
├── requirements.txt      # Dependencies for the project
├── README.md             # This documentation file
```

## Requirements

- Python 3.x
- Libraries: 
  - `csv`
  - `os`
  - `random`

These libraries are part of the Python Standard Library, so no additional installation is required.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


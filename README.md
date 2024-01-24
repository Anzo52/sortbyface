# sortbyface

## Introduction

sortbyface is a Python-based tool designed to organize and categorize local photos by identifying and comparing faces present in images. Utilizing face recognition technology, it simplifies the process of sorting through large collections of photos based on the people in them.

## Features

- Face detection and comparison in images.
- Clustering of images based on facial similarities.
- User-friendly command-line interface.

## Installation

Before running the scripts, ensure you have Python installed along with the necessary dependencies:

- face_recognition
- argparse
- shutil
- pathlib

## Usage Instructions

### check4match.py

This script compares two images to determine if the same face is present in both.

- **Usage**:

```bash
python check4match.py <path_to_first_image> <path_to_second_image>
```

- **Example**:

```bash
python check4match.py image1.jpg image2.jpg
```

- The script will output "It's a match!" if the same face is detected in both images, otherwise "It's not a match!".

### process_cluster.py

This script processes a batch of images, identifying faces, and sorts them into clusters based on facial similarity.

- **Preparation**: Place all images to be processed in a directory named `dataset2` in the same directory as the script.
- **Usage**:

```bash
python process_cluster.py
```

- The script will create a `results` directory with subfolders for each cluster of faces.

## Contributing

Contributions to improve sortbyface are welcome. Feel free to fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

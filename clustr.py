import os


def get_dataset_path():
    cwd = os.getcwd()
    return os.path.join(cwd, "dataset")


def get_filepaths(dataset_path):
    return [
        os.path.join(subdir, file)
        for subdir, _, files in os.walk(dataset_path)
        for file in files
    ]


def main():
    dataset_path = get_dataset_path()
    filepaths = get_filepaths(dataset_path)
    for filepath in filepaths:
        print(filepath)


if __name__ == "__main__":
    main()

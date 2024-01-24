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


def fp():
    dataset_path = get_dataset_path()
    return get_filepaths(dataset_path)


def main():
    filepaths = fp()
    for filepath in filepaths:
        print(filepath)


if __name__ == "__main__":
    main()

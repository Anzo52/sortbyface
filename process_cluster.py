import face_recognition
import os
from pathlib import Path
from shutil import copyfile

cwd = os.getcwd()
results_path = os.path.join(cwd, "results")
encodings = {}


def process_file(filepath):
    img = face_recognition.load_image_file(filepath)
    fe = face_recognition.face_encodings(img)
    # it could be possible that no faces can be found. If any, just take the first image
    if fe:
        fe = fe[0]
    else:
        return
    action_taken = False
    curr_image_cluster_id = None
    for cluster_id, cluster_encodings in encodings.items():
        results = face_recognition.compare_faces(cluster_encodings, fe)
        print(f"results {results} {cluster_id}")
        # if the current image matches all the encodings of the encodings we have for that cluster,
        # we add the current image to that cluster
        if all(results):
            print(f"cluster_id {cluster_id}")
            curr_image_cluster_id = cluster_id
            encodings.get(curr_image_cluster_id).append(fe)
            action_taken = True
    # if current image was not added to any cluster we have, create a new cluster
    if not action_taken:
        curr_image_cluster_id = f"cluster_{len(encodings.keys()) + 1}"
        print(f"creating new cluster {curr_image_cluster_id}")
        encodings[curr_image_cluster_id] = [fe]

    curr_cluster = os.path.join(results_path, curr_image_cluster_id)
    curr_cluster_dir = Path(curr_cluster)
    curr_cluster_dir.mkdir(parents=True, exist_ok=True)
    # extract the filename from the filepath
    filename = os.path.basename(filepath)
    # copy the file to the corresponding cluster's folder
    copyfile(filepath, os.path.join(curr_cluster_dir, filename))


def process_cluster():
    dataset_path = os.path.join(cwd, "dataset")
    filepaths = [
        os.path.join(subdir, file)
        for subdir, _, files in os.walk(dataset_path)
        for file in files
    ]
    for filepath in filepaths:
        process_file(filepath)
    print(encodings)
    return encodings


if __name__ == "__main__":
    process_cluster()

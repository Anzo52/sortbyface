import face_recognition
from pathlib import Path
from shutil import copyfile


def process_file(filepath):
    faceencodings = get_faceencodings(filepath)
    action_taken, encodings = acta(faceencodings)
    if not action_taken:
        curr_image_cluster_id = get_curr_image_cluster_id(faceencodings, encodings)
    results_path = Path.cwd() / "results"
    curr_cluster = results_path / curr_image_cluster_id
    curr_cluster.mkdir(parents=True, exist_ok=True)
    filename = filepath.name
    copyfile(filepath, curr_cluster / filename)
    return encodings


def get_curr_image_cluster_id(faceencodings, encodings):
    curr_image_cluster_id = f"cluster_{len(encodings.keys()) + 1}"
    print(f"creating new cluster {curr_image_cluster_id}")
    encodings[curr_image_cluster_id] = [faceencodings]
    return curr_image_cluster_id


def acta(faceencodings):
    action_taken = False
    curr_image_cluster_id = None
    encodings = {}
    for cluster_id, cluster_encodings in encodings.items():
        results = get_results(faceencodings, cluster_id, cluster_encodings)
        if all(results):
            print(f"cluster_id {cluster_id}")
            curr_image_cluster_id = cluster_id
            encodings.get(curr_image_cluster_id).append(faceencodings)
            action_taken = True
    return action_taken, encodings


def get_results(faceencodings, cluster_id, cluster_encodings):
    results = face_recognition.compare_faces(cluster_encodings, faceencodings)
    print(f"results {results} {cluster_id}")
    return results


def get_faceencodings(filepath):
    img = face_recognition.load_image_file(str(filepath))
    faceencodings = face_recognition.face_encodings(img)
    if faceencodings:
        faceencodings = faceencodings[0]
    return faceencodings


def process_cluster():
    dataset_path = Path.cwd() / "dataset2"
    filepaths = list(dataset_path.iterdir())
    for filepath in filepaths:
        process_file(filepath)
        print(f"processed {filepath}")
    print("done")
    return True


def get_dataset_path():
    return Path.cwd() / "dataset"


def main():
    process_cluster()


if __name__ == "__main__":
    main()

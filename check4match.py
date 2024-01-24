import argparse
import face_recognition


def load_and_encode_image(image_path):
    image = face_recognition.load_image_file(image_path)
    return face_recognition.face_encodings(image)[0]


def args_to_encodings(args):
    face1_encoding = load_and_encode_image(args.image1)
    face2_encoding = load_and_encode_image(args.image2)
    return face1_encoding, face2_encoding


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("image1", help="Path to the first image")
    parser.add_argument("image2", help="Path to the second image")
    return parser.parse_args()



def check_match(args):
    face1_encoding, face2_encoding = args_to_encodings(args)

    return face_recognition.compare_faces([face1_encoding], face2_encoding)[0]


def main():
    args = get_args()

    match = check_match(args)
    print("It's a match!" if match else "It's not a match!")


if __name__ == "__main__":
    main()

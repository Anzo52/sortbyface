import argparse
import face_recognition


def check_for_match(face1_encoding, face2_encoding):
    return face_recognition.compare_faces([face1_encoding], face2_encoding)[0]


def load_and_encode_image(image_path):
    image = face_recognition.load_image_file(image_path)
    return face_recognition.face_encodings(image)[0]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("image1", help="Path to the first image")
    parser.add_argument("image2", help="Path to the second image")
    args = parser.parse_args()

    face1_encoding = load_and_encode_image(args.image1)
    face2_encoding = load_and_encode_image(args.image2)

    match = check_for_match(face1_encoding, face2_encoding)
    print("It's a match!" if match else "It's not a match!")


if __name__ == "__main__":
    main()

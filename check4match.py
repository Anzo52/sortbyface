import argparse
import face_recognition

def check4match(face1_emcoding, face2_encoding):
    # compare the face encodings using compare_faces
    results = face_recognition.compare_faces([face1_emcoding], face2_encoding)
    match = results[0]
    print("It's a match!" if match else "It's not a match!")
    return match

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("image1", help="Path to the first image")
    parser.add_argument("image2", help="Path to the second image")
    args = parser.parse_args()

    # load the images
    image1 = face_recognition.load_image_file(args.image1)
    image2 = face_recognition.load_image_file(args.image2)

    # get the face encodings of the images
    face1_encoding = face_recognition.face_encodings(image1)[0]
    face2_encoding = face_recognition.face_encodings(image2)[0]

    # compare the face encodings using compare_faces
    check4match(face1_encoding, face2_encoding)

if __name__ == "__main__":
    main()

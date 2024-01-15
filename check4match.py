import face_recognition


def check4match(face1_emcoding, face2_encoding):
    # compare the face encodings using compare_faces
    results = face_recognition.compare_faces([face1_emcoding], face2_encoding)

    # if array of encodings is passed as first parameter
    # then just compare the first encoding in the array
    if results[0] == True:
        print("It's a match!")
        return True
    else:
        print("It's not a match!")
        return False


def load_image():
    image_path = input("Enter the path of the image: ")
    return face_recognition.load_image_file(image_path)


def get_encoding(image):
    return face_recognition.face_encodings(image)[0]


def main():
    # load the image
    image1 = load_image()
    image2 = load_image()

    # get the face encoding of the image
    face1_encoding = get_encoding(image1)
    face2_encoding = get_encoding(image2)

    # compare the face encodings using compare_faces
    check4match(face1_encoding, face2_encoding)


if __name__ == "__main__":
    main()
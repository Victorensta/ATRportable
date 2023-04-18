import face_recognition
from imutils import paths
import numpy as np


def load_BDD():
    imagePaths = list(paths.list_images("./Test_material/Images"))
    known_face_encodings = np.zeros((len(imagePaths), 128))
    with open('known_face_names.txt', 'w') as f:
        for i in range(len(imagePaths)):
            image = face_recognition.load_image_file(imagePaths[i])
            if face_recognition.face_encodings(image):
                face_encoding = face_recognition.face_encodings(image)[0]
            name = str(imagePaths[i][23:].split(".", 1)[0])+'\n'
            f.write(name)
            known_face_encodings[i] = face_encoding
    np.save("known_face_encodings", known_face_encodings)

load_BDD()

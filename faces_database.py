import face_recognition


nicolas_image = face_recognition.load_image_file("Test_material/Images/nicolas.jpg")
nicolas_face_encoding = face_recognition.face_encodings(nicolas_image)[0]

obama_image = face_recognition.load_image_file("Test_material/Images/barackObama.jpg")
obama_face_encoding = face_recognition.face_encodings(obama_image)[0]

musk_image = face_recognition.load_image_file("Test_material/Images/elonMusk.jpg")
musk_face_encoding = face_recognition.face_encodings(musk_image)[0]

victor_image = face_recognition.load_image_file("Test_material/Images/VictorXu.JPG")
victor_face_encoding = face_recognition.face_encodings(victor_image)[0]

eliot_image = face_recognition.load_image_file("Test_material/Images/EliotJacquemin.JPG")
eliot_face_encoding = face_recognition.face_encodings(eliot_image)[0]

salman_image = face_recognition.load_image_file("Test_material/Images/SalmanAlmutairi.JPG")
salman_face_encoding = face_recognition.face_encodings(salman_image)[0]

ahmed_image = face_recognition.load_image_file("Test_material/Images/AhmedAlotaibi.JPG")
ahmed_face_encoding = face_recognition.face_encodings(ahmed_image)[0]

#toumi_image = face_recognition.load_image_file("Test_material/Images/toumi.jpg")
#toumi_face_encoding = face_recognition.face_encodings(toumi_image)[0]

thomas_image = face_recognition.load_image_file("Test_material/Images/thomas.PNG")
thomas_face_encoding = face_recognition.face_encodings(thomas_image)[0]


# Create arrays of known face encodings and their names
known_face_encodings = [
    nicolas_face_encoding, obama_face_encoding, musk_face_encoding, victor_face_encoding,
    eliot_face_encoding, salman_face_encoding, ahmed_face_encoding, thomas_face_encoding #toumi_face_encoding
]
known_face_names = [
    "Nicolas Le Roux", "Barack Obama", "Elon Musk", "Victor Xu",
    "Eliot Jacquemin", "Salman Almutairi", "Ahmed Alotaibi", "Thomas Le Roux" #, "Abdelmalek Toumi"
]

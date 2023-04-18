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

# thibault_haudricourt_image = face_recognition.load_image_file("Test_material/Images/ThibaultHaudricourt.JPG")
# thibault_haudricourt_face_encoding = face_recognition.face_encodings(thibault_haudricourt_image)[0]
#
# celia_giani_image = face_recognition.load_image_file("Test_material/Images/CeliaGiani.JPG")
# celia_giani_face_encoding = face_recognition.face_encodings(celia_giani_image)[0]
#
# emilie_peridon_image = face_recognition.load_image_file("Test_material/Images/EmiliePeridon.JPG")
# emilie_peridon_face_encoding = face_recognition.face_encodings(emilie_peridon_image)[0]
#
# maurine_orveillon_image = face_recognition.load_image_file("Test_material/Images/maurine_orveillon.JPG")
# maurine_orveillon_face_encoding = face_recognition.face_encodings(maurine_orveillon_image)[0]
#
# clara_baffou_image = face_recognition.load_image_file("Test_material/Images/clara_baffou.JPG")
# clara_baffou_face_encoding = face_recognition.face_encodings(clara_baffou_image)[0]
#
# louka_masson_image = face_recognition.load_image_file("Test_material/Images/louka_masson.JPG")
# louka_masson_face_encoding = face_recognition.face_encodings(louka_masson_image)[0]
#
# maelys_eymond_image = face_recognition.load_image_file("Test_material/Images/maelys_eymond.JPG")
# maelys_eymond_face_encoding = face_recognition.face_encodings(maelys_eymond_image)[0]
#
# adam_goux_gateau_image = face_recognition.load_image_file("Test_material/Images/adam_goux_gateau.JPG")
# adam_goux_gateau_face_encoding = face_recognition.face_encodings(adam_goux_gateau_image)[0]
#
# simon_martineau_image = face_recognition.load_image_file("Test_material/Images/simon_martineau.JPG")
# simon_martineau_face_encoding = face_recognition.face_encodings(simon_martineau_image)[0]
#
# quentin_delaunay_image = face_recognition.load_image_file("Test_material/Images/quentin_delaunay.JPG")
# quentin_delaunay_face_encoding = face_recognition.face_encodings(quentin_delaunay_image)[0]
#
# romain_bornier_image = face_recognition.load_image_file("Test_material/Images/romain_bornier.JPG")
# romain_bornier_face_encoding = face_recognition.face_encodings(romain_bornier_image)[0]
#
# alexis_aygalenq_image = face_recognition.load_image_file("Test_material/Images/alexis_aygalenq.JPG")
# alexis_aygalenq_face_encoding = face_recognition.face_encodings(alexis_aygalenq_image)[0]
#
# noe_parker_image = face_recognition.load_image_file("Test_material/Images/noe_parker.JPG")
# noe_parker_face_encoding = face_recognition.face_encodings(noe_parker_image)[0]
#
# gwendal_crequer_image = face_recognition.load_image_file("Test_material/Images/gwendal_crequer.JPG")
# gwendal_crequer_face_encoding = face_recognition.face_encodings(gwendal_crequer_image)[0]
#
# harry_mang_image = face_recognition.load_image_file("Test_material/Images/harry_mang.JPG")
# harry_mang_face_encoding = face_recognition.face_encodings(harry_mang_image)[0]
#
# thomas_nguyen_image = face_recognition.load_image_file("Test_material/Images/thomas_nguyen.JPG")
# thomas_nguyen_face_encoding = face_recognition.face_encodings(thomas_nguyen_image)[0]
#
# livia_gattacceca_image = face_recognition.load_image_file("Test_material/Images/livia_gattacceca.JPG")
# livia_gattacceca_face_encoding = face_recognition.face_encodings(livia_gattacceca_image)[0]
#
# elise_mainka_image = face_recognition.load_image_file("Test_material/Images/elise_mainka.JPG")
# elise_mainka_face_encoding = face_recognition.face_encodings(elise_mainka_image)[0]
#
# titouan_st_cyr_image = face_recognition.load_image_file("Test_material/Images/titouan_st_cyr.JPG")
# titouan_st_cyr_face_encoding = face_recognition.face_encodings(titouan_st_cyr_image)[0]
#
# mohammed_alamri_image = face_recognition.load_image_file("Test_material/Images/mohammed_alamri.JPG")
# mohammed_alamri_face_encoding = face_recognition.face_encodings(mohammed_alamri_image)[0]
#
# abdulmalik_alhomidy_image = face_recognition.load_image_file("Test_material/Images/abdulmalik_alhomidy.JPG")
# abdulmalik_alhomidy_face_encoding = face_recognition.face_encodings(abdulmalik_alhomidy_image)[0]
#
# abdulmajeed_alhusaini_image = face_recognition.load_image_file("Test_material/Images/abdulmajeed_alhusaini.JPG")
# abdulmajeed_alhusaini_face_encoding = face_recognition.face_encodings(abdulmajeed_alhusaini_image)[0]
#
# marius_berezecki_image = face_recognition.load_image_file("Test_material/Images/marius_berezecki.JPG")
# marius_berezecki_face_encoding = face_recognition.face_encodings(marius_berezecki_image)[0]
#
# clement_patrizio_image = face_recognition.load_image_file("Test_material/Images/clement_patrizio.JPG")
# clement_patrizio_face_encoding = face_recognition.face_encodings(clement_patrizio_image)[0]
#
# jean_pierre_chauvet_image = face_recognition.load_image_file("Test_material/Images/jean_pierre_chauvet.JPG")
# jean_pierre_chauvet_face_encoding = face_recognition.face_encodings(jean_pierre_chauvet_image)[0]
#
# marie_lissillour_image = face_recognition.load_image_file("Test_material/Images/marie_lissillour.JPG")
# marie_lissillour_face_encoding = face_recognition.face_encodings(marie_lissillour_image)[0]
#
# titouan_marechal_image = face_recognition.load_image_file("Test_material/Images/Titouan_Marechal.JPG")
# titouan_marechal_face_encoding = face_recognition.face_encodings(titouan_marechal_image)[0]
# Create arrays of known face encodings and their names
known_face_encodings = [
    nicolas_face_encoding, obama_face_encoding, musk_face_encoding, victor_face_encoding,
    eliot_face_encoding, salman_face_encoding, ahmed_face_encoding
    # , thibault_haudricourt_face_encoding, celia_giani_face_encoding, emilie_peridon_face_encoding, maurine_orveillon_face_encoding, clara_baffou_face_encoding, louka_masson_face_encoding, maelys_eymond_face_encoding, adam_goux_gateau_face_encoding, simon_martineau_face_encoding, quentin_delaunay_face_encoding, romain_bornier_face_encoding, alexis_aygalenq_face_encoding, noe_parker_face_encoding, gwendal_crequer_face_encoding, harry_mang_face_encoding, thomas_nguyen_face_encoding, livia_gattacceca_face_encoding, elise_mainka_face_encoding, titouan_st_cyr_face_encoding, mohammed_alamri_face_encoding, abdulmalik_alhomidy_face_encoding, abdulmajeed_alhusaini_face_encoding, marius_berezecki_face_encoding, clement_patrizio_face_encoding, jean_pierre_chauvet_face_encoding, marie_lissillour_face_encoding, titouan_marechal_face_encoding
]
known_face_names = [
    "Nicolas Le Roux", "Barack Obama", "Elon Musk", "Victor Xu",
    "Eliot Jacquemin", "Salman Almutairi", "Ahmed Alotaibi"
    # , "Thibault Haudricourt", "Célia Giani", "Émilie Péridon", "Maurine Orveillon", "Clara Baffou", "Louka Masson", "Maëlys Eymond", "Adam Goux-Gateau", "Simon Martineau", "Quentin Delaunay", "Romain Bornier", "Alexis Aygalenq", "Noé Parker", "Gwendal Crequer", "Harry Mang", "Thomas Nguyen", "Livia Gattacceca", "Elise Mainka", "Titouan Saint-Cyr", "Mohammed Alamri", "Abdulmalik Alhomidy", "Abdulmajeed Alhusaini", "Marius Berezecki", "Clement Patrizio", "Jean-Pierre Chauvet", "Marie Lissillour", "Titouan Maréchal"
]

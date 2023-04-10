import unittest
import numpy as np
import cv2 as cv2
import face_recognition
from datetime import datetime
from tracker import EuclideanDistTracker


class TestEuclideanDistTracker(unittest.TestCase):
    def testInitI(self):
        testname = "testname"
        testtracker = EuclideanDistTracker(testname)
        self.assertIs(testtracker.name, testname)

    def testInitII(self):
        testtracker = EuclideanDistTracker("testname")
        self.assertEqual(testtracker.id_count, 0)

    def testInitIII(self):
        testtracker = EuclideanDistTracker("testname")
        self.assertEqual(testtracker.center_points, {})

    def testUpdateI(self):
        testtracker = EuclideanDistTracker("testname")
        [min, sec] = (datetime.now().minute, datetime.now().second)
        testrec = np.array([[100, 200, 101, 101]])
        testtracker.update(testrec)
        # on prend la partie entiere pour avoir des coordonnees entieres
        self.assertEqual(testtracker.center_points[0], [150, 250, [min, sec]])

    def testMemory(self):
        testtracker = EuclideanDistTracker("testname")
        testrec1 = np.array([[100, 200, 101, 101]])
        testtracker.update(testrec1)
        testrec2 = np.array([[150, 250, 101, 101]])
        testtracker.update(testrec2)
        self.assertEqual(testtracker.id_count, 2)
        testtracker.center_points[0][2][0] = -1.1 + datetime.now().minute
        testtracker.center_points[1][2][0] = -1.1 + datetime.now().minute
        testrec3 = np.array([[200, 300, 101, 101]])
        testtracker.update(testrec3)
        self.assertEqual(testtracker.id_count, 1)
        self.assertEqual(len(testtracker.center_points), 3)
        testtracker.center_points[2][2][0] = -1.1 + datetime.now().minute
        testtracker.update([])
        self.assertEqual(testtracker.id_count, 0)
        testtracker.update([])
        self.assertEqual(len(testtracker.center_points), 0)


class TestRecognition(unittest.TestCase):
    def testKnownFace(self):
        # C'est normal que ça ne marche pas tout le temps, à relancer et ça devrait marcher au bout d'un temps
        frame = cv2.imread("Test_material/Images/nicolas2.png")
        nicolas_image = face_recognition.load_image_file("Test_material/Images/nicolas.jpg")
        nicolas_face_encoding = face_recognition.face_encodings(nicolas_image)[0]
        obama_image = face_recognition.load_image_file("Test_material/Images/barackObama.jpg")
        obama_face_encoding = face_recognition.face_encodings(obama_image)[0]
        known_face_encodings = [nicolas_face_encoding, obama_face_encoding]
        known_face_names = ["Nicolas Le Roux", "Barack Obama"]
        frame = cv2.resize(frame, (640, 400))
        rgb_frame = frame[:, :, ::-1]
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
        face_names = []
        face_encoding = face_encodings[0]
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"
        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = known_face_names[best_match_index]
        face_names.append(name)
        self.assertIn("Nicolas Le Roux", face_names)


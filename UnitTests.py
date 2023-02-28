import unittest
import numpy as np
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
        testrec = np.array([[100, 200, 101, 101]])
        testtracker.update(testrec)
        # on prend la partie entiere pour avoir des coordonnees entieres
        self.assertEqual(testtracker.center_points[0], (150, 250))


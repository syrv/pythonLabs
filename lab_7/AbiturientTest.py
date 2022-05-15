import unittest
import Abiturient


class AbiturientTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Set Up Class Method!"""
        print("SetUpClass")
        print("==========================")

    @classmethod
    def tearDownClass(cls):
        """Tear Down Class Method!"""
        print("==========================")
        print("TearDownClass")

    def setUp(self):
        """Set Up Method!"""
        print("Setting up for a test")
        print("==========================")

    def tearDown(self):
        """Tear Down Method!"""
        print("==========================")
        print("Cleaning mess after a test")


    def test_str(self):
        self.assertNotEqual(Abiturient.igor.__str__(), Abiturient.igor.name+Abiturient.igor.phone)

    def test_awards(cls):
        cls.assertTrue("Награжден медалью или грамотой.", Abiturient.ivan )

    def test_accuracy(self):
        self.assertEqual(Abiturient.Abiturient.__mark.isinstance(int),True)

    def test_abData(self):
        self.assertLess(Abiturient.igor , Abiturient.artem)



if __name__ == '__main__':
    unittest.main()
import unittest
from password import User


class TestUser(unittest.TestCase):

    def setUp(self):
        self.new_credentials = User("Kenneth", "facebook", "kys1112")

    def tearDown(self):
        User.User_list = []

    def test_init(self):
        """
        test init help test if the object is initialized properly
        """
        self.assertEqual(self.new_credentials.username, "Kenneth")
        self.assertEqual(self.new_credentials.account, "facebook")
        self.assertEqual(self.new_credentials.passwords, "kys1112")

    def test_save_details(self):
        self.new_credentials.save_details()
        self.assertEqual(len(User.User_list), 1)

    def test_multiple_saves(self):
        self.new_credentials.save_details()
        test_credential = User("kent", "twitter", "1234ae")
        test_credential.save_details()
        self.assertEqual(len(User.User_list), 2)

    def test_delete_credentials(self):
        self.new_credentials.save_details()
        test_credential = User("ken", "intagram", "iii111")
        test_credential.save_details()
        self.new_credentials.delete_credential()
        self.assertEqual(len(User.User_list), 1)


if __name__ == '__main__':
    unittest.main()

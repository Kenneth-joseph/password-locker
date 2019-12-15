import unittest
from password import User


class TestUser(unittest.TestCase):

    def setUp(self):
        self.new_credentials = User("Kenneth", "facebook", "kys1112")

    def test_init(self):
        """
        test init help test if the object is initialized properly
        """
        self.assertEqual(self.new_credentials.username, "Kenneth")
        self.assertEqual(self.new_credentials.account, "facebook")
        self.assertEqual(self.new_credentials.passwords, "kys1112")

    def test_save_details(self):
        self.new_credentials.save_details()
        self.assertEqual(len(User.User_list),1)


if __name__ == '__main__':
    unittest.main()

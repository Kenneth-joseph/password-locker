import unittest
from password import User


class TestUser(unittest.TestCase):

    def setUp(self):
        self.new_user = User("Kenneth", "kys1112")

    def test_init(self):
        """
        test init help test if the object is initialized properly
        """
        self.assertEqual(self.new_user.username, "Kenneth")
        self.assertEqual(self.new_user.passwords, "kys1112")


if __name__ == '__main__':
    unittest.main()

import unittest

from locker import Credential, User


class TestUser(unittest.TestCase):
    """Test class that defines test cases for the User class.
    """

    def setUp(self):
        """Set up method to run before each test case."""
        self.new_user = User("trucktar", "TruckOnTAR")

    def test_create_user(self):
        """Test case to test if user is created properly."""
        self.assertEqual(self.new_user.username, "trucktar")
        self.assertEqual(self.new_user.password, "TruckOnTAR")

    def test_save_user(self):
        """Test case to test if user is saved successfully."""
        self.new_user.save_user()
        self.assertEqual(len(User.user_list), 1)


class TestCredential(unittest.TestCase):
    """Test class that defines test cases for the Credential class.
    """

    pass


if __name__ == "__main__":
    unittest.main()

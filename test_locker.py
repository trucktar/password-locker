import unittest

from locker import Credential, User


class TestUser(unittest.TestCase):
    """Test class that defines test cases for the User class.
    """

    def setUp(self):
        """Set up method to run before each test case."""
        self.new_user = User("trucktar", "TruckOnTAR")

    def tearDown(self):
        """Clean up logic after each test case."""
        User.user_list.clear()

    def test_create_user(self):
        """Test case to test if user is created properly."""
        self.assertEqual(self.new_user.username, "trucktar")
        self.assertEqual(self.new_user.password, "TruckOnTAR")

    def test_save_user(self):
        """Test case to test if user is saved successfully."""
        self.new_user.save_user()
        self.assertEqual(len(User.user_list), 1)

    def test_save_multiple_users(self):
        """Test case to test if multiple users are saved successfully."""
        self.new_user.save_user()
        other_user_1 = User("johndoe", "JohnDOE")
        other_user_1.save_user()
        other_user_2 = User("pipfile", "PipFILE")
        other_user_2.save_user()

        self.assertEqual(len(User.user_list), 3)


class TestCredential(unittest.TestCase):
    """Test class that defines test cases for the Credential class.
    """

    pass


if __name__ == "__main__":
    unittest.main()

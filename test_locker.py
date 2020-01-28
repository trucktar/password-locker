import unittest

from locker import Credential, UserAccount


class TestUser(unittest.TestCase):
    """Test class that defines test cases for the UserAccount class."""

    def setUp(self):
        """Set up method to run before each test case."""
        self.new_account = UserAccount("trucktar", "TruckOnTAR")
        self.new_account.create_account()

    def tearDown(self):
        """Clean up logic after each test case."""
        UserAccount.user_list.clear()

    def test_init(self):
        """Test case to test if account is instantiated properly."""
        self.assertEqual(self.new_account.username, "trucktar")
        self.assertEqual(self.new_account.password, "TruckOnTAR")

    def test_create_account(self):
        """Test case to test if an account is created successfully."""
        self.assertEqual(len(UserAccount.user_list), 1)

    def test_create_multiple_accounts(self):
        """Test case to test if multiple accounts are created successfully."""
        newer_account = UserAccount("johndoe", "JohnDOE")
        newer_account.create_account()

        newest_account = UserAccount("pipfile", "PipFILE")
        newest_account.create_account()

        self.assertEqual(len(UserAccount.user_list), 3)

    def test_delete_account(self):
        """Test case to test if an account is deleted successfully."""
        self.new_account.delete_account()
        self.assertEqual(len(UserAccount.user_list), 0)

    def test_login_account(self):
        """Test case to test if account login actually works."""
        UserAccount.login_account(self)
        self.assertEqual(UserAccount.active_user, self)

    def test_find_account_by_username(self):
        """Test case to check if account can be found by username."""
        newer_account = UserAccount("johndoe", "JohnDOE")
        newer_account.create_account()

        self.assertEqual(
            UserAccount.find_account_by_username("trucktar"), self.new_account
        )
        self.assertEqual(UserAccount.find_account_by_username("johndoe"), newer_account)


class TestCredential(unittest.TestCase):
    """Test class that defines test cases for the Credential class."""

    def setUp(self):
        """Set up method to run before each test case."""
        self.new_credential = Credential("Twitter","trucktar", "TruckOnTAR")

    def test_init(self):
        """Test case to test if account is instantiated properly."""
        self.assertEqual(self.new_credential.sitename, "Twitter")
        self.assertEqual(self.new_credential.username, "trucktar")
        self.assertEqual(self.new_credential.password, "TruckOnTAR")


if __name__ == "__main__":
    unittest.main()

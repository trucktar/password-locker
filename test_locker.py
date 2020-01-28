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
        UserAccount.login_account(self.new_account)
        self.assertEqual(UserAccount.active_user, self.new_account)

    def test_find_account_by_username(self):
        """Test case to check if account can be found by username."""
        newer_account = UserAccount("johndoe", "JohnDOE")
        newer_account.create_account()

        self.assertEqual(
            UserAccount.find_account_by_username("trucktar"), self.new_account
        )
        self.assertEqual(UserAccount.find_account_by_username("johndoe"), newer_account)

    def test_create_credential(self):
        """Test case to test if a credential is created successfully."""
        new_credential = Credential("Twitter", "trucktar", "TruckOnTAR")

        UserAccount.login_account(self.new_account)
        UserAccount.active_user.create_credential(new_credential)

        self.assertEqual(len(self.new_account.credentials), 1)

    def test_create_multiple_credentials(self):
        """Test case to test multiple credentials are created successfully."""
        new_credential = Credential("Twitter", "trucktar", "TruckOnTAR")
        newer_credential = Credential("Instagram", "johndoe", "JohnDOE")

        UserAccount.login_account(self.new_account)
        UserAccount.active_user.create_credential(new_credential)
        UserAccount.active_user.create_credential(newer_credential)

        self.assertEqual(len(self.new_account.credentials), 2)

    def test_delete_credential(self):
        """Test case to test multiple credentials are created successfully."""
        new_credential = Credential("Twitter", "trucktar", "TruckOnTAR")
        newer_credential = Credential("Instagram", "johndoe", "JohnDOE")

        UserAccount.login_account(self.new_account)
        UserAccount.active_user.create_credential(new_credential)
        UserAccount.active_user.create_credential(newer_credential)

        UserAccount.active_user.delete_credential(new_credential)

        self.assertEqual(len(self.new_account.credentials), 1)


class TestCredential(unittest.TestCase):
    """Test class that defines test cases for the Credential class."""

    def setUp(self):
        """Set up method to run before each test case."""
        self.new_credential = Credential("Twitter", "trucktar", "TruckOnTAR")

    def test_init(self):
        """Test case to test if account is instantiated properly."""
        self.assertEqual(self.new_credential.sitename, "Twitter")
        self.assertEqual(self.new_credential.username, "trucktar")
        self.assertEqual(self.new_credential.password, "TruckOnTAR")

    def test_generate_password(self):
        """Test case to check if random password is generated."""
        newer_credential = Credential("Instagram", "johndoe")
        self.assertTrue(newer_credential.password)


if __name__ == "__main__":
    unittest.main()

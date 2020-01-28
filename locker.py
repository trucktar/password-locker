import random
import string


class UserAccount:
    """Class that generates locker account instances."""

    user_list = []  # Empty users list
    active_user = None

    def __init__(self, username, password):
        """Assign account attributes after instantiation.

        Args:
            username: New user's username.
            password: New user's password. 
        """
        self.username = username
        self.password = password
        self.credentials = []

    def create_account(self):
        """Add new account instance to user_list."""
        UserAccount.user_list.append(self)

    def delete_account(self):
        """Remove an account instance from user_list."""
        UserAccount.user_list.remove(self)

    def create_credential(self, credential):
        """Add new credential instance to user credentials.
        
        Args:
            credential: the credential to save for user
        """
        if UserAccount.active_user == self:
            self.credentials.append(credential)

    def delete_credential(self, credential):
        """Remove credential instance from user credentials."""
        if UserAccount.active_user == self:
            self.credentials.remove(credential)

    @classmethod
    def login_account(cls, account):
        """Login to a specific account.
        
        Args:
            account: Locker account to login
        """
        cls.active_user = account

    @classmethod
    def find_account_by_username(cls, username):
        """Finds a locker account that matches a username
        
        Args:
            username: Account username to use as filter
        Returns:
            UserAccount instance
        """
        user_match = filter(lambda user: user.username == username, cls.user_list)
        found_user = next(user_match, None)

        return found_user


class Credential:
    """Class that generates credential instances."""

    def __init__(self, sitename, username, password=None):
        """Assign credential attributes after instantiation.

        Args:
            sitename: Credential's linked site.
            username: Credential's username.
            password: Credential's password. 
        """
        self.sitename = sitename
        self.username = username
        self.password = password if password else Credential.generate_password()

    @classmethod
    def generate_password(cls):
        """Generate a random password for credential."""
        characters = string.ascii_letters + string.digits
        random_characters = random.choices(characters, k=12)
        random_password = "".join(random_characters)

        return random_password

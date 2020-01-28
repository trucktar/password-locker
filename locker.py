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

    def create_account(self):
        """Add new account instance to user_list."""
        UserAccount.user_list.append(self)

    @classmethod
    def login_account(cls, account):
        """Login to a specific account.
        
        Args:
            account: Locker account to login
        """
        cls.active_user = account


class Credential:
    """Class that generates credential instances."""

    pass

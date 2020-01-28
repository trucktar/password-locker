class UserAccount:
    """Class that generates locker account instances."""

    user_list = []  # Empty users list

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


class Credential:
    """Class that generates credential instances."""

    pass

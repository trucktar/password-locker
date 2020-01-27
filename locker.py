class User:
    """Class that generates instances of users
    """

    user_list = []  # Empty users list

    def __init__(self, username, password):
        """Create user attributes after instantiation.

        Args:
            username: New user's username.
            password: New user's password. 
        """

        self.username = username
        self.password = password

    def save_user(self):
        """Append user instance to user_list."""

        User.user_list.append(self)


class Credential:
    """Class that generates instances of credentials
    """

    pass

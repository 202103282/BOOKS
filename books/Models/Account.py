class Account:
    """Represents a user account with email and password, allowing account creation, login, and logout functionality."""

    # Class-level dictionary to store all created accounts with email as the key
    _accounts = {}

    def __init__(self, email: str, password: str, is_logged_in=False, account_type="standard"):
        self._email = email
        self._password = password
        self._is_logged_in = is_logged_in
        self._account_type = account_type

    # Getters
    def get_email(self):
        return self._email

    def get_password(self):
        return self._password

    def get_is_logged_in(self):
        return self._is_logged_in

    def get_account_type(self):
        return self._account_type

    # Setters
    def set_email(self, email):
        self._email = email

    def set_password(self, password):
        self._password = password

    def set_is_logged_in(self, is_logged_in):
        self._is_logged_in = is_logged_in

    def set_account_type(self, account_type):
        self._account_type = account_type

    @classmethod
    def create_account(cls, email: str, password: str, account_type="standard") -> None:
        """Creates a new account with the given email and password, if the email is not already registered."""
        if email in cls._accounts:
            raise ValueError("An account with this email already exists.")
        # Add the new account to the _accounts dictionary
        cls._accounts[email] = cls(email, password, False, account_type)
        print(f"Account created successfully for {email}.")

    def login(self, email: str, password: str) -> bool:
        """Logs in the user if the email and password match an existing account."""
        # Check if the email exists in the _accounts dictionary
        if email in Account._accounts and Account._accounts[email].get_password() == password:
            Account._accounts[email].set_is_logged_in(True)
            print(f"{email} logged in successfully.")
            return True
        print("Invalid email or password.")
        return False

    def logout(self) -> None:
        """Logs the user out if they are logged in."""
        if self.get_is_logged_in():
            self.set_is_logged_in(False)
            print(f"{self.get_email()} logged out successfully.")
        else:
            print(f"{self.get_email()} is not currently logged in.")

    def __str__(self):
        return f"Account(email={self._email}, logged_in={self._is_logged_in})"

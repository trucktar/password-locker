#!/usr/bin/python3

import random
import string

from locker import UserAccount, Credential


def create_account(username, password):
    """Creates password locker account
     
    Args:
        username: Account username
        password: Account password
    """
    new_account = UserAccount(username, password)
    new_account.create_account()


def login_account(username, password):
    """Controls user access to locker account"""
    found_account = UserAccount.find_account_by_username(username)
    try:
        if found_account.password == password:
            UserAccount.login_account(found_account)
    except Exception:
        return None


def delete_account():
    """Remove account from list of users."""
    UserAccount.active_user.delete_account()


def create_credential(sitename, username, password=None):
    """Creates a new credential with custom or randomly generated password.
    
    Args:
        Account: Account linked to credential
        username: Credential username
        password: Credential password; If none, generate random password
    """
    new_credential = Credential(sitename, username, password)
    UserAccount.active_user.create_credential(new_credential)


def display_credentials():
    return UserAccount.active_user.credentials


def delete_credential(credential):
    """Remove credential from user's credentials.
    
    Args:
        credential: the credential to be deleted
    """
    UserAccount.active_user.delete_credential(credential)


def main():
    print("Hello Welcome to PyPass - Python Password Locker.")
    while True:
        print("-" * 15)
        print("1. Create Account")
        print("2. Account Login")
        print("3. Exit")
        print("-" * 15)

        option = int(input("\nEnter option: "))
        if option == 1:
            print("Account Registration")
            print("-" * 15)

            print("Username....")
            username = input()

            print("Password....")
            password = input()

            create_account(username, password)  # Create and save account
            print("\nAccount successfully created!\n")

        elif option == 2:
            if UserAccount.user_list:
                print("Account Login")
                print("-" * 15)

                print("Username....")
                username = input()

                print("Password....")
                password = input()

                login_account(username, password)
                user_active = UserAccount.active_user
                while user_active:
                    print("\n")
                    print("-" * 15)
                    print("1. Display Credentials")
                    print("2. Create Credential")
                    print("3. Delete Credential")
                    print("4. Delete Account")
                    print("5. Main Menu")
                    print("-" * 15)

                    option = int(input("\nEnter option: "))
                    if option == 1:
                        print(f"{user_active.username}'s Credentials")
                        print("-" * 15)

                        if display_credentials():
                            for cred in display_credentials():
                                print(
                                    f"{cred.sitename} - {cred.username} - {cred.password}"
                                )
                        else:
                            print("You don't seem to have any credentials.")
                            print("Consider creating one by selecting option 2")

                    elif option == 2:
                        print("New Credential")
                        print("-" * 15)

                        print("Sitename....")
                        sitename = input()

                        print("Username....")
                        username = input()

                        print("Password....")
                        password = input()

                        create_credential(sitename, username, password)
                        print("\nCredential successfully created!\n")

                    elif option == 3:
                        print("This function doesn't work yet. Under implementation")
                        
                    elif option == 4:
                        print("You are about to delete your account....")
                        confirmed = input("Do you wish to continue.... [y/N]")

                        if confirmed:
                            delete_account()
                            print("\nAccount successfully deleted!\n")

                    elif option == 5:
                        break

                    else:
                        print(
                            "I really didn't get that. Please use the provided options"
                        )
            else:
                print(
                    "You're our first user. Please select option 1 to create account."
                )

        elif option == 3:
            print("Bye .......")
            break

        else:
            print("I really didn't get that. Please use the provided options")


if __name__ == "__main__":
    main()

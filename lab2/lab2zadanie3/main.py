from singleton.authenticator import Authenticator

def main():
    auth1 = Authenticator()
    auth2 = Authenticator()

    print(auth1 is auth2)  # True, оскільки обидва посилання на той самий екземпляр

    print(auth1.authenticate("admin", "password"))  # True
    print(auth2.authenticate("user", "pass"))       # False

if __name__ == "__main__":
    main()

import threading

class Authenticator:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
        return cls._instance

    def authenticate(self, user, password):
        # Умовна логіка автентифікації
        return user == "admin" and password == "password"

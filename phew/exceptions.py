class WifiException(Exception):
    pass

class WrongPasswordException(WifiException):
    pass

class SSIDNotFoundException(WifiException):
    pass

class ConnectingFailedException(WifiException):
    pass

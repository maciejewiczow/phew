class WifiException(Exception):
    pass

class WrongPasswordException(WifiException):
    pass

class APNotFoundException(WifiException):
    pass

class ConnectingFailedException(WifiException):
    pass

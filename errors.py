class UserNameTooShortError(Exception):
    def __init__(self, message):
        super().__init__(message)


class NameNonCharError(Exception):
    def __init__(self, message):
        super().__init__(message)


class IllegalEmailFormatError(Exception):
    def __init__(self, message):
        super().__init__(message)


class IllegalPasswordFormatError(Exception):
    def __init__(self, message):
        super().__init__(message)


class IllegalBirthdayError(Exception):
    def __init__(self, message):
        super().__init__(message)


class UserTooYoungError(Exception):
    def __init__(self, message):
        super().__init__(message)
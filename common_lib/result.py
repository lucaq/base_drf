class Result:
    def __init__(self, err=None, msg=None):
        self._err = err
        self._msg = msg

    @property
    def message(self):
        return self._msg

    @property
    def error(self):
        return self._err

    @property
    def has_error(self):
        return self._err is not None

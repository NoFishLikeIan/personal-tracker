from flask import jsonify


class HttpError(Exception):

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        if self.status_code is not None:
            rv['error'] = self.status_code

        return rv


def error_handler(error):

    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


class InvalidArguments(HttpError):
    status_code = 422


class FailedDatabaseConnection(HttpError):
    status_code = 502

import base64


class EncodingHandler:
    def __init__(self):
        print 'w0t w0t .o/'

    @staticmethod
    def encode(base64_object, method='base64'):
        obj = None
        if method == 'base64':
            obj = base64.b64encode(str(base64_object))
        # Multiple options here.
        return obj

    @staticmethod
    def decode(base64_object, method='base64'):
        obj = None
        if method == 'base64':
            obj = base64.b64decode(str(base64_object))
        # Multiple options here.
        return obj








class ObjectDecodingException(Exception):
    def __init__(self, obj_type, j):
        self.obj_type = obj_type
        self.json = j

    def __str__(self):
        return "Exception trying to decode a %s object." % (
            self.obj_type)

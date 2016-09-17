class FundamentalType(object):
    def __init__(self, name):
        self._name = name

    @property
    def typename(self):
        return self._name


class StructureType(object):
    def __init__(self, name, fields):
        self._fields = fields
        self._name = name

    @property
    def typename(self):
        return self._name

    @property
    def fields(self):
        for i, v in enumerate(self._fields):
            yield v, 'f' + str(i)

class ArrayType(object):
    def __init__(self, basetype, size):
        self.basetype = basetype
        self.size = size

    @property
    def typename(self):
        return '%s[%d]' % (self.basetype.typename, self.size)



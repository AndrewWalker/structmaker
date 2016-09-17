import copy
import numpy.random as nr
from .model import *

class SimpleStructureGenerator(object):
    def __init__(self, fundamental_types):
        self.array_len_lambda = 4
        self.array_len_min = 2
        self.struct_len_lambda = 4
        self.struct_len_min = 2
        self.p_fundamental = 0.7
        self.p_array = 0.1
        self.fundamental_types = copy.deepcopy(fundamental_types)
        assert(len(self.fundamental_types)>0)

    def random_structs(self, nameprefix, size):
        structs = []
        for i in xrange(size):
            s = self._random_struct(structs, nameprefix + str(i))
            structs.append(s)
        return structs

    def _random_scalar_type(self, compound_types):
        if len(compound_types) == 0 or nr.random() < self.p_fundamental:
            t = nr.choice(self.fundamental_types)
            return FundamentalType(t)
        return nr.choice(compound_types)

    def _random_array_length(self):
        n = nr.poisson(lam=self.array_len_lambda, size=1)
        return n+self.array_len_min

    def _random_type(self, compound_types):
        basetype = self._random_scalar_type(compound_types)
        if nr.random() < self.p_array:
            return ArrayType(basetype, self._random_array_length())
        return basetype

    def _random_struct_size(self):
        n = nr.poisson(lam=self.struct_len_lambda, size=1)
        return n+self.struct_len_min

    def _random_struct(self, compound_types, name):
        nfields = self._random_struct_size()
        it = xrange(nfields)
        fields = [ self._random_type(compound_types) for _ in it ]
        return StructureType(name, fields)


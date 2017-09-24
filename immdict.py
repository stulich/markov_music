class ImmDict:
    """A class representing an immutable dictionary (ImmDict).
    This class wraps a Python dictionary to provide an immutable version.
    This class is used to store the markov chain as prefix-suffix pairs.
    The keys are the prefix tuples. The value mapped to a key is a suffix,
    which is also represented by an immutable dictionary (ImmDict).
    """
    def __init__(self):
        self.value={}

    def put(self, key, value):
        """returns new Immdict instance with the parameters added to
        its dictionary"""
        copy=self.value.copy()
        copy[key]=value
        new_dict=ImmDict()
        new_dict.value=copy
        #print(new_dict.value)
        return new_dict

    def get(self,key):
        """returns the value mapped to the key"""
        copy=self.value.copy()
        return copy[key]

    def keys(self):
        """returns copy of list of keys in dictionary"""
        copy=self.value.copy()
        return list(key for key in copy)

    def values(self):
        copy = self.value.copy()
        return list(copy[key] for key in copy)
from immdict import ImmDict
import random

"""
dictionary where key maps to another dictionary where the suffixes are keys and values are frequencies
"""
def empty_suffix():
    """Returns an instance of the ImmDict class- an empty immutable dictionary."""
    return ImmDict()

def add_word(suffix, word):
    """returns a new ImmDict instance with word added to its list
      If it exists in the suffix. adds the word as a key and increments that key’s frequency count
      If not, it enters the word with a frequency of 1."""
    if word not in suffix.keys():
        new_dict=suffix.put(word, 1)
        return new_dict
    else:
        updated_value=suffix.get(word)+1
        new_dict=suffix.put(word,updated_value)
        return new_dict

def choose_word(chain, prefix, randomizer):
    """finds the suffix (an ImmDict) associated with the prefix in the chain
     then randomly chooses a word in the suffix and returns """
    suffix=chain.get(prefix)
    the_suffixes=list_of_suffixes(suffix)
    the_place=randomizer(len(the_suffixes))
    return the_suffixes[the_place-1]

def list_of_suffixes(input_dict_of_suffixes):
    return list(key for key in input_dict_of_suffixes.keys() for x in range(input_dict_of_suffixes.get(key)))
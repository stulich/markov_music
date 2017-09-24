from functools import*
from prefix import*
from suffix import*
"""The functions in this module build the Markov chain. A text file is
passed in as well as a randomizer (see the markov and markov_main modules)
A Markov chain is returned as an ImmDict instance. Imports prefix and
suffix."""

NONWORD="\n"

def build(file_name):
    """returns an ImmDict instance, calls pairs_gen and passes that to build_chain"""
    da_generator=pairs_gen(file_name,line_gen)
    return(build_chain(add_to_chain,da_generator,empty_suffix()))

def build_chain(function_to_add_prefix, generator, empty_dict):
    """returns an immdict object containing complete Markov Chain"""
    da_chain=reduce(function_to_add_prefix, generator, empty_dict)
    return da_chain

def add_to_chain(the_chain, pair):
    """returns a new ImmDict with the pair added to it
    if prefix exists in data structure the word freq will increase in suffix
    if prefix doesn't exist new pair is added"""
    the_prefix=pair[0]
    word=pair[1]

    if the_prefix in the_chain.keys():
        suffix=the_chain.get(the_prefix)
        new_chain = the_chain.put(the_prefix,add_word(suffix, word))
    else:
        da_chain=the_chain.put(the_prefix,empty_suffix())
        suffix=da_chain.get(the_prefix)
        new_chain = da_chain.put(the_prefix,add_word(suffix, word))
    return new_chain


def line_gen(file):
    """returns generator object that produces lines from the text file
    upon demand, loop is allowed here"""
    with open(file) as the_file:
            yield the_file.readlines()

def pairs_gen(the_file, line_gen):
    """calls line_gen to get lines of text, returns gernartor that produces
    tuples, each tuple contains prefix and the following word in text"""
    start_prefix=(NONWORD,NONWORD)
    gen= line_gen(the_file)

    for line in gen:
         for word in str(line).split():
            yield (start_prefix, word )
            start_prefix=shift_in(start_prefix,word)


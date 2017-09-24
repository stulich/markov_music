from prefix import*
from suffix import*

"""The functions generate a string of words chosen from the Markov chain
built by the builder module, """

def get_word_list(markov_chain, prefix, randomizer,num_words_generate, NONWORD):
    """returns tuple of words with length equal to number of words passed in unless nonword was encountered first"""
    returner=(helper(markov_chain,prefix,randomizer, num_words_generate,NONWORD,[]))
    flipped=list(reversed(returner))
    return tuple(flipped)

def helper(markov_chain, prefix, randomizer,num_words_generate, NONWORD,accumulator):
    da_word=choose_word(markov_chain,prefix,randomizer)
    if(num_words_generate>0 & (da_word!=NONWORD)):
        helper(markov_chain, shift_in(prefix,da_word), randomizer,num_words_generate-1, NONWORD,accumulator)
        accumulator.append(da_word)
    return accumulator

def generate(markov_chain, randomizer,num_words_generate, NONWORD):
    """returns a string containing the words returned from get_word_list"""

    da_tuple=get_word_list(markov_chain, new_prefix(NONWORD,NONWORD), randomizer,num_words_generate, NONWORD)
    return " ".join(da_tuple)


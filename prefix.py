def new_prefix(first, second):
    """"returns a tuple witht the two words given"""
    the_list=[first, second]
    return tuple(the_list)

def shift_in(the_tuple, the_word):
    """takes tuple, returns new tuple with word shifted in to second spot and
    original second spot at first"""
    the_list=[the_tuple[1],the_word]
    return tuple(the_list)

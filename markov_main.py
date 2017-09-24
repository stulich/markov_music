import builder
import generator
import random

def randomizer(bound):
    return random.randint(1, bound)

if __name__ == "__main__":
    file_name = 'music_notes.txt'
    chain = builder.build(file_name)
    num_words = 40
    outstr = generator.generate(chain, randomizer, num_words, builder.NONWORD)
    print(outstr[2::])
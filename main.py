import search.searchPart
import guess.guessPhrase

import random



def generate_phrase_to_guess(phrases):

    rand_selected = random.choice(phrases)
    phrase = rand_selected
    generated_guess_list = (lambda phrase1: phrase1.split())(phrase)

    return generated_guess_list


# main  block executes here
if __name__ == '__main__':
    # read from internet set of phrases
    data_input = search.searchPart.retrieve_input_from_inet()
    data_input = data_input[1:]

    # randomly select one phrase from prepared set of phrases
    # in order to test - just comment
    random_selected_phrase = generate_phrase_to_guess(data_input[:])
    # in order to test uncomment
    #random_selected_phrase = (lambda phrase1: phrase1.split())('Mission is')

    # start game of guess phrase words by entered letters
    guess.guessPhrase.guess_random_phrase(random_selected_phrase)

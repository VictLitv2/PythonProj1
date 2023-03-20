import time

generate_enc_part = lambda length: "_" * length


def encrypt_for_user(phrase):
    result = []
    for phrase_part in phrase:
        enc_part = generate_enc_part(len(phrase_part))
        result.append(enc_part)
    return result


def phrases_are_equal(origin_phrase, user_decrypted_phrase):
    non_empty = lambda word: word != None and len(f'{word}'.lstrip(' ').rstrip(' ')) > 0

    both_non_empty = non_empty(origin_phrase) == True and non_empty(user_decrypted_phrase) == True

    if (both_non_empty == False):
        return False

    if (len(origin_phrase) != len(user_decrypted_phrase)):
        return False

    counter = 0
    parts_equal = [False] * len(origin_phrase)

    for part in origin_phrase:
        if part == user_decrypted_phrase[counter]:
            parts_equal[counter] = True

        counter = counter + 1

    all_parts_equal = True
    for part_equal in parts_equal:  # all is true
        all_parts_equal = all_parts_equal and part_equal
    return all_parts_equal


def indexes_of_symbol_in_word(word, user_symbol):
    result = [None] * len(word)
    for i, ltr in enumerate(word):
        if str(ltr).lower() == str(user_symbol).lower():
            result[i] = i

    return result


def update_user_guess(user_phrase_part, origin_phrase_part, guessed_positions):
    scores = 0
    result = []
    for s in user_phrase_part:
        result.append(s)

    for guessed_position in guessed_positions:

        counter = 0
        while counter < len(user_phrase_part):
            if guessed_position == None:
                counter = counter + 1
                continue
            try:
                if guessed_position == counter:
                    result[counter] = origin_phrase_part[counter]
                    scores = scores + 5
            except:
                pass
            finally:
                counter = counter + 1

    return (result, scores)


def guess_random_phrase(phrase):
    # 1-st
    encrypted_phrase = encrypt_for_user(phrase)
    print(f'Guess phrase: {encrypted_phrase}')
    print("Enter letter every time till you guess whole phrase...")

    user_decrypted_phrase = []
    for part in encrypted_phrase:
        user_decrypted_phrase.append(part)
    total_points = 0
    # 2-nd - start guess play
    game_start_time = time.time()
    guessed_phrase_to_show = None

    while phrases_are_equal(phrase, user_decrypted_phrase) == False:
        user_symbol = input("Please enter symbol exists in guessed phrase:")

        all_guessed_indexes = build_all_guessed_indexes_for_phrase(phrase, user_symbol)

        total_score_from_update = update_user_guessed_phrase_by_letter_guess(all_guessed_indexes, phrase,

                                                                             user_decrypted_phrase)
        if total_score_from_update != 0:
            total_points = total_points + total_score_from_update
        else:
            total_points = total_points - 1
        guessed_phrase_to_show = ' '.join(user_decrypted_phrase)
        print(f"Your guess:")
        print(f"{guessed_phrase_to_show}")
        time.sleep(.5)
    game_end_time = time.time()


    #check time of game that has been finished - if less equal to 30 sec give additional 100 points
    if game_end_time - game_start_time < 30:
        total_points = total_points + 100
    print(f"Your guess is correct:")
    print(f"{guessed_phrase_to_show}")
    print(f"You earned {total_points} points")


def update_user_guessed_phrase_by_letter_guess(all_guessed_indexes, phrase,
                                               user_decrypted_phrase):
    total_score_from_update = 0
    for phrase_counter, decrypted_phrase_part in enumerate(user_decrypted_phrase):
        origin_phrase_part = phrase[phrase_counter]
        updated_user_guess = update_user_guess(decrypted_phrase_part, origin_phrase_part,
                                               all_guessed_indexes[phrase_counter])

        user_decrypted_phrase[phrase_counter] = "".join(updated_user_guess[0])
        total_score_from_update = total_score_from_update + updated_user_guess[1]
    return total_score_from_update


def build_all_guessed_indexes_for_phrase(phrase, user_symbol):
    all_guessed_indexes = {}
    for phrase_counter, phrase_part in enumerate(phrase):
        indexes_of_symbol = indexes_of_symbol_in_word(f'{phrase_part}', user_symbol)

        all_guessed_indexes[phrase_counter] = indexes_of_symbol
    return all_guessed_indexes

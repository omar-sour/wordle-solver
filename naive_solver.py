words = set()
with open('word_list.txt') as word_list_file:
    for word in word_list_file:
        words.add(word.strip())

def oracle(guess,target_word):
    response = []
    target_letters = set(target_word)
    for i,c in enumerate(guess):
        if c == target_word[i]:      # letter correct and in position
            response.append(c)
        elif c in target_letters:    # letter in word
            response.append('1')
        else:                        # letter not in word
            response.append('2')
    return response

import random as rand

def match_position(word,mask,anti_mask):
    match = all( [word[i] == mask[i] or mask[i] == None for i in range(5)])
    for i,s in enumerate(anti_mask):
        if word[i] in s:
            return False
    return match
    

def match_letters(word, known_inclusions, known_exclusions):
    for c in known_inclusions:
        if c not in word:
            return False
    for c in known_exclusions:
        if c in word:
            return False
    return True

def solve(target_word,verbose=False):
    mask = [None for i in range(5)]
    anti_mask = [set() for i in range(5)]
    known_inclusions = set()  # known included letters
    known_exclusions = set()  # known excluded letters

    candidates = words.copy()

    attempt = 0
    guesses = []
    while attempt < 26:

        # winnow candidates down given the known information
        candidates = {word for word in candidates if match_position(word,mask,anti_mask)}  #  restrict consideration to positional matches
        candidates = {word for word in candidates if match_letters(word,known_inclusions,known_exclusions)}

        # query the oracle with a uniformly random guess from the set of candidates
        guess = rand.choice(tuple(candidates)) 
        guesses.append(guess)
        response = oracle(guess,target_word)

        for i,c in enumerate(response):
            if c == '1':
                known_inclusions.add(guess[i])
                anti_mask[i].add(guess[i])
            elif c == '2': 
                known_exclusions.add(guess[i])
                anti_mask[i].add(guess[i])
            else:
                mask[i] = c
                known_inclusions.add(guess[i])

        if verbose:
            print(f"Attempt #{str(attempt)}  Guess: {guess}" +  '\t' + ''.join(map(lambda x: '_' if x == None else x,mask)))
            print('Included: ' + ''.join(known_inclusions)  +'\tExcluded: ' + ''.join(known_exclusions) + '\t' + "len(candidates):" + str(len(candidates)))
            print("\t" + str(anti_mask))

        if ''.join(response) == guess:
            break

        attempt += 1
    if verbose and ''.join(response) == guess:
        print(f"SOLVED in {attempt} guesses")
    return guesses


if __name__ == '__main__':
    print(solve('hello',verbose=False))
    print(solve('world',verbose=False))
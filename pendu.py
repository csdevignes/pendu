'''
Final project Algorithm Class: Pendu game

@Usage:
python pendu.py

'''

import functions as fct

lexicon_name = "dico.txt"

if __name__ == "__main__":
    word = fct.word_pick(lexicon_name)
    letter = ''
    tried = ''
    wrong = 0
    print(word)

    table = list()
    for i in range(0, len(word)):
        table.append(0)
    k = 0
    while k == 0:
        fct.display_word(word, table)
        tried, letter = fct.enter_letter(tried)
        table, wrong = fct.check_letter(letter, word, table, wrong)
        k = fct.end_game(table, wrong)
    fct.epilogue(word, k)


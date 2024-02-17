'''
Final project Algorithm Class: Pendu game

@Usage:
python pendu.py

'''

import functions as fct
import argparse

# Define argument for usage in command line
parser = argparse.ArgumentParser(description="Argument analysis")
parser.add_argument('-l', '--lexicon', help="Path to word dictionary/lexicon.")
# Argument analysis
args = parser.parse_args()
lexicon_name = args.lexicon
# If no lexicon is defined, load default file
if not lexicon_name:
    lexicon_name = "dico.txt"

word = fct.word_pick(lexicon_name)
letter = ''
tried = ''
wrong = 0

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


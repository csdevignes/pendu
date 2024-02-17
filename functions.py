'''
Final project Algorithm Class: Pendu game

@Usage:
python pendu.py

'''

import random

def word_pick(lexicon_name)-> str:
    '''
    Randomly pick a word from a lexicon file
    which should be a txt file containing
    one word per line
    :param lexicon_name: str, Filename
    :return: str, word picked
    '''
    lexicon = []
    word_count = 0
    with open(lexicon_name, "r", encoding='UTF-8') as f:
        for ligne in f:
            ligne = ligne.strip().upper()
            lexicon.append(ligne)
            word_count += 1
    pick = random.randint(0, word_count)
    return lexicon[pick]

def enter_letter(a):
    '''
    Processes letter input from the user.
    :param a: str, letters already tried
    :return: a: str, b: str letter proposed
    '''
    correct = 0
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    while not correct:
        b = input("Enter a letter :").upper()
        if b not in alpha or len(b) != 1:
            print("This is not a letter !")
        elif b in a:
            print("Letter already tried !")
        else:
            correct = 1
            a = a+b
    return a, b

def display_word(word, table) -> None:
    '''
    Displays the guessed word with guessed letters revealed
    and non-guessed letter as "_"
    :param word: str, word to guess
    :param table: list, table of boolean with letter status
    '''
    disp = ''
    i = 0
    for i in range(len(word)):
        if not table[i]:
            disp = disp + '_'
        else:
            disp = disp + word[i]
    print(disp)

def check_letter(letter, word, table, x):
    '''
    Check if proposed letter is in the word to guess
    update the boolean table accordingly
    return the table and the number of mistakes
    :param letter: proposed letter, str
    :param word: word to guess, str
    :param table: boolean table with correctly guessed letters
    :param x: int, wrong answers
    :return: table, x
    '''
    correct = 0
    i = 0
    for i in range(len(word)):
        if word[i] == letter:
            correct = 1
            table[i] = 1
    if not correct:
        x += 1
    return table, x

def end_game(table, x)-> int:
    '''
    Check if game is finished or not
    :param table: boolean table with status of each guessed letter
    :param x: int, wrong answers
    :return: int, game status
    '''
    if x == 10: #If 10 mistakes, game is over
        return 2
    else: #
        end = 1
        for i in table:
            if not i:
                end = 0
        return end
def epilogue(word, end)-> None:
    '''
    Writes a personalized message depending on game issue
    :param word: word to guess
    :param end: game status (output of end_game())
    '''
    if end == 2:
        print("One try too much...Game over !")
        print(f"The word to guess was {word}.")
    else:
        print(word)
        print("Well done ! You win ! (☆^ー^☆)")
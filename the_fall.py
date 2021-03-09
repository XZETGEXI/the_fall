import os, time

from random import randint

from itertools import cycle

W, H = os.get_terminal_size()

nb_bord = W // 4

MAX_LEN = W // 2

VITESSE = 29

player_index = W // 2

BORDS_CHARS = ['/'] + ['|'] * 5 + ['\\']

bords = cycle(BORDS_CHARS)

CHAR_CHARS = ['ö', 'ö']

char = cycle(CHAR_CHARS)

TAILLE_CHAR = 1

vitesse_aleatoire = input('Vitesse aléatoire ? (0/1) ')

hypno_mode = input('Hypno mode ? (0/1) ')

if hypno_mode:
    MILIEU_CHAR = '_'
else:
    MILIEU_CHAR = '.'




while True:
    direction = randint(0,1) * 2 - 1
    movement = randint(0,1) * direction
    
    nb_bord = max(0, nb_bord + movement)
    nb_bord = min(MAX_LEN, nb_bord)
    
    bord_char = next(bords)
    
    nb_milieu = W - 2 * nb_bord
    
    player_index += randint(0,1) * 2 - 1
    player_index = max(0, player_index)
    player_index = min(nb_milieu - TAILLE_CHAR, player_index)
    
    player = next(char)
    
    inside = MILIEU_CHAR * nb_milieu
    inside = inside[:player_index] + player + inside[player_index + TAILLE_CHAR:]
    
    line = bord_char * nb_bord + inside + bord_char * nb_bord
    print(line)
    
    if vitesse_aleatoire:
        VITESSE += randint(0,1) * 2 - 1
        VITESSE = max(4, VITESSE)
    
    time.sleep(1 / VITESSE)

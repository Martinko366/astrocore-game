WIN_WIDTH = 800
WIN_HEIGHT = 400
TILESIZE = 32
FPS = 60

PLAYER_NAME = None
PLAYER_SEX = None

GROUND_LAYER = 1
BLOCK_LAYER = 2
ITEM_LAYER = 3
PLAYER_LAYER = 4

HP = 100
STAMINA = 100

COINS = 50

PLAYER_SPEED = 4
ADD_PLAYER_SPEED = 0

WHITE = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
DARKGREEN = (30, 135, 61)

TEST = 8

#   = Void
# . = Ground

# P = Player

# B = Border U / b = Border B
# N = Border L / n = Border R
# V = Corner UL / v = Border BL
# M = Corner UR / m = Border BR

# X = Border b2N / x = Border b2n
# C = Border B2N / c = Border B2n

# 1, 2, 3, 4 = Teleports to other level
# 0 = Item (temporary)

level_lobby_map = [
    'VBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBM             ',
    'N.......................................n             ',
    'N.......................................n             ',
    'N.......................................n             ',
    'N.......................................n             ',
    'N.......................................n             ',
    'N.....................................,,cBBBBBBBBBBBBB',
    'N.....................................,,,,,,,,1,,,,,,,',
    'N...................P.................,,,,,,,,1,,,,,,,',
    'N.....................................,,,,,,,,1,,,,,,,',
    'N.....................................,,xbbbbbbbbbbbbb',
    'N...............,,,,,,,,,...............n             ',
    'N...............,,,,,,,,,...............n             ',
    'vbbbbbbbbbbbbbbbbZ,,,,,zbbbbbbbbbbbbbbbbm             ',
    '               N,,,,,,,,,n                            ',
    '               N,,,,,,,,,n                            ',
    '               N,,,,,,,,,n                            ',
    '               N,,,,,,,,,n                            ',
    '               vbbbbbbbbbm                            '
]
level_cafe_map = [
    '                VBBBBBBBBBBBBBBBBBBBBBZ22222222zBBBBBBBBBBBBBBBBBBBBBM',
    '                N....................,,,,,,,,,,,,....................n',
    '                N....................,,,,,,,,,,,,....................n',
    '                N....................................................n',
    '                N....................................................n',
    '                N....................................................n',
    'BBBBBBBBBBBBBBBBx,,..................................................n',
    ',,,,,,,1,,,,,,,,,,,..................................................n',
    ',,,,,,,1,,,,,,,,,,,.P................................................n',
    ',,,,,,,1,,,,,,,,,,,..................................................n',
    'bbbbbbbbbbbbbbbbX,,..................................................n',
    '                N....................................................n',
    '                N....................................................n',
    '                N....................................................n',
    '                N....................................................n',
    '                N....................................................n',
    '                N....................................................n',
    '                N....................................................n',
    '                vbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbm'
]

level_core_map = [
    '                VBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBM',
    '                N....................................................n',
    '                N....................................................n',
    '                N....................................................n',
    '                N....................................................n',
    '                N....................................................n',
    '                N....................................................n',
    '                N....................................................n',
    '                N...P................................................n',
    '                N....................................................n',
    '                N....................................................n',
    '                N....................................................n',
    '                N....................................................n',
    '                N....................................................n',
    '                N....................................................n',
    '                N....................................................n',
    '                N....................,,,,,,,,,,,,....................n',
    '                N....................,,,,,,,,,,,,....................n',
    '                vbbbbbbbbbbbbbbbbbbbbbZ22222222zbbbbbbbbbbbbbbbbbbbbbm'
]


LEVEL_DICT = {
                'lobby': {'title':'Lobby',
                          'found':True,
                          'map':level_lobby_map,
                             'goto':{'up':'cafe',
                                     'left':'cafe',
                                     'down':'cafe',
                                     'right':'cafe'}},

                'cafe': {'title':'Cafe',
                         'found':False,
                         'map':level_cafe_map,
                             'goto':{'up':'core',
                                     'left':'lobby',
                                     'down':'core',
                                     'right':'core'}},

                'core': {'title':'Core',
                         'found':False,
                         'map':level_core_map,
                            'goto':{'up':'cafe',
                                    'left':'cafe',
                                    'down':'cafe',
                                    'right':'cafe'}}
             }

CURRENT_LEVEL = 'lobby'
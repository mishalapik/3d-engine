import msvcrt

ARROWS = {'H': 'up', 'P': 'down', 'K': 'left', 'M': 'right'}

def get_keys():
    '''Возвращает список нажатых за кадр клавиш: 'w', 'a', 's', 'd', 'up', 'down', 'left', 'right'...'''
    keys = []
    while msvcrt.kbhit():
        ch = msvcrt.getwch()
        if ch in ('\xe0', '\x00'):          # префикс спец. клавиши
            code = msvcrt.getwch()          # читаем вторую часть
            name = ARROWS.get(code)
            if name:
                keys.append(name)
        else:
            keys.append(ch.lower())         # lower(): работает и с Caps Lock, и с Shift
    return keys

# import time

# while True:
#     time.sleep(1)
#     for key in get_keys():
#         print(key)
#         if key == 'q':
#             raise SystemExit
    
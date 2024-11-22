import math
from pygame import font

def r_font(content, size = 25, color=000000000): #色はRGBの順に3桁ずつ並べてください
    r = math.floor(color / 1000000)
    g = math.floor(color / 1000) % 1000
    b = color % 1000
    if r <=255 and g <= 255 and b <= 255:
        f = font.Font('Kosugi-Regular.ttf', size) #任意のフォントを入れてください
        t = f.render(content, True, (r, g, b))
        return t
    else:
        f = font.Font('Kosugi-Regular.ttf', size) #任意のフォントを入れてください。
        t = f.render('colorに正しい値を入れてください。', True, (0, 0, 0))
        return t
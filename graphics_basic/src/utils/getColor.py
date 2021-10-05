import random

colorsArray = ['#fff402', '#febe05', '#f4a405', '#e34009', '#cd090d', '#ae132c', '#86124f', '#56146b', '#00346d',
               '#348968', '#67b434', '#cce116']


def get_color(i, start=0):
    return colorsArray[(i + start) % len(colorsArray)]

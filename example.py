import pandas as pd
from matplotlib import pyplot as plt




with open('camelot.txt') as song:
    # print(type(song.read(2)))
    # print(song.read(8))
    print(list(song.readlines()))


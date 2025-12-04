from winreg import KEY_SET_VALUE

import pandas as pd

df = pd.read_csv("pokemon.csv", index_col="Name")

#print(df.loc["Charizard":"Blastoise", ["Height", "Weight"]])

pokemon = input("Enter a pokemon name: ")

try:
    print(df.loc[pokemon])
except KeyError:
    print(f"{pokemon} doesn't exist")









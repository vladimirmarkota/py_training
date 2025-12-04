import pandas as pd

df = pd.read_csv("pokemon.csv")

#tall_pokemon = df[df["Height"] >= 2]

legendary_pokemon = df[df["Legendary"] == 1]
print(legendary_pokemon)

water_pokemon = df[(df["Type1"] == "Water") |
                   (df["Type2"] == "Water")]
print(water_pokemon)

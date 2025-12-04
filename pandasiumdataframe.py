import pandas as pd

data = {"Name" : ["Spongebob", "Patrick", "Squidward"],
        "Age" : [30, 34, 60],
        "Species" : ["Sponge", "Sea star", "Squid"]}

df = pd.DataFrame(data, index=["Employee 1", "Employee 2", "Employee 3"])

new_rows = pd.DataFrame([{"Name": "Sandy", "Age": 28, "Species": "Squirrel", "Job": "Engineer"},
                         {"Name": "Eugene", "Age": 60, "Species": "Crab", "Job": "Manager"}],
                        index=["Employee 4", "Employee 5"])

df = pd.concat([df, new_rows])

df["Job"][0:3] = ["Cook", "N/A", "Cashier"]

#selection by column
#print(df[["Name", "Species"]])

#selection by row




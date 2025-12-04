brojevi = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
brojs = [1, 2, 3, 4, 5]
parni = list(filter(lambda x: x%2==0, brojevi))
print(parni)

mapirano = list(map(lambda x: x*2, brojs))
print(mapirano)




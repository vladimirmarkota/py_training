str1 = "ABECEDA"

mid = int(len(str1) / 2)

srednji = str1[mid]
lijevi = str1[mid -1]
desni = str1[mid +1]

gotov = lijevi + srednji + desni
print(gotov)

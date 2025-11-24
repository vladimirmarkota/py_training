str_x = "vlado je papa, majka, pamajka, jamajka, pa i papalina"

cnt = str_x.count("pa")
print(cnt)

#count() metoda

#s funkcijom

def countt(izreka):
    print("izreka je: ", izreka)
    count = 0
    for i in range(len(izreka)-1):
        count += izreka[i: i+2] == "pa"
    return count
count = countt("vlado je papa, majka, pamajka, jamajka, pa i papalina")
print("pa se prikazuje: ", count, "puta")

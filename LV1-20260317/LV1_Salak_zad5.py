

file = open("C:/Users/Korisnik/Downloads/LV1-20260614/song.txt")

r = {}

for line in file:
    words = line.split()
    for word in words:
        if word in r:
            r[word] += 1
        else:
            r[word] = 1
file.close()

rjednom = []

for word, count in r.items():
    if count == 1:  
        rjednom.append(word)
        
print(r)
print("Broj rijeci koje se pojavljuju jednom:", len(rjednom))
print("Rijeci:", rjednom)
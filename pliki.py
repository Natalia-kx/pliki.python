import sys
print("Generowanie liczb podzielnych przez 4 \n")

file = open("plik.txt", "w")

for i in range(1, 100 + 1):
    if i % 4 == 0:
        file.write(str(i) + " ")
file.close()
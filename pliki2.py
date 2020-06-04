import sys
print("Odczyt liczb z pliku: \n")

file = open("plik.txt", "r")
print(file.read())
file.close()
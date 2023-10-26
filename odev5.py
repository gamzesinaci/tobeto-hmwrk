sayi = int(input("Lütfen Bir sayı girin:"))
orjinal = sayi
tersi = 0

while(sayi > 0):
    hane = sayi % 10
    tersi = tersi * 10 + hane
    sayi = sayi // 10

if orjinal == tersi :
    print("Bu sayı palindrom sayıdır.")
else:
    print("Bu sayı palindrom sayı değildir.")

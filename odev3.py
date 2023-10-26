ilksayi = int(input("ilk sayı:"))
ikincisayi = int(input("ikinci sayı:"))
ucuncusayi = int(input("üçüncü sayı:"))

if(ilksayi >= ikincisayi) and (ilksayi >= ucuncusayi):
    buyuk = ilksayi
elif(ikincisayi >= ilksayi) and (ikincisayi >= ucuncusayi):
    buyuk = ikincisayi
else:
    buyuk = ucuncusayi

print(ilksayi,",",ikincisayi,"ve",ucuncusayi,"üçü arasında en büyük sayı:",buyuk)
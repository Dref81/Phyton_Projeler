def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

print("1.Sayıyı girin")
sayi1 = int(input())

print("2.Sayıyı girin")
sayi2 = int(input())


print("İşlem seçin")
print("1 - Toplama")
print("2 - Çıkarma")
print("3 - Çarpma")
print("4 - Bölme")
secim = input()

if secim == '1':
            print(sayi1, "+", sayi2, "=", add(sayi1, sayi2))

elif secim == '2':
            print(sayi1, "-", sayi2, "=", subtract(sayi1, sayi2))

elif secim == '3':
            print(sayi1, "*", sayi2, "=", multiply(sayi1, sayi2))
elif secim == '4':
            print(sayi1, "/", sayi2, "=", divide(sayi1, sayi2))
else:
            print("Geçersiz girdi")
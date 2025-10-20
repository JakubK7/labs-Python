import matplotlib.pyplot as plt


dane = input('Podaj ciąg liczb całkowitych oddzielonych spacjami')

if dane.strip() == '':
   print('Nie wprowadzono żadnych liczb!!')
else: 
   try:

    liczby = [int(x) for x in dane.split()]

    ilosc = len(liczby)
    suma = sum(liczby)
    srednia = suma / ilosc if ilosc > 0 else 0 

    dodatnie = sum(1 for x in liczby if x > 0)
    ujemne = sum(1 for x in liczby if x < 0)
    zera = sum(1 for x in liczby if x == 0)

    max = max(liczby)
    min = min(liczby)


    print('\n--- Przekształcanie i analiza liczb ---')
    print(f'Lista liczb: {liczby}')
    print(f'Ilość liczb: {ilosc}')
    print(f'Suma: {suma}')
    print(f'Średnia: {srednia}')
    print(f'Ilość liczb dodatnich: {dodatnie}')
    print(f'Ilość lic zb ujemnych: {ujemne}')
    print(f'Ilość zer: {zera}')
    print(f'Największa liczba: {max}')
    print(f'Najmniejsza liczba: {min}')

    plt.subplot(1,3,1)
    plt.hist(liczby, bins=10, edgecolor='pink', color='blue')
    plt.title('Histogram liczb całkowitych')
    plt.xlabel('Wartość')
    plt.ylabel('Częstość')
    plt.show()

    plt.subplot(1,3,2)
    cat = ['Dodatnie', 'Ujemne', 'Zera']
    wartosci = [dodatnie, ujemne, zera]
    plt.bar(cat, wartosci, color=['green', 'red', 'blue'])
    plt.title('Liczba wystąpień liczb dodatnich, ujemnych i zer')
    plt.show()

    plt.subplot(1,3,3)
    plt.plot(range(1, len(liczby) + 1), liczby, marker='o', linestyle='-', color='purple')
    plt.title('Kolejność wprowadzania liczb')
    plt.xlabel('Indeks kolejności')
    plt.ylabel('Wartość liczby')
    plt.grid(True)
    plt.show()

   except ValueError:
    print('Błąd: proszę wprowadzić tylko liczby całkowite oddzielone spacjami.')


